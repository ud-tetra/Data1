#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

mkdir -p build results logs preflight

NET="p4er1-net"
SW="p4er1-switch"

P4C_IMAGE="${P4C_IMAGE:-p4lang/p4c:latest}"
BMV2_IMAGE="${BMV2_IMAGE:-p4lang/behavioral-model:latest}"
P4RTSH_IMAGE="${P4RTSH_IMAGE:-p4lang/p4runtime-sh:latest}"
PLATFORM="${PLATFORM:-linux/amd64}"

cleanup() {
  docker rm -f "$SW" >/dev/null 2>&1 || true
  docker network rm "$NET" >/dev/null 2>&1 || true
}
trap cleanup EXIT

python3 scripts/validate_source_plan.py config/P4_ER1_SOURCE_PLAN_v0.1.json \
  | tee preflight/SOURCE_PLAN_PREFLIGHT.txt

cleanup
docker network create "$NET" >/dev/null

echo "Pulling public P4 images..."
docker pull --platform "$PLATFORM" "$P4C_IMAGE"
docker pull --platform "$PLATFORM" "$BMV2_IMAGE"
docker pull --platform "$PLATFORM" "$P4RTSH_IMAGE"

{
  echo "platform=$PLATFORM"
  echo "p4c_image=$P4C_IMAGE"
  echo "bmv2_image=$BMV2_IMAGE"
  echo "p4runtime_sh_image=$P4RTSH_IMAGE"
  docker image inspect "$P4C_IMAGE" \
    --format 'p4c_repo_digest={{if .RepoDigests}}{{index .RepoDigests 0}}{{else}}{{.Id}}{{end}}'
  docker image inspect "$BMV2_IMAGE" \
    --format 'bmv2_repo_digest={{if .RepoDigests}}{{index .RepoDigests 0}}{{else}}{{.Id}}{{end}}'
  docker image inspect "$P4RTSH_IMAGE" \
    --format 'p4runtime_sh_repo_digest={{if .RepoDigests}}{{index .RepoDigests 0}}{{else}}{{.Id}}{{end}}'
} | tee results/RUNTIME_IMAGES.txt

echo "Compiling P4_16 source..."
docker run --rm --platform "$PLATFORM" \
  --mount "type=bind,source=$ROOT,target=/work" \
  -w /work \
  "$P4C_IMAGE" \
  p4c --target bmv2 --arch v1model --std p4-16 \
    --p4runtime-files build/p4er1.p4info.txt \
    --p4runtime-format text \
    -o build/p4er1.json \
    p4/p4er1_receipt_loopback.p4

echo "Starting BMv2 simple_switch_grpc..."
docker run -d \
  --name "$SW" \
  --network "$NET" \
  --platform "$PLATFORM" \
  "$BMV2_IMAGE" \
  simple_switch_grpc --log-console --no-p4 --device-id 1 -- \
    --grpc-server-addr 0.0.0.0:9559 \
    --cpu-port 510 >/dev/null

sleep 3

echo "Executing P4Runtime controller / collector..."
CONTROLLER_CMD="source /p4runtime-sh/venv/bin/activate && \
python3 /work/controller/p4er1_controller.py \
--grpc-addr ${SW}:9559 \
--device-id 1 \
--p4info /work/build/p4er1.p4info.txt \
--bmv2-json /work/build/p4er1.json \
--plan /work/config/P4_ER1_SOURCE_PLAN_v0.1.json \
--out /work/results/P4_ER1_EXTERNAL_SOURCE_ONLY_RECEIPTS.jsonl \
--manifest /work/results/P4_ER1_EXTERNAL_CORPUS_MANIFEST.json"

docker run --rm \
  --platform "$PLATFORM" \
  --network "$NET" \
  --mount "type=bind,source=$ROOT,target=/work" \
  -w /work \
  --entrypoint /bin/bash \
  "$P4RTSH_IMAGE" \
  -lc "$CONTROLLER_CMD"

docker logs "$SW" > logs/simple_switch_grpc.log 2>&1 || true

python3 scripts/verify_external_corpus.py \
  results/P4_ER1_EXTERNAL_SOURCE_ONLY_RECEIPTS.jsonl \
  results/P4_ER1_EXTERNAL_CORPUS_MANIFEST.json \
  config/P4_ER1_SOURCE_PLAN_v0.1.json \
  | tee results/VERIFY_EXTERNAL_CORPUS.txt

echo "P4_ER1_GITHUB_ACTIONS_PASS"
