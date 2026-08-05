#!/usr/bin/env python3
"""Extract email subject and HTML body from a weekly report."""

import html
import os
import re
import sys
from pathlib import Path

REPO = "aadeshbakliwal-commits/itsm-change-intelligence"
PAGES_BASE = f"https://{REPO.split('/')[0]}.github.io/{REPO.split('/')[1]}"


def extract_section(content: str, section_id: str) -> str:
    pattern = rf'<section id="{section_id}">(.*?)</section>'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return ""

    section = match.group(1)
    section = re.sub(r"<h2[^>]*>.*?</h2>", "", section, count=1, flags=re.DOTALL)
    paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", section, re.DOTALL)
    text_parts = []
    for p in paragraphs[:3]:
        p = re.sub(r"<[^>]+>", "", p)
        p = html.unescape(p.strip())
        if p:
            text_parts.append(p)
    return " ".join(text_parts)


def extract_takeaways(content: str, limit: int = 5) -> list[str]:
    pattern = r'<section id="takeaways">(.*?)</section>'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return []

    items = re.findall(r"<li>(.*?)</li>", match.group(1), re.DOTALL)
    results = []
    for item in items[:limit]:
        item = re.sub(r"<[^>]+>", "", item)
        item = html.unescape(item.strip())
        if item:
            results.append(item)
    return results


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: extract_digest.py <week-report.html>", file=sys.stderr)
        sys.exit(1)

    report_path = Path(sys.argv[1])
    content = report_path.read_text(encoding="utf-8")

    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.DOTALL)
    week_title = (
        html.unescape(re.sub(r"<[^>]+>", "", title_match.group(1)).strip())
        if title_match
        else report_path.stem
    )

    summary = extract_section(content, "summary")
    takeaways = extract_takeaways(content)

    report_url = f"{PAGES_BASE}/weeks/{report_path.name}"
    home_url = f"{PAGES_BASE}/"

    subject = f"IT Change Intelligence — {week_title}"

    takeaway_html = ""
    if takeaways:
        items = "".join(
            f"<li style='margin-bottom:8px;'>{html.escape(t)}</li>" for t in takeaways
        )
        takeaway_html = f"""
        <h3 style="color:#e8edf4;margin:24px 0 12px;">Key Takeaways</h3>
        <ul style="color:#8b9cb3;padding-left:20px;">{items}</ul>
        """

    body = f"""<!DOCTYPE html>
<html>
<body style="font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0f1419;color:#e8edf4;padding:24px;max-width:640px;margin:0 auto;">
  <div style="background:#1a2332;border:1px solid #2d3a4f;border-radius:10px;padding:24px;">
    <p style="color:#3b82f6;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;margin:0 0 8px;">IT Change Intelligence</p>
    <h1 style="font-size:22px;margin:0 0 16px;color:#e8edf4;">{html.escape(week_title)}</h1>
    <p style="color:#8b9cb3;line-height:1.6;margin:0 0 20px;">{html.escape(summary[:600])}{'…' if len(summary) > 600 else ''}</p>
    {takeaway_html}
    <p style="margin:28px 0 0;">
      <a href="{report_url}" style="display:inline-block;background:#3b82f6;color:#fff;text-decoration:none;padding:12px 20px;border-radius:8px;font-weight:600;">Read full report</a>
      &nbsp;
      <a href="{home_url}" style="color:#3b82f6;text-decoration:none;">All reports</a>
    </p>
    <p style="color:#8b9cb3;font-size:12px;margin-top:24px;border-top:1px solid #2d3a4f;padding-top:16px;">
      Automated digest from your IT Change Intelligence site. Updated every Sunday at 6 PM IST.
    </p>
  </div>
</body>
</html>"""

    Path("email-body.html").write_text(body, encoding="utf-8")

    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"subject={subject}\n")

    print(f"Subject: {subject}")
    print(f"Report URL: {report_url}")


if __name__ == "__main__":
    main()
