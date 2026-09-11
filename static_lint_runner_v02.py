#!/usr/bin/env python3
from pathlib import Path
p=Path("scripts/run_github_bmv2.sh").read_text()
checks={
    "deliberate_output_dir":"-o build/p4c_out" in p,
    "json_discovery":"find build/p4c_out -type f -name '*.json'" in p,
    "exact_json_to_controller":"--bmv2-json /work/${BMV2_JSON_REL}" in p,
    "missing_json_hold":"could not resolve compiled BMv2 JSON file" in p,
    "exit_log_capture":"trap cleanup EXIT" in p and "capture_switch_log" in p,
}
for k,v in checks.items():
    print(k, "PASS" if v else "FAIL")
assert all(checks.values())
print("RUNNER_V02_STATIC_PASS")
