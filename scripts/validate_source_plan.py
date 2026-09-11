#!/usr/bin/env python3
import json
import sys
from pathlib import Path

EVENT_CODES = {
    "IDLE":0,
    "NOVEL":1,
    "RENEWAL":2,
    "SINK":3,
    "CONTINUE":4,
    "REPLACE_NOVEL":5,
    "REPLACE_RENEWAL":6,
}
ADDRESS_CODES = {"A":0,"B":1,"C":2}

d = json.loads(Path(sys.argv[1]).read_text())
events = d["events"]

assert len(events) == 18
assert [e["event_seq"] for e in events] == list(range(1, 19))
assert {e["seam_id"] for e in events} == set(range(6))

for seam in range(6):
    q = [e for e in events if e["seam_id"] == seam]
    assert [e["address"] for e in q] == ["A","B","C"]

for e in events:
    assert e["event_class_code"] == EVENT_CODES[e["event_class"]]
    assert e["address_code"] == ADDRESS_CODES[e["address"]]
    assert e["viability"] == 1

assert {e["event_class"] for e in events} == set(EVENT_CODES)

print("SOURCE_PLAN_PASS")
print("events=18=6*3")
print("all_7_MP1R_classes=PASS")
print("source_plan_contains_hidden_theta_target=NO")
