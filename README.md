# deployguard-target

> **Demo & test harness for [DeployGuard](https://github.com/Dan16ssd/Deploy-Guard-Ai-Agents-)** — a multi-agent AI system that reviews pull requests for security vulnerabilities and gates deployments.

This repository is **not** a real product. It is a deliberately minimal application that exists to **demonstrate DeployGuard catching a real vulnerability before it merges** — giving the agent chain something concrete and reproducible to review.

## The demo: a planted vulnerability

The vulnerability lives in a **pull request**, not in `main` — exactly how DeployGuard is meant to catch it *before* it ships:

- **`main`** holds clean, safe code — `app/auth.py` uses a **parameterized SQL query**.
- The **`feature/add-login`** branch (open as **PR #1**) introduces **deliberate SQL-injection** vulnerabilities: user input concatenated / format-strung straight into SQL in the new `get_user_for_request` and `login` methods.

When that PR is opened, GitHub notifies DeployGuard and its five agents review the change:

```
PR opened → webhook → ScanAgent → SecurityAgent → RiskAgent → DeployAgent → ReportAgent
```

**SecurityAgent** flags the SQL injection, posts a `CRITICAL` comment with the exact `file:line`, and the chain **blocks the deployment** instead of shipping vulnerable code. A clean PR (no findings) would instead flow through to a real `workflow_dispatch` deploy.

## What's in this repo

| Path | Purpose |
|------|---------|
| `app/auth.py` | A tiny user-auth service. On `main` it is **safe** (parameterized SQL). |
| `tests/test_auth.py` | A passing unit test for the safe version. |
| `.github/workflows/deploy.yml` | A `workflow_dispatch` deploy job DeployGuard triggers on an approved PR. |
| `requirements.txt` | Just `pytest`. |

## How it's wired

This repo has a GitHub **webhook** pointed at the DeployGuard service (hosted on Railway). On every pull request, GitHub delivers the event to DeployGuard, which opens a [Band](https://band.ai) chat room where the five agents collaborate to **approve or block** the change — posting their verdict back as a PR comment.

> Architecture, agents, tools, and setup live in the main project:
> **[github.com/Dan16ssd/Deploy-Guard-Ai-Agents-](https://github.com/Dan16ssd/Deploy-Guard-Ai-Agents-)**

## Run the (safe) app's tests

```bash
pip install -r requirements.txt
pytest -q
```

---

_Single-token demo today; multi-tenant review across arbitrary repos is the production path (via a GitHub App)._
