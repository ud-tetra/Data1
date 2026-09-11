#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

corpus_path = Path(sys.argv[1])
manifest_path = Path(sys.argv[2])
plan_path = Path(sys.argv[3])

def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")

records = [json.loads(x) for x in corpus_path.read_text().splitlines() if x.strip()]
manifest = json.loads(manifest_path.read_text())
plan = json.loads(plan_path.read_text())

assert manifest["status"] == "PASS_EXTERNAL_P4RUNTIME_RECEIPT_CORPUS"
assert len(records) == 18 == manifest["receipt_count"]
assert [r["event_seq"] for r in records] == list(range(1, 19))
assert manifest["sequence_gap_count"] == 0

previous = "0" * 64
for r in records:
    stored_record_sha = r["record_sha256"]
    stored_previous = r["previous_chain_sha256"]
    stored_chain = r["chain_sha256"]

    base = {
        k:v for k,v in r.items()
        if k not in ("record_sha256","previous_chain_sha256","chain_sha256")
    }
    record_sha = hashlib.sha256(canonical_bytes(base)).hexdigest()
    chain_sha = hashlib.sha256((previous + record_sha).encode("ascii")).hexdigest()

    assert stored_record_sha == record_sha
    assert stored_previous == previous
    assert stored_chain == chain_sha
    previous = chain_sha

assert previous == manifest["final_chain_sha256"]
assert hashlib.sha256(corpus_path.read_bytes()).hexdigest() == manifest["corpus_sha256"]
assert hashlib.sha256(plan_path.read_bytes()).hexdigest() == manifest["source_plan_sha256"]

source_by_seq = {e["event_seq"]: e for e in plan["events"]}
FIELDS = [
    "event_seq","seam_id","address_code","event_class_code",
    "token_id","predecessor_id","sink_token_id","reentry_seed_id",
    "frame_cert_id","quotient_manifest_id","viability",
]
for r in records:
    src = source_by_seq[r["event_seq"]]
    # Returned packet has numeric address/event class codes, not string labels.
    for f in FIELDS:
        assert r[f] == src[f]

print("EXTERNAL_CORPUS_VERIFICATION_PASS")
print("receipt_count=18")
print("sequence_gap_count=0")
print("corpus_sha256=" + manifest["corpus_sha256"])
print("final_chain_sha256=" + manifest["final_chain_sha256"])
