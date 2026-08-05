# IT Change Intelligence

Weekly research digest on IT change management (ITIL/ITSM) and AI-related features across competitors.

**Live site:** https://aadeshbakliwal-commits.github.io/itsm-change-intelligence/

## Email setup (one-time)

Add these [repository secrets](https://github.com/aadeshbakliwal-commits/itsm-change-intelligence/settings/secrets/actions):

| Secret | Example (Gmail) | Description |
|--------|-----------------|-------------|
| `MAIL_SERVER` | `smtp.gmail.com` | SMTP server hostname |
| `MAIL_PORT` | `587` | SMTP port (587 for TLS) |
| `MAIL_USERNAME` | `you@gmail.com` | SMTP login |
| `MAIL_PASSWORD` | *(app password)* | Gmail App Password — not your regular password |
| `MAIL_FROM` | `aadesh.bakliwal@zendesk.com` | From address |
| `MAIL_TO` | `aadesh.bakliwal@zendesk.com` | Where digests are sent |

### Gmail App Password

1. Enable 2-Step Verification on your Google account
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Create an app password for "Mail"
4. Use that 16-character password as `MAIL_PASSWORD`

### Test the email

After secrets are set, go to **Actions → Email Weekly Digest → Run workflow** to send the latest report.

## How it works

| Trigger | What happens |
|---------|--------------|
| Push to `main` with changes in `weeks/` | Builds HTML email from the new report and sends it |
| Push to `main` (any change) | Redeploys GitHub Pages |
| Manual workflow dispatch | Sends digest for the most recent report |

## Structure

```
index.html              # Home page
css/style.css           # Shared styles
weeks/YYYY-MM-DD.html   # Weekly research reports
scripts/extract_digest.py
.github/workflows/
  deploy-pages.yml      # GitHub Pages
  email-digest.yml      # Email on new week
```

## Local preview

```bash
python3 -m http.server 8080
# http://localhost:8080
```

## Weekly schedule

Reports are published every **Sunday at 6:00 PM IST**. When a new file is added under `weeks/` and pushed, you receive an email with the executive summary and a link to the full report.
