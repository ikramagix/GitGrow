[![GitGrowBot Follower (Scheduled)](https://github.com/ikramagix/GitGrowBot/actions/workflows/run_follow.yml/badge.svg)](https://github.com/ikramagix/GitGrowBot/actions/workflows/run_follow.yml)
[![GitGrowBot Unfollower (Scheduled)](https://github.com/ikramagix/GitGrowBot/actions/workflows/run_unfollow.yml/badge.svg)](https://github.com/ikramagix/GitGrowBot/actions/workflows/run_unfollow.yml)
[![GitGrowBot Stargazer Shoutouts (Manual)](https://github.com/ikramagix/GitGrowBot/actions/workflows/stargazer_shoutouts.yml/badge.svg)](https://github.com/ikramagix/GitGrowBot/actions/workflows/stargazer_shoutouts.yml)

# GitGrowBot

GitGrowBot is your personal GitHub networking assistant. It's an automation tool designed to help you **grow** and **nurture** your developer network organically. With GitGrowBot, you’ll:

* **Follow** users from our curated list, up to a configurable limit per run.
* **Unfollow** anyone who doesn’t follow you back, because **reciprocity** matters.
* **Star** and **unstar** repositories with the same give-and-take logic.

All actions run on a schedule (or on demand) in GitHub Actions, so you never need to manually review your follow list. Just set it up, sit back, and let GitGrowBot handle your networking while you focus on coding.

- 🤔 [How it works](#how-it-works)
- ❔[Features](#features)
- ⏭️ [Getting started](#getting-started)
- [Local testing](#local-testing)
- ⭐ [Join more than 91,000 users!](#join-more-than-91000-users)
- [Configuration](#configuration)
- [Repository structure](#repository-structure)
- [Manual Troubleshooting Runners (optional)](#manual-troubleshooting-runners-optional)
- 🤝 [Contributing](#contributing)

## How it works

The motto **“You only get what you give”** drives GitGrowBot’s behavior:

1. GitGrowBot **follow** someone for you—chances are, they’ll notice and **follow you back** (especially if they use GitGrowBot too!).  
2. If they **don’t** reciprocate by the next run, GitGrowBot quietly **unfollows** them.
3. You star their repo, they star yours; you unstar, GitGrowBot unstars theirs.

## Features

- **Automated Follow / Unfollow**  
  - Follows 5 to 155 fresh users each run, from `config/usernames.txt` (**now over 91,000 deduplicated, proofchecked usernames**).
  - Only targets users who have been active in the last 30 days for maximum impact.
  - Duplicates and dead accounts are continuously pruned and removed.
  - Unfollows non-reciprocals.  
  - Skips any usernames you whitelist.  
- **Cleaner utility** (`scripts/duplicates.py`)  
  - Deduplicates and prunes dead GitHub usernames locally.  
- **Offline logging**  
  - Records missing usernames in `logs/offline_usernames-<timestamp>.txt`.  
- **CI-first, dev-friendly**  
  - Runs hands-free in Actions.  
  - `.env` support for local testing (optional).  
- **Modular code**  
  - `scripts/gitgrow.py` for main logic.  
  - `scripts/duplicates.py` for list maintenance. 
  - `scripts/integrity.py` for users existence check.
  - `scripts/orgs.py` for optional org member targeting (deprecated, see [CHANGELOG.md](./CHANGELOG.md))
  - `scripts/autotrack.py` tracks all unique stargazers across your repos, logs "unstargazers," and updates `.github/state/stargazer_state.json` (persisted to the `tracker-data` branch).
  - `scripts/autostarback.py` automatically stars back new stargazers (with action limits for rate safety), unstars users who unstar you, and skips users with excessive public repos.

- **Prebuilt Workflow**  
  - `.github/workflows/run_follow.yml`: Runs **every hour at minute 5** (UTC) by default.
  - `.github/workflows/run_unfollow.yml` runs **every 10 hours at minute 5** (UTC) by default.
  - `.github/workflows/manual_follow.yml` – manual trigger: **follow & follow-back only**  
  - `.github/workflows/manual_unfollow.yml` – manual trigger: **unfollow non-reciprocals only**
  - `.github/workflows/run_orgs.yml`: (Optional but deprecated, see [CHANGELOG.md](./CHANGELOG.md) for notes on its usage and status.)
  - `.github/workflows/autostar.yml`: Tracks new/lost stargazers, automatically stars back new stargazers (with rate limiting), and syncs `.github/state/stargazer_state.json` to the `tracker-data` branch.

- **Change Tracking & Artifacts**
  - New and lost stargazers are detected using a persistent `.github/state/stargazer_state.json` file, which is automatically updated and committed to the dedicated `tracker-data` branch.
  - This `tracker-data` branch must exist for full functionality; it is used exclusively for storing state files, so main code and workflow changes remain isolated from tracking data.
  - Artifacts generated for each run (such as the latest stargazer state file) are available for download directly from the Actions tab.
  - All state management (reciprocity, lost stargazers, starred users, etc.) is decoupled from the main codebase by using this separate branch.
  
## Getting started

GitGrowBot is designed to be easy to set up and use. Here’s how you can get started:

1. **Fork** or **clone** this repo.
2. In **Settings → Secrets → Actions**, add your Github PAT as `PAT_TOKEN` (scope: `user:follow`, `public_repo` for starring).
3. In **Settings → Variables → Repository variables**, add **`BOT_USER`** with _your_ GitHub username. *This prevents the workflow from running in other people’s forks unless they set their own name.*
4. **91,000+ members like you who want to grow are waiting for you in** `config/usernames.txt`.  
You can join this list too—see below (**⭐ & Join more than 91,000 users!**).
5. (Optional) Tweak the schedules in your workflow files:
    - `.github/workflows/run_follow.yml` runs **hourly at minute 5** by default.
    - `.github/workflows/run_unfollow.yml` runs **every 10 hours at minute 5** (UTC) by default.
    - `.github/workflows/run_autostar.yml` runs **hourly at minute 20** by default, handling stargazer reciprocity and state management.
6. (Important) Edit `config/whitelist.txt` to protect any accounts you never want the script to act on (no unfollowing, no unstarring for usernames in `whitelist.txt`).
7. (Optional) Copy `.env.example` → `.env` for local testing (or contributors).
8. **Enable** GitHub Actions in your repo settings.
9. (One-time setup) Manually create the `tracker-data` branch in your repository. This branch is used to store and version the persistent stargazer state files (`.github/state/stargazer_state.json`) required for full stargazer reciprocity and tracking.
10. Sit back and code—**GitGrowBot** does the networking (and starring) for you!

## Local testing

If you want to test the bot locally, you can use the provided `scripts/duplicates.py` and `scripts/gitgrow.py` scripts.

1. Copy `.env.example` → `.env` and fill in your PAT.
2. Run the following commands:

```bash
# Example local run of cleanup
python scripts/duplicates.py

# Example local dry-run of follow bot
python scripts/gitgrow.py
````

## Join more than 91,000 users!

Want in? It’s effortless. If you:

1. **Star** this repository, **AND**
2. **Follow** both **[@ikramagix](https://github.com/ikramagix)** and **[@gr33kurious](https://github.com/gr33kurious)**

then your username will be **automatically** added to the master `usernames.txt` list alongside the **91,000+** active members!

Let's grow! 💪

## Configuration

| Options             | Description                                                | Default                |
| ------------------- | ---------------------------------------------------------- | ---------------------- |
| PAT\_TOKEN          | Your PAT with `user:follow` scopes, added in your secrets   | (empty) **required**   |
| USERNAME\_FILE      | File listing target usernames (in the `config/` directory) | `config/usernames.txt` |
| WHITELIST\_FILE     | File listing usernames never to unfollow (in `config/`)    | `config/whitelist.txt` |
| FOLLOWERS\_PER\_RUN | Number of new users to follow each run                     | Random value: `5–155 per run`| 

## Repository structure

```
├── .gitattributes
├── .github
│   └── workflows
│       ├── run_follow.yml              # Scheduled: follow-only (hourly @ :05)
│       ├── run_unfollow.yml            # Scheduled: unfollow-only (daily every 10 hours @ :05 UTC)
│       ├── autostar.yml                # scheduled/manual: stargazer reciprocity (tracks, stars/un-stars on tracker-data branch)
│       ├── run_orgs.yml                # (Deprecated, optional) targets famous organizations for exposure
│       ├── manual_follow.yml           # workflow_dispatch → follow only
│       ├── manual_unfollow.yml         # workflow_dispatch → unfollow only
│       └── stargazer_shoutouts.yml     # keep it deactivated - its purpose is to generate stargazer shoutouts
├── .gitignore
├── README.md
├── config
│   ├── usernames.txt                  # 91,000+ community members (deduped, activity filtered)
│   ├── organizations.txt              # (Optional) org members, only relevant if using run_orgs.yml
│   └── whitelist.txt                  # accounts to always skip
├── logs                               # CI artifacts (gitignored)
│   └── offline_usernames-*.txt
├── requirements.txt
├── scripts
│   ├── gitgrow.py                    # Main follow/unfollow driver
│   ├── unfollowers.py                # Unfollow-only logic
│   ├── duplicates.py                    # Username list maintenance
│   ├── integrity.py                  # Username existence check and cleaning
│   ├── autostarback.py               # Stargazer reciprocity logic: stars/un-stars
│   ├── autotrack.py                  # Stargazer tracker/state generator (called by autostarback.py)
│   └── orgs.py                       # (Deprecated) org follow extension
├── tests
│   ├── test_bot_core_behavior.py     # follow/unfollow/follow-back
│   ├── test_unfollowers.py           # unfollow-only logic
│   └── test_duplicates.py              # cleaner dedupe + missing-user removal
```

### Manual Troubleshooting Runners (optional)

If you ever need to isolate one step for debugging, head to your repo’s **Actions** tab:

* **GitGrowBot Manual Follow** (`.github/workflows/manual_follow.yml`)
  Manually triggers **only** the follow & follow-back logic.
* **GitGrowBot Manual Unfollow** (`.github/workflows/manual_unfollow.yml`)
  Manually triggers **only** the unfollow non-reciprocals logic.

Choose the workflow, click **Run workflow**, select your branch, and go!

## Contributing

We started building GitGrowBot as a peer-to-peer coding challenge on a sleepless night. But it doesn't have to end here.
Feel free to:

1. **Open an issue** to suggest new features, report bugs, or share ideas.
2. **Submit a pull request** to add enhancements, fix problems, or improve documentation.
3. Join the discussion—your use cases, feedback, and code all keep our community vibrant.
4. **Star** the repository to show your support and help others discover it.

Every contribution, big or small, helps everyone grow. Thank you for pitching in!

### With 💛 from contributors like you: 

<a href="https://github.com/ikramagix"><img src="https://img.shields.io/badge/ikramagix-000000?style=flat&logo=github&labelColor=0057ff&color=ffffff" alt="ikramagix"></a> <a href="https://github.com/gr33kurious"><img src="https://img.shields.io/badge/gr33kurious-000000?style=flat&logo=github&labelColor=ab1103&color=ffffff" alt="gr33kurious"></a>

**Happy networking & happy coding!**
*And thank you for saying thank you! If you find this project useful, please consider giving it a star or supporting us on **buymeacoffee** below.*

<div>
<a href="https://www.buymeacoffee.com/ikramagix" target="_blank">
  <img 
    src="https://i.ibb.co/tP37SFx/cuphead-thx-nobg.png" 
    alt="Buy Me A Coffee" 
    width="170">
</a>
</div>

[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge\&logo=buy-me-a-coffee\&logoColor=black)](https://www.buymeacoffee.com/ikramagix)