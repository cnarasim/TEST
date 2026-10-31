#!/usr/bin/env bash
# Run Hermes Agent inside a Claude Code cloud session, as a sandbox for testing.
#
# A cloud session's VM pauses after a few minutes idle, so this is for
# testing prompts, skills, models and persona. It is NOT for 24/7 use.
# Production runs on the VM (see ../README.md).
#
#   hermes-cc.sh start [--with-chat]  start Hermes (LLM keys only, unless --with-chat)
#   hermes-cc.sh ask "prompt"         one-shot question; prints only the answer
#   hermes-cc.sh doctor | status | logs
#   hermes-cc.sh sync                 copy ../../hermes-config (SOUL.md, skills/) into Hermes
#   hermes-cc.sh stop                 stop the container (data kept)
#   hermes-cc.sh reset                stop it and delete the sandbox's data
#
# Keys are read from the cloud environment's variables (environment settings
# -> Environment variables) and passed through with `docker run -e NAME`, so
# their values never appear on a command line. Optional settings:
#   HERMES_CC_PROVIDER   provider for `ask`, e.g. anthropic | openrouter | gemini
#   HERMES_INFERENCE_MODEL  model for `ask` (unset = the provider default)

set -euo pipefail

IMG="${HERMES_IMAGE:-nousresearch/hermes-agent:stable}"
NAME=hermes-cc
DATA="${HERMES_CC_DATA:-$HOME/.hermes-cc}"
HUID=10000   # the image's default hermes user
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_CFG="$(cd "$SCRIPT_DIR/../.." && pwd)/hermes-config"

LLM_VARS=(ANTHROPIC_API_KEY OPENROUTER_API_KEY GOOGLE_API_KEY GEMINI_API_KEY
          OPENAI_API_KEY HERMES_INFERENCE_MODEL)
# Messaging tokens are opt-in (--with-chat). If the sandbox and the production
# VM poll the same bot, they fight over its updates. Use a separate test bot.
CHAT_VARS=(TELEGRAM_BOT_TOKEN TELEGRAM_ALLOWED_USERS SLACK_BOT_TOKEN
           SLACK_APP_TOKEN SLACK_ALLOWED_USERS)

die() { echo "hermes-cc: $*" >&2; exit 1; }

ensure_docker() {
  docker info >/dev/null 2>&1 && return
  echo "hermes-cc: starting Docker daemon" >&2
  (nohup dockerd >/tmp/dockerd.log 2>&1 &)
  for _ in $(seq 1 30); do docker info >/dev/null 2>&1 && return; sleep 1; done
  die "Docker daemon did not start (see /tmp/dockerd.log)"
}

ensure_image() {
  docker image inspect "$IMG" >/dev/null 2>&1 && return
  echo "hermes-cc: pulling $IMG (about 4.3 GB; the setup script caches it)" >&2
  docker pull -q "$IMG" \
    || { docker pull -q "mirror.gcr.io/$IMG" && docker tag "mirror.gcr.io/$IMG" "$IMG"; } \
    || die "image pull failed"
}

running() { [[ "$(docker inspect -f '{{.State.Running}}' "$NAME" 2>/dev/null)" == true ]]; }
need_running() { running || die "not running; run: $0 start"; }

sync_cfg() {
  [[ -d "$REPO_CFG" ]] || { echo "hermes-cc: no $REPO_CFG, nothing to sync" >&2; return 0; }
  mkdir -p "$DATA"
  [[ -f "$REPO_CFG/SOUL.md" ]] && cp "$REPO_CFG/SOUL.md" "$DATA/SOUL.md"
  if [[ -d "$REPO_CFG/skills" ]]; then
    mkdir -p "$DATA/skills" && cp -R "$REPO_CFG/skills/." "$DATA/skills/"
  fi
  chown -R "$HUID:$HUID" "$DATA"
  echo "hermes-cc: synced $REPO_CFG into $DATA" >&2
}

