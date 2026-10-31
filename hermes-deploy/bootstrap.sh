#!/usr/bin/env bash
# Sets up a fresh Ubuntu 22.04+/Debian 12+ cloud VM to run Hermes Agent.
# Works on AWS, GCP, Azure, Hetzner, DigitalOcean, or any other VPS.
# Safe to re-run.
#
# Usage (on the VM, from this directory):
#   sudo ./bootstrap.sh
#
# What it does:
#   1. Installs Docker Engine and the compose plugin (official Docker apt repo)
#   2. Creates a 'hermes' system user that owns the agent's data directory
#   3. Firewall: allows SSH in, denies all other inbound traffic (ufw)
#   4. Turns on unattended security upgrades
#   5. Adds a 2 GB swap file if the VM has under 4 GB RAM and no swap
#   6. Installs the compose stack to /srv/hermes and pulls the image
# It does NOT start the agent. That's README steps 3-4.

set -euo pipefail

DEPLOY_DIR=/srv/hermes
DATA_DIR="$DEPLOY_DIR/data"
HERMES_USER=hermes
IMAGE_TAG="${HERMES_IMAGE_TAG:-stable}"
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

log() { printf '\n\033[1;36m==> %s\033[0m\n' "$*"; }

[[ $EUID -eq 0 ]] || { echo "Run as root: sudo $0" >&2; exit 1; }
# shellcheck disable=SC1091
. /etc/os-release
case "$ID" in ubuntu|debian) ;; *) echo "Unsupported OS: $ID (need Ubuntu or Debian)" >&2; exit 1;; esac

export DEBIAN_FRONTEND=noninteractive

log "Installing base packages"
apt-get update -y
apt-get install -y ca-certificates curl gnupg ufw unattended-upgrades

if ! command -v docker >/dev/null 2>&1; then
  log "Installing Docker Engine"
  install -m 0755 -d /etc/apt/keyrings
  curl -fsSL "https://download.docker.com/linux/$ID/gpg" -o /etc/apt/keyrings/docker.asc
  chmod a+r /etc/apt/keyrings/docker.asc
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/$ID ${VERSION_CODENAME} stable" \
    > /etc/apt/sources.list.d/docker.list
  apt-get update -y
  apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
fi
systemctl enable --now docker

log "Creating '$HERMES_USER' user and data directory"
id "$HERMES_USER" >/dev/null 2>&1 || useradd --system --create-home --shell /usr/sbin/nologin "$HERMES_USER"
HERMES_UID="$(id -u "$HERMES_USER")"
HERMES_GID="$(id -g "$HERMES_USER")"
install -d -m 0755 "$DEPLOY_DIR"
install -d -m 0700 -o "$HERMES_UID" -g "$HERMES_GID" "$DATA_DIR"

log "Firewall: allow SSH only"
ufw allow OpenSSH >/dev/null
ufw default deny incoming >/dev/null
ufw default allow outgoing >/dev/null
ufw --force enable

log "Enabling unattended security upgrades"
dpkg-reconfigure -f noninteractive unattended-upgrades

mem_kb="$(awk '/MemTotal/ {print $2}' /proc/meminfo)"
if [[ "$mem_kb" -lt 4000000 ]] && ! swapon --show | grep -q .; then
  log "Low RAM (${mem_kb} kB): adding a 2 GB swap file"
  fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
  grep -q '^/swapfile' /etc/fstab || echo '/swapfile none swap sw 0 0' >> /etc/fstab
fi

log "Installing compose stack to $DEPLOY_DIR"
install -m 0644 "$SRC_DIR/docker-compose.yml" "$DEPLOY_DIR/docker-compose.yml"
cat > "$DEPLOY_DIR/.env" <<EOF
# Compose variables (not agent secrets; those go in $DATA_DIR/.env)
HERMES_IMAGE_TAG=$IMAGE_TAG
HERMES_DATA=$DATA_DIR
HERMES_UID=$HERMES_UID
HERMES_GID=$HERMES_GID
EOF

log "Pulling nousresearch/hermes-agent:$IMAGE_TAG"
docker compose --project-directory "$DEPLOY_DIR" pull

cat <<EOF

Bootstrap complete. Next steps (also in README.md):

  # 3. Start the container (it idles until it has an LLM key and a chat platform)
  cd $DEPLOY_DIR && sudo docker compose up -d

  # 4. One-time setup wizard inside the running container, then restart
  sudo docker exec -it hermes hermes setup
  sudo docker compose restart

  # 5. Check health
  sudo docker exec -it hermes hermes doctor
EOF
