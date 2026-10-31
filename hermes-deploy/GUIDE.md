# Hermes Agent: deployment options and how to use Claude cloud with it

**Short answer:** Claude cloud can run Hermes, but only while a session is
active. A cloud session's VM pauses after a few minutes idle and is later
reclaimed. So it's a good place to develop and test Hermes, and the wrong
place to host your always-on bot. Production belongs on a small VM
([README.md](README.md)).

---

## 1. Deployment options compared

| # | Option | Always on? | Rough cost | Effort | Use it for |
|---|---|---|---|---|---|
| 1 | **Cloud VM + Docker** (this kit) | Yes | $5–30/mo | Low | **Production default.** Telegram/Slack bot, Hermes cron, persistent memory |
| 2 | Cloud VM, native install + systemd | Yes | $5–30/mo | Low | Same as 1 without Docker: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash`, then `sudo hermes gateway install --system` |
| 3 | PaaS: Fly.io / Railway / Render, Telegram **webhook mode** | Sleeps when idle, wakes on each message | Low, pay per use | Medium | Cheap personal bot. Needs a persistent volume for `/opt/data`, plus `TELEGRAM_WEBHOOK_URL` and `TELEGRAM_WEBHOOK_SECRET`. Scheduled jobs run only while it's awake |
| 4 | Your own hardware: Mac mini, home server, Raspberry Pi 5 | While powered on | $0 | Low | Home lab. The Docker kit works on any Linux box, and the image is published for arm64 |
| 5 | **Claude Code cloud session** (`claude-cloud/`) | **No**, active session only | Included in your Claude plan | Low | **Development and testing**: persona, skills, model choice, prompts |
| 6 | Hybrid: small VM + Modal/Daytona *terminal backend* | Yes (the gateway) | VM plus per-use compute | Medium | Hermes runs its shell commands in serverless sandboxes that hibernate when idle. Good for heavy or untrusted tool work |

**Recommended setup:** option 1 for production and option 5 as your workbench.
Section 4 shows how they fit together.

---

## 2. What works in Claude cloud and what doesn't

Tested in a Claude cloud session with Hermes v0.22.5:

| Works | Doesn't work |
|---|---|
| Hermes container starts in under a minute (image cached by the setup script) | Running 24/7. The VM pauses after a few minutes without Claude activity |
| One-shot questions: `hermes-cc.sh ask "..."` | Hermes's own cron. It runs inside the gateway, which stops when the VM pauses |
| Reaching `api.anthropic.com` under the default **Trusted** network level | OpenRouter and Telegram are blocked until you allow those domains (step 4 below) |
| Testing your `SOUL.md` and skills from the repo (`hermes-cc.sh sync`) | Long-term memory. The sandbox's data lives on the session VM and is lost when the VM is reclaimed |
| A test Telegram bot, while the session is active | The dashboard and the interactive Hermes TUI. Use the VM for those |

Two things the helper handles for you. The session's outbound traffic goes
through an agent proxy that re-signs TLS. `hermes-cc.sh` gives the container
the proxy CA certificate and the proxy settings (by name only). Without that,
every LLM call fails with `SSL certificate problem`.

---

## 3. Step by step: set up Claude cloud for Hermes

### Step 1: Open your cloud environment's settings
At [claude.ai/code](https://claude.ai/code), on the new-session screen, select
the **environment selector** (the first control under the message box).
Hover over your environment and select the **settings icon**.
(In a running session: the caret after the session title, then **Edit cloud environment**.)

### Step 2: Add the setup script
Select **Setup script** and paste the contents of
[`claude-cloud/setup-script.sh`](claude-cloud/setup-script.sh). It pulls the
Hermes image (about 80 s here), and Claude Code caches it, so later sessions
start with the image already on disk. The cache rebuilds about every 7 days.

### Step 3: Add environment variables
Select **Environment variables** and add (in `.env` format):

```text
ANTHROPIC_API_KEY=sk-ant-...      # a separate key just for Hermes, with a spend limit
HERMES_CC_PROVIDER=anthropic
# HERMES_INFERENCE_MODEL=...      # optional; unset uses the provider default
```

- Hermes needs **its own** LLM key. It can't use Claude Code's built-in access.
- Anyone who uses this environment can read these values, so use a dedicated,
  spend-limited key. (Network secrets don't help here: the proxy never
  attaches them to `api.anthropic.com`.)

### Step 4 (optional): Let it reach Telegram or OpenRouter
Under **Network access**, choose **Custom** and keep the default list ticked.
Then add, one per line:

```text
api.telegram.org
openrouter.ai
```

For Telegram, create a **separate test bot** with @BotFather. Don't reuse
your production bot: if the sandbox and the VM poll the same bot, they fight
over its messages. Then add `TELEGRAM_BOT_TOKEN=...` and
`TELEGRAM_ALLOWED_USERS=<your numeric id>` to the environment variables.

### Step 5: Start a new session on this repo
Environment changes apply to **new** sessions. Start one on `cnarasim/TEST`
(branch `hermes-cloud-deploy` until it's merged), then ask Claude in plain
English. Claude runs the helper for you:

| You say | Claude runs |
|---|---|
| "Start Hermes" | `hermes-deploy/claude-cloud/hermes-cc.sh start` |
| "Start Hermes with my test Telegram bot" | `hermes-cc.sh start --with-chat` |
| "Ask Hermes: …" | `hermes-cc.sh ask "…"` |
| "Check Hermes's health" | `hermes-cc.sh doctor` / `status` / `logs` |
| "Stop Hermes" / "Wipe the sandbox" | `hermes-cc.sh stop` / `reset` |

### Step 6: Develop the persona and skills in Git
Keep the files you want to control in the repo:

```text
hermes-config/
  SOUL.md                    # Hermes's persona and standing instructions
  skills/<skill-name>/SKILL.md
