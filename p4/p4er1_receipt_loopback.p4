// SPDX-License-Identifier: Apache-2.0
// UD P4-ER1 identity-bearing receipt loopback v0.1
// Target: BMv2 simple_switch_grpc / v1model

#include <core.p4>
#include <v1model.p4>

#define CPU_PORT 510

@controller_header("packet_out")
header p4er1_packet_out_t {
    bit<64> event_seq;
    bit<16> seam_id;
    bit<8>  address;
    bit<8>  event_class;
    bit<64> token_id;
    bit<64> predecessor_id;
    bit<64> sink_token_id;
    bit<64> reentry_seed_id;
    bit<32> frame_cert_id;
    bit<32> quotient_manifest_id;
    bit<8>  viability;
}

@controller_header("packet_in")
header p4er1_packet_in_t {
    bit<64> event_seq;
    bit<16> seam_id;
    bit<8>  address;
    bit<8>  event_class;
    bit<64> token_id;
    bit<64> predecessor_id;
    bit<64> sink_token_id;
    bit<64> reentry_seed_id;
    bit<32> frame_cert_id;
    bit<32> quotient_manifest_id;
    bit<8>  viability;
    bit<8>  switch_seen;
}

struct headers_t {
    p4er1_packet_out_t packet_out;
    p4er1_packet_in_t  packet_in;
}

struct metadata_t {
    bit<64> event_seq;
    bit<16> seam_id;
    bit<8>  address;
    bit<8>  event_class;
    bit<64> token_id;
    bit<64> predecessor_id;
    bit<64> sink_token_id;
    bit<64> reentry_seed_id;
    bit<32> frame_cert_id;
    bit<32> quotient_manifest_id;
    bit<8>  viability;
}

parser MyParser(
    packet_in packet,
    out headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t standard_metadata)
{
    state start {
        transition select(standard_metadata.ingress_port) {
            CPU_PORT: parse_packet_out;
            default: accept;
        }
    }

    state parse_packet_out {
        packet.extract(hdr.packet_out);
        transition accept;
    }
}

control MyVerifyChecksum(inout headers_t hdr, inout metadata_t meta) {
    apply { }
}

control MyIngress(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t standard_metadata)
{
    apply {
        if (hdr.packet_out.isValid()) {
            meta.event_seq            = hdr.packet_out.event_seq;
            meta.seam_id              = hdr.packet_out.seam_id;
            meta.address              = hdr.packet_out.address;
            meta.event_class          = hdr.packet_out.event_class;
            meta.token_id             = hdr.packet_out.token_id;
            meta.predecessor_id       = hdr.packet_out.predecessor_id;
            meta.sink_token_id        = hdr.packet_out.sink_token_id;
            meta.reentry_seed_id      = hdr.packet_out.reentry_seed_id;
            meta.frame_cert_id        = hdr.packet_out.frame_cert_id;
            meta.quotient_manifest_id = hdr.packet_out.quotient_manifest_id;
            meta.viability            = hdr.packet_out.viability;

            hdr.packet_out.setInvalid();
            standard_metadata.egress_spec = CPU_PORT;
        } else {
            mark_to_drop(standard_metadata);
        }
    }
}

control MyEgress(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t standard_metadata)
{
    apply {
        if (standard_metadata.egress_port == CPU_PORT) {
            hdr.packet_in.setValid();
            hdr.packet_in.event_seq            = meta.event_seq;
            hdr.packet_in.seam_id              = meta.seam_id;
            hdr.packet_in.address              = meta.address;
            hdr.packet_in.event_class          = meta.event_class;
            hdr.packet_in.token_id             = meta.token_id;
            hdr.packet_in.predecessor_id       = meta.predecessor_id;
            hdr.packet_in.sink_token_id        = meta.sink_token_id;
            hdr.packet_in.reentry_seed_id      = meta.reentry_seed_id;
            hdr.packet_in.frame_cert_id        = meta.frame_cert_id;
            hdr.packet_in.quotient_manifest_id = meta.quotient_manifest_id;
            hdr.packet_in.viability            = meta.viability;
            hdr.packet_in.switch_seen          = 1;
        }
    }
}

control MyComputeChecksum(inout headers_t hdr, inout metadata_t meta) {
    apply { }
}

control MyDeparser(packet_out packet, in headers_t hdr) {
    apply {
        packet.emit(hdr.packet_in);
    }
}

V1Switch(
    MyParser(),
    MyVerifyChecksum(),
    MyIngress(),
    MyEgress(),
    MyComputeChecksum(),
    MyDeparser()
) main;
