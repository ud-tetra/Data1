#!/usr/bin/env python3
import argparse
import hashlib
import json
import threading
import time
from pathlib import Path

from google.protobuf import text_format
from p4.config.v1 import p4info_pb2
from p4runtime_sh import shell as sh

PACKET_FIELDS = [
    "event_seq",
    "seam_id",
    "address",
    "event_class",
    "token_id",
    "predecessor_id",
    "sink_token_id",
    "reentry_seed_id",
    "frame_cert_id",
    "quotient_manifest_id",
    "viability",
]

def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()

def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")

def packet_in_metadata_map(p4info_path):
    info = p4info_pb2.P4Info()
    text_format.Merge(Path(p4info_path).read_text(), info)
    for obj in info.controller_packet_metadata:
        if obj.preamble.name == "packet_in":
            return {md.id: md.name for md in obj.metadata}
    raise RuntimeError("packet_in ControllerPacketMetadata not found in P4Info")

def decode_packet_in(msg, id_to_name):
    out = {}
    for md in msg.metadata:
        name = id_to_name.get(md.metadata_id, f"id_{md.metadata_id}")
        out[name] = int.from_bytes(md.value, byteorder="big", signed=False)
    return out

def send_event(event):
    packet = sh.PacketOut()
    packet.payload = b"UD-P4-ER1"
    packet_values = {
        "event_seq": event["event_seq"],
        "seam_id": event["seam_id"],
        "address": event["address_code"],
        "event_class": event["event_class_code"],
        "token_id": event["token_id"],
        "predecessor_id": event["predecessor_id"],
        "sink_token_id": event["sink_token_id"],
        "reentry_seed_id": event["reentry_seed_id"],
        "frame_cert_id": event["frame_cert_id"],
        "quotient_manifest_id": event["quotient_manifest_id"],
        "viability": event["viability"],
    }
    for field, value in packet_values.items():
        # P4Runtime Shell's documented API accepts metadata values as strings.
        packet.metadata[field] = str(value)
    packet.send()

def append_hash_chain(records):
    previous = "0" * 64
    chained = []
    for rec in records:
        base = dict(rec)
        record_sha = sha256_bytes(canonical_bytes(base))
        chain_sha = sha256_bytes((previous + record_sha).encode("ascii"))
        base["record_sha256"] = record_sha
        base["previous_chain_sha256"] = previous
        base["chain_sha256"] = chain_sha
        chained.append(base)
        previous = chain_sha
    return chained, previous

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grpc-addr", default="p4er1-switch:9559")
    ap.add_argument("--device-id", type=int, default=1)
    ap.add_argument("--p4info", required=True)
    ap.add_argument("--bmv2-json", required=True)
    ap.add_argument("--plan", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--sniff-timeout", type=float, default=12.0)
    args = ap.parse_args()

    plan_path = Path(args.plan)
    plan = json.loads(plan_path.read_text())
    source_events = plan["events"]
    expected_count = len(source_events)
    expected_seq = list(range(1, expected_count + 1))
    id_to_name = packet_in_metadata_map(args.p4info)

    sh.setup(
        device_id=args.device_id,
        grpc_addr=args.grpc_addr,
        election_id=(0, 1),
        config=sh.FwdPipeConfig(args.p4info, args.bmv2_json),
    )

    captured = []
    packet_in = sh.PacketIn()

    def sniff():
        captured.extend(packet_in.sniff(timeout=args.sniff_timeout))

    t = threading.Thread(target=sniff, daemon=True)
    t.start()
    time.sleep(0.5)

    for event in source_events:
        send_event(event)
        time.sleep(0.03)

    t.join(timeout=args.sniff_timeout + 2.0)
    sh.teardown()

    decoded = []
    for msg in captured:
        rec = decode_packet_in(msg, id_to_name)
        if rec.get("switch_seen") == 1:
            decoded.append(rec)

    decoded.sort(key=lambda r: r.get("event_seq", -1))
    observed_seq = [r.get("event_seq") for r in decoded]

    if observed_seq != expected_seq:
        raise SystemExit(
            "FAIL_CLOSED_SEQUENCE: "
            f"observed={observed_seq}, expected={expected_seq}"
        )

    source_by_seq = {e["event_seq"]: e for e in source_events}
    for rec in decoded:
        source = source_by_seq[rec["event_seq"]]
        expected_by_packet_field = {
            "event_seq": source["event_seq"],
            "seam_id": source["seam_id"],
            "address": source["address_code"],
            "event_class": source["event_class_code"],
            "token_id": source["token_id"],
            "predecessor_id": source["predecessor_id"],
            "sink_token_id": source["sink_token_id"],
            "reentry_seed_id": source["reentry_seed_id"],
            "frame_cert_id": source["frame_cert_id"],
            "quotient_manifest_id": source["quotient_manifest_id"],
            "viability": source["viability"],
        }
        for field, expected in expected_by_packet_field.items():
            if rec.get(field) != expected:
                raise SystemExit(
                    "FAIL_CLOSED_SWITCH_ECHO_MISMATCH: "
                    f"event={rec['event_seq']} field={field} "
                    f"observed={rec.get(field)} expected={expected}"
                )

        # Preserve human-readable source provenance without confusing it
        # with the numeric P4 metadata coordinates.
        rec["address_code"] = rec.pop("address")
        rec["event_class_code"] = rec.pop("event_class")
        rec["address"] = source["address"]
        rec["event_class"] = source["event_class"]

    chained, final_chain = append_hash_chain(decoded)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        for rec in chained:
            f.write(json.dumps(rec, sort_keys=True) + "\n")

    manifest = {
        "status": "PASS_EXTERNAL_P4RUNTIME_RECEIPT_CORPUS",
        "physical_promotion": 0,
        "receipt_count": len(chained),
        "first_event_seq": chained[0]["event_seq"] if chained else None,
        "last_event_seq": chained[-1]["event_seq"] if chained else None,
        "sequence_gap_count": 0,
        "final_chain_sha256": final_chain,
        "source_plan_sha256": sha256_bytes(plan_path.read_bytes()),
        "p4info_sha256": sha256_bytes(Path(args.p4info).read_bytes()),
        "bmv2_json_sha256": sha256_bytes(Path(args.bmv2_json).read_bytes()),
        "corpus_sha256": sha256_bytes(out_path.read_bytes()),
        "interpretation":
            "Switch-produced BMv2/P4Runtime identity-bearing source-only receipt corpus; "
            "operational provenance evidence only.",
    }
    Path(args.manifest).write_text(
        json.dumps(manifest, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print("P4_ER1_EXTERNAL_CORPUS_PASS")
    print(f"receipt_count={len(chained)}")
    print(f"corpus_sha256={manifest['corpus_sha256']}")
    print(f"final_chain_sha256={manifest['final_chain_sha256']}")

if __name__ == "__main__":
    main()