cmd_start() {
  local with_chat=0
  [[ "${1:-}" == "--with-chat" ]] && with_chat=1
  ensure_docker; ensure_image
  if running; then echo "hermes-cc: already running" >&2; return; fi
  docker rm -f "$NAME" >/dev/null 2>&1 || true
  install -d -m 0700 -o "$HUID" -g "$HUID" "$DATA"
  sync_cfg

  local args=() v found=0
  local vars=("${LLM_VARS[@]}")
  (( with_chat )) && vars+=("${CHAT_VARS[@]}")
  for v in "${vars[@]}"; do
    if [[ -n "${!v:-}" ]]; then args+=(-e "$v"); [[ "$v" == *_API_KEY ]] && found=1; fi
  done
  (( found )) || echo "hermes-cc: WARNING no LLM API key in the environment; 'ask' will fail until you add one" >&2

  # Claude cloud egress goes through an agent proxy that re-signs TLS with its
  # own CA. Containers trust neither, so hand both in. The CA is a public cert,
  # and the proxy variables are passed by name only (/root/.ccr/README.md).
  local ca=/root/.ccr/ca-bundle.crt
  if [[ -f "$ca" ]]; then
    args+=(-v "$ca:/etc/ssl/certs/ccr-ca-bundle.crt:ro")
    for v in SSL_CERT_FILE REQUESTS_CA_BUNDLE CURL_CA_BUNDLE NODE_EXTRA_CA_CERTS; do
      args+=(-e "$v=/etc/ssl/certs/ccr-ca-bundle.crt")
    done
  fi
  for v in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy; do
    [[ -n "${!v:-}" ]] && args+=(-e "$v")
  done

  docker run -d --name "$NAME" --network host \
    -e HERMES_UID="$HUID" -e HERMES_GID="$HUID" \
    "${args[@]}" -v "$DATA:/opt/data" "$IMG" gateway run >/dev/null

  for _ in $(seq 1 60); do
    docker exec "$NAME" hermes --version >/dev/null 2>&1 && break; sleep 1
  done
  docker exec "$NAME" hermes --version | head -1
  local names=()
  for v in "${vars[@]}"; do [[ -n "${!v:-}" ]] && names+=("$v"); done
  echo "hermes-cc: running. Variables passed through: ${names[*]:-(none)}" >&2
}

cmd_ask() {
  [[ $# -gt 0 ]] || die 'usage: ask "your prompt"'
  need_running
  local extra=()
  [[ -n "${HERMES_CC_PROVIDER:-}" ]] && extra+=(--provider "$HERMES_CC_PROVIDER")
  # -z prints only the final answer; exit 0 = done, 2 = failed/partial
  docker exec -i "$NAME" hermes -z "$*" "${extra[@]}"
}

case "${1:-}" in
  start)  shift; cmd_start "$@" ;;
  ask)    shift; cmd_ask "$@" ;;
  doctor) need_running; docker exec "$NAME" hermes doctor ;;
  status) if running; then echo "running"; docker exec "$NAME" hermes gateway status 2>&1 | head -1; else echo "stopped"; fi ;;
  logs)   need_running; docker logs --tail 50 "$NAME" 2>&1; tail -n 30 "$DATA/logs/gateways/default/current" 2>/dev/null || true ;;
  sync)   sync_cfg; if running; then docker restart "$NAME" >/dev/null; echo "hermes-cc: restarted" >&2; fi ;;
  stop)   if docker stop "$NAME" >/dev/null 2>&1; then echo "stopped"; else echo "not running"; fi ;;
  reset)  docker rm -f "$NAME" >/dev/null 2>&1 || true; rm -rf "$DATA"; echo "sandbox data deleted" ;;
  *)      sed -n '2,/^$/p' "$0" | sed -e '/^$/d' -e 's/^# \{0,1\}//'; exit 2 ;;
esac
