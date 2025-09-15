## \[1.0.0] – 2025-05-19 (Pre-release)

* Initial public release of GitGrowBot.
* Automated follow/unfollow via scheduled GitHub Actions.
* Whitelist support to protect accounts from actions.
* Configurable target user list (`usernames.txt`), deduped and checked.
* Only follows accounts active in the last 3 days.
* Username cleaner utility (dedupe, dead user removal, offline logging).
* Manual workflows for on-demand actions and isolated testing.
* Isolated config/testing infrastructure.

**Contributors:**
[@ikramagix](https://github.com/ikramagix), [@gr33kurious](https://github.com/gr33kurious)
[All commits →](https://github.com/ikramagix/GitGrowBot/commits/1.0.0)

---

## \[1.1.0] – 2025-06-04

### Added

* Menu navigation in README.
* Expanded `usernames.txt` (now over 161,000 deduplicated, active users).
* Stargazer tracking:

  * `.github/workflows/stargazer_shoutouts.yml` tracks new/lost stargazers.
  * Artifacts for each run, state persisted on `tracker-data` branch.
* Follow logic now targets only users active in last 3 days.

### Changed

* Follower batch size is now random (5–55 per run) for rate-limit safety.

### Deprecated

* `.github/workflows/run_orgs.yml` and `scripts/orgs.py` (org-member mass-follow):

  * **Deprecated due to poor results** – did not increase profile visits or organic followers.

### Maintainer-only

* Local scripts (`.env`, `scripts/duplicates.py`, `scripts/gitgrow.py` for local runs).
* Manual workflows (`manual_follow.yml`, `manual_unfollow.yml`).
* Stargazer shoutouts workflow is for repo analytics/discussion, not for general users.

**Contributors:**
[@ikramagix](https://github.com/ikramagix)
[All commits →](https://github.com/ikramagix/GitGrowBot/commits/1.1.0)

## [1.1.1] – 2025-06-29

### Added

* **Stargazer Reciprocity**
  - New scripts: `scripts/autostar.py` and `scripts/autotrack.py` for automated stargazer reciprocity.
    - Automatically stars a public repository for each new stargazer (subject to per-user repo limit, skip if >50 repos).
    - Unstars users who remove their star.
    - Hard limits (e.g. max 5 new stargazers and 5 growth users per run) to avoid API and rate-limit abuse.
    - Growth starring from `config/usernames.txt` still supported (sample, skip excessive repos).
* **Workflow Integration**
  - `.github/workflows/autostar.yml`: Scheduled and manual stargazer reciprocity workflow.
  - All state and log artifacts (e.g. `stargazer_state.json`) are versioned to the `tracker-data` branch and attached as workflow artifacts.
* **Documentation**
  - Updated `README.md` for new starring features, tracker-data state handling, and full setup instructions.

### Changed

* State file handling is now more robust and incremental for stargazer reciprocity.
* Documentation improved for clarity regarding analytics and reciprocity workflows.

**Contributors:**
[@ikramagix](https://github.com/ikramagix)
[All commits →](https://github.com/ikramagix/GitGrowBot/commits/1.1.1)
---