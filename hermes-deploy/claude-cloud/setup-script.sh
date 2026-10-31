#!/bin/bash
# Claude Code cloud environment setup script for Hermes Agent.
#
# Paste this into your cloud environment's Setup script box
# (claude.ai/code -> environment selector -> settings icon -> Setup script).
#
# It pulls the Hermes image once. Claude Code snapshots the filesystem after
# setup, so later sessions start with the image already on disk. Runs as
# root on Ubuntu 24.04, before environment variables are set.
#
# It must exit 0, or the session won't start. Every step is best-effort.

IMG="nousresearch/hermes-agent:stable"

started_dockerd=0
if ! docker info >/dev/null 2>&1; then
  (dockerd >/var/log/dockerd-setup.log 2>&1 &)
  started_dockerd=1
  for _ in $(seq 1 30); do docker info >/dev/null 2>&1 && break; sleep 1; done
fi

# Docker Hub rate-limits anonymous pulls from shared IPs. Fall back to
# Google's public mirror of Docker Hub.
docker pull -q "$IMG" \
  || { docker pull -q "mirror.gcr.io/$IMG" && docker tag "mirror.gcr.io/$IMG" "$IMG"; } \
  || echo "WARN: Hermes image pull failed; hermes-cc.sh will retry at start" >&2

# Stop dockerd cleanly so the snapshot holds a consistent /var/lib/docker
if [ "$started_dockerd" = 1 ]; then
  pkill -TERM dockerd || true
  for _ in $(seq 1 20); do pgrep -x dockerd >/dev/null || break; sleep 1; done
fi
exit 0
