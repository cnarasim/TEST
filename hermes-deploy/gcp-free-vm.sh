#!/usr/bin/env bash
# Creates a Google Cloud "Always Free" e2-micro VM and installs Hermes on it.
#
# Run it from Google Cloud Shell (shell.cloud.google.com, gcloud is already
# signed in there) or from any machine where `gcloud auth login` is done:
#
#   ./gcp-free-vm.sh <project-id>
#
# Free tier terms: one e2-micro, 30 GB standard disk, in us-west1,
# us-central1 or us-east1 only. A billing account must be linked, but usage
# within the limits isn't charged. Set a budget alert anyway, because external
# IPv4 and egress terms change.
#
# e2-micro has 1 GB RAM. Hermes's gateway idles at about 330 MB, and
# bootstrap.sh adds 2 GB of swap. Fine for a chat bot. Heavy browser
# automation needs a bigger VM.

set -euo pipefail

PROJECT="${1:-$(gcloud config get-value project 2>/dev/null || true)}"
[[ -n "$PROJECT" ]] || { echo "usage: $0 <project-id>" >&2; exit 1; }
ZONE="${ZONE:-us-central1-a}"   # must be in us-west1, us-central1 or us-east1
NAME="${NAME:-hermes}"
KIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
G=(--project "$PROJECT" --zone "$ZONE")

case "$ZONE" in
  us-west1-*|us-central1-*|us-east1-*) ;;
  *) echo "WARNING: $ZONE is outside the free-tier regions; you will be billed" >&2 ;;
esac

echo "==> Enabling Compute Engine API (first run takes a minute)"
gcloud services enable compute.googleapis.com --project "$PROJECT"

if gcloud compute instances describe "$NAME" "${G[@]}" >/dev/null 2>&1; then
  echo "==> VM '$NAME' already exists, reusing it"
else
  echo "==> Creating e2-micro VM '$NAME' in $ZONE"
  gcloud compute instances create "$NAME" "${G[@]}" \
    --machine-type e2-micro \
    --image-family ubuntu-2404-lts-amd64 --image-project ubuntu-os-cloud \
    --boot-disk-size 30GB --boot-disk-type pd-standard
fi

echo "==> Waiting for SSH"
for i in $(seq 1 20); do
  gcloud compute ssh "$NAME" "${G[@]}" --command true --quiet >/dev/null 2>&1 && break
  [[ $i -eq 20 ]] && { echo "SSH never came up" >&2; exit 1; }
  sleep 10
done

echo "==> Copying the deploy kit and running bootstrap (pulls a 4.3 GB image, ~5-10 min on e2-micro)"
gcloud compute scp --recurse "$KIT_DIR" "$NAME":~/ "${G[@]}" --quiet
gcloud compute ssh "$NAME" "${G[@]}" --quiet \
  --command "cd ~/$(basename "$KIT_DIR") && sudo ./bootstrap.sh"

cat <<EOF

Done. Finish setup over SSH (README steps 3-5):

  gcloud compute ssh $NAME --project $PROJECT --zone $ZONE
  cd /srv/hermes && sudo docker compose up -d
  sudo docker exec -it hermes hermes model      # pick "OpenAI API", paste key, pick gpt-6-luna
  sudo docker exec -it hermes hermes setup gateway   # connect Telegram + set allowed users
  sudo docker compose restart

To delete everything later:  gcloud compute instances delete $NAME --project $PROJECT --zone $ZONE
EOF
