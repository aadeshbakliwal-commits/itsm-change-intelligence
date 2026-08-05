# Email setup for aadesh.bakliwal@zendesk.com

Add these secrets at:
https://github.com/aadeshbakliwal-commits/itsm-change-intelligence/settings/secrets/actions

## Required secrets

| Secret | Your value |
|--------|------------|
| `MAIL_TO` | `aadesh.bakliwal@zendesk.com` |
| `MAIL_FROM` | `aadesh.bakliwal@zendesk.com` |
| `MAIL_USERNAME` | `aadesh.bakliwal@zendesk.com` |
| `MAIL_PASSWORD` | *(see below — you must create this)* |
| `MAIL_SERVER` | *(see below)* |
| `MAIL_PORT` | `587` |

## SMTP server (Zendesk / Google Workspace)

If your Zendesk email is on **Google Workspace** (most common):

| Secret | Value |
|--------|-------|
| `MAIL_SERVER` | `smtp.gmail.com` |
| `MAIL_PORT` | `587` |
| `MAIL_PASSWORD` | Google App Password — [create one here](https://myaccount.google.com/apppasswords) |

Steps:
1. Enable 2-Step Verification on your Google/Zendesk account
2. Create an App Password named "GitHub Actions IT Change Intel"
3. Paste the 16-character password as `MAIL_PASSWORD` in GitHub secrets

If your org uses **Microsoft 365** instead:

| Secret | Value |
|--------|-------|
| `MAIL_SERVER` | `smtp.office365.com` |
| `MAIL_PORT` | `587` |
| `MAIL_PASSWORD` | Your work password or app password (check with IT if SMTP is allowed) |

## After secrets are set

1. Push code (if not done): `git push -u origin main`
2. Enable Pages: repo Settings → Pages → Source: **GitHub Actions**
3. Test email: Actions → **Email Weekly Digest** → Run workflow

You will receive digests at **aadesh.bakliwal@zendesk.com** whenever a new file is added under `weeks/` and pushed.