```

Then ask Claude, for example: *"Write a Hermes skill that turns an SAP SD
order-to-cash issue description into a structured triage note. Sync it and
test it with three sample issues."* Claude writes the files, runs
`hermes-cc.sh sync`, tests with `ask`, and commits when you're happy.

---

## 4. Best ways to use it

**Pattern: Claude cloud is the workbench, the VM is production.**

```text
 Claude cloud session                 GitHub repo                   Cloud VM (24/7)
 ────────────────────                 ───────────                   ───────────────
 edit SOUL.md / skills   ──commit──▶  hermes-config/   ──deploy──▶  /srv/hermes/data
 test with hermes-cc.sh                (source of truth)             Telegram bot, cron, memory
 test bot only                                                       production bot
```

1. **Change and test in Claude cloud.** Persona tweaks, new skills, and model
   comparisons go through `hermes-cc.sh ask` with a test bot or no bot.
   Nothing touches production.
2. **Review in Git.** Every change to Hermes's behaviour is a diff you can read
   and revert.
3. **Deploy to the VM.** For now, copy the files over and restart:
   ```bash
   scp -r hermes-config <user>@<vm-ip>:~/
   ssh <user>@<vm-ip> 'sudo cp ~/hermes-config/SOUL.md /srv/hermes/data/ \
     && sudo cp -R ~/hermes-config/skills/. /srv/hermes/data/skills/ \
     && sudo chown -R hermes:hermes /srv/hermes/data \
     && cd /srv/hermes && sudo docker compose restart'
   ```
   This adds and overwrites files but never deletes, so skills that Hermes
   creates on the VM are kept. Include `/srv/hermes/data` in your backups.
4. **Use Hermes's cron on the VM for recurring jobs** (daily digests,
   reminders), not Claude scheduled tasks. Hermes's jobs then have its memory
   and deliver to your chat.
5. **Use Claude scheduled tasks for maintenance**, e.g. a weekly task that
   checks Docker Hub for a new Hermes release and opens a PR bumping
   `HERMES_IMAGE_TAG`.

### Rules of thumb
- One bot token per environment: test bot in Claude cloud, production bot on the VM.
- Secrets never go in the repo. They live in the VM's `/srv/hermes/data/.env`
  and in Claude cloud environment variables.
- Use a separate, spend-limited LLM key for each place Hermes runs.
- Always set an allowlist (`TELEGRAM_ALLOWED_USERS` etc.). Hermes can run shell commands.
- Keep the VM dashboard behind an SSH tunnel, and expose no ports except SSH.
