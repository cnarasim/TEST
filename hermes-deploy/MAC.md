# Run Hermes on your Mac mini (M2 Pro, 16 GB)

Assessed from the machine's own readout:

| Check | Value | Verdict |
|---|---|---|
| Chip / RAM | Apple M2 Pro, 10 cores, 16 GB | Plenty. The Hermes gateway idles at about 330 MB |
| Memory free | 40% (about 6 GB) | Fine for Hermes with a cloud model |
| Disk free | **18 GB of 460 GB** | **Too low. Free up space first** (target 50 GB or more) |
| Sleep | `sleep 1`: sleeps after 1 min idle, only kept awake by other apps | **Must change.** If those apps close, the bot goes offline |
| Restart after power cut | `autorestart 0` | Turn on |
| Uptime / load | 17 days, load about 3 on 10 cores | Good, stable |
| Tools | brew, git, python3, ollama present; Docker absent | Good. Install natively, no Docker needed |

**Verdict:** this Mac mini is a better Hermes host than the free cloud VM
(16 times the RAM, a much faster CPU), and electricity at idle should cost
about $1/month. Use **OpenAI `gpt-6-luna`** as the model. Skip local models
on 16 GB: a model small enough to fit (3–8B) is weak at multi-step tool use,
and it would have to process Hermes's ~13K-token prompt on every turn. That
makes replies slow.

---

## Step 1: Free disk space (aim for 50 GB or more free)

Find what's big (read-only):

```bash
ollama list                       # downloaded local models; often 4–40 GB each
du -sh ~/.ollama ~/anaconda3 ~/miniconda3 ~/opt/anaconda3 ~/Library/Caches ~/Downloads 2>/dev/null
```

Typical wins: `ollama rm <model>` for models you don't use, and
`conda clean --all` to remove conda's package cache. Also check
Apple menu → About This Mac → More Info → Storage settings.

## Step 2: Keep the Mac awake and auto-restart after a power cut

```bash
sudo pmset -a sleep 0 autorestart 1
pmset -g | grep -E " sleep|autorestart"    # expect: sleep 0, autorestart 1
```

The display can still sleep. Only system sleep is turned off.

## Step 3: Create a separate macOS user for Hermes (strongly recommended)

Hermes can run shell commands and has a macOS computer-use tool. On your
own account it could reach your files, keychain, SSH keys and browser
sessions. A separate **Standard** (non-admin) user contains that.

System Settings → Users & Groups → **Add User…** → New User: **Standard**,
name `hermes`, then set a password.

## Step 4: Install Hermes as that user

Log in as `hermes`: Apple menu → Lock Screen, then pick `hermes` (or use
fast user switching). In Terminal:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.zshrc

# OpenAI key (not echoed, kept out of shell history) and the cheap model
read -rs "K?OpenAI API key: "; echo
hermes config set OPENAI_API_KEY "$K"; unset K
hermes config set model.provider openai-api
hermes config set model.default gpt-6-luna

hermes gateway setup      # Telegram: bot token from @BotFather + YOUR user id as allowed user
hermes gateway install    # installs the launchd background service
hermes gateway status     # should say running
hermes doctor
```

(`read -rs "K?prompt"` is the zsh form. macOS Terminal uses zsh by default.)

Set a monthly spend limit at platform.openai.com → Settings → Limits.

## Step 5: Switch back to your own account and leave `hermes` logged in

Apple menu → Lock Screen → pick your account. **Don't log `hermes` out.**
Its background service runs only while that user has a session. Message the
bot on Telegram to confirm it replies.

## Reboots and power cuts

- After a restart, log in as `hermes` once (then switch back), and the
  service starts again.
- If **FileVault** is on (`fdesetup status`), the Mac waits at the unlock
  screen after a power cut, so Hermes stays down until someone types the
  password. That's the trade-off for disk encryption. A UPS avoids most of it.

## Day-to-day (as the `hermes` user)

```bash
hermes gateway status | restart | stop
hermes update             # upgrade Hermes
hermes model              # switch model, e.g. to gpt-6-sol for a harder job
```

Back up `~/.hermes` (in the `hermes` user's home). It holds config, keys,
memory and skills.
