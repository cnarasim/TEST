# Hermes Agent: cloud deploy kit

Runs [Hermes Agent](https://github.com/NousResearch/hermes-agent) (Nous Research)
24/7 on one cloud VM. You chat with it from Telegram or Slack. It uses the
official Docker image, keeps all state on the VM's disk, and accepts no
inbound traffic except SSH.

| File | Purpose |
|---|---|
| `bootstrap.sh` | Sets up a fresh Ubuntu/Debian VM: Docker, firewall, `hermes` user, swap, pulls the image |
| `docker-compose.yml` | Runs the gateway and the dashboard in one container. Dashboard is on loopback only |
| `hermes.env.example` | Starter secrets template (LLM key, Telegram allowlist) if you don't use the wizard |
| [`GUIDE.md`](GUIDE.md) | **Start here.** Deployment options compared, step-by-step Claude cloud setup, and recommended ways to use it |
| `claude-cloud/setup-script.sh` | Paste into a Claude cloud environment's Setup script. Caches the Hermes image |
| `claude-cloud/hermes-cc.sh` | Runs Hermes as a test sandbox inside a Claude cloud session (`start`, `ask`, `sync`, `stop`) |

## 1. Create the VM

Any provider works. Recommended size: **Ubuntu 24.04 LTS, 2 vCPU / 4 GB RAM, 30 GB disk**.
Hermes calls a hosted LLM API, so the VM needs no GPU.

| Cloud | Instance type | Rough cost |
|---|---|---|
| AWS | `t3.medium` (or `t4g.medium` ARM) | ~$30/mo on-demand |
| GCP | `e2-medium` | ~$25/mo |
| Azure | `B2s` | ~$30/mo |
| Hetzner / DigitalOcean | 2 vCPU / 4 GB plan | ~$5–25/mo |

A 1 GB VM can run it too, though it will rely on swap (bootstrap adds swap
automatically). The image is about 4.3 GB and is published for amd64 and arm64.

Network: allow inbound **TCP 22 only**, ideally only from your own IP. Use SSH
key login. The agent connects out to Telegram, Slack, and the LLM API, so it
needs no open inbound ports.

## 2. Bootstrap

From your laptop:

```bash
scp -r hermes-deploy <user>@<vm-ip>:~/
ssh <user>@<vm-ip>
cd ~/hermes-deploy && sudo ./bootstrap.sh
```

> Use real SSH, not the provider's browser console. The upstream docs warn
> that some web consoles mangle `:`, `@` and `=` in pasted commands and keys.

## 3. Start the container

```bash
cd /srv/hermes && sudo docker compose up -d
```

On first start it writes a default `config.yaml` and `.env` into
`/srv/hermes/data`. Until it has an LLM key and a chat platform, it just idles.

## 4. One-time setup wizard (inside the running container)

```bash
sudo docker exec -it hermes hermes setup
sudo docker compose restart
```

Run setup with `docker exec` as shown, not a separate `docker run … setup`.
A second container would start its own gateway, and two gateways would poll
the same bot. The `hermes` command inside the container drops to the `hermes`
user automatically, so file ownership stays correct.

The wizard asks for:
1. **LLM provider and API key.** Options include Anthropic, OpenRouter,
   Gemini, and Nous Portal (OAuth). The key is saved to `/srv/hermes/data/.env`.
2. **A messaging platform.** For Telegram:
   - Message **@BotFather**, send `/newbot`, and copy the bot token.
   - Message **@userinfobot** to get your numeric user ID.
   - Enter both. **Always set the allowed-users list**, or anyone who finds
     the bot can run commands on your VM through it.

## 5. Verify

```bash
sudo docker exec -it hermes hermes doctor           # health check
sudo docker exec -it hermes hermes gateway status   # should say "Gateway is running"
```

Then message your bot on Telegram. It should reply. In Docker, s6 already
supervises the gateway, so ignore the `gateway status` hint about
`hermes gateway install`.

## Dashboard (optional)

The dashboard listens on the VM's `127.0.0.1:9119` only. Reach it over an
SSH tunnel:

```bash
ssh -L 9119:localhost:9119 <user>@<vm-ip>
# then open http://localhost:9119 on your laptop
```

Don't publish 9119 or 8642 to the internet. The dashboard holds your API keys.

## Day-2 operations

```bash
cd /srv/hermes

# Logs
sudo docker logs -f hermes                                    # container + dashboard
sudo tail -f /srv/hermes/data/logs/gateways/default/current   # gateway

# Hermes CLI inside the container
sudo docker exec -it hermes hermes model           # switch model
sudo docker exec -it hermes hermes gateway setup   # add Slack/Discord/WhatsApp/Email
sudo docker exec -it hermes hermes tools           # enable/disable tools

# Upgrade (all state is in /srv/hermes/data, so nothing is lost)
sudo docker compose pull && sudo docker compose up -d

# Backup (contains secrets, so store it encrypted)
sudo docker compose stop
sudo tar czf ~/hermes-backup-$(date +%F).tgz -C /srv/hermes data
sudo docker compose start
```

To pin a version instead of following `stable`, set e.g. `HERMES_IMAGE_TAG=v0.22.5`
in `/srv/hermes/.env` (tags: [Docker Hub](https://hub.docker.com/r/nousresearch/hermes-agent/tags))
and run `docker compose up -d`.

If `docker compose pull` fails with `429 Too Many Requests` (Docker Hub's
anonymous pull limit), run `docker login` or pull through Google's mirror:
`docker pull mirror.gcr.io/nousresearch/hermes-agent:stable && docker tag mirror.gcr.io/nousresearch/hermes-agent:stable nousresearch/hermes-agent:stable`.

## Security checklist

- [ ] Inbound allows SSH only (cloud security group + `ufw`, which bootstrap configures)
- [ ] `TELEGRAM_ALLOWED_USERS` (or the Slack/Discord equivalent) is set, and `GATEWAY_ALLOW_ALL_USERS=false`
- [ ] Dashboard reached only through the SSH tunnel
- [ ] `/srv/hermes/data` is `0700` and owned by `hermes` (bootstrap sets this)
- [ ] The LLM API key has a spend limit set in the provider console
- [ ] The VM holds no other sensitive credentials. The agent can run shell
      commands, so treat the VM as the agent's machine
