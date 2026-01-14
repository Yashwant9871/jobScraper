import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_indeed(q, l):
    r = requests.get(f"https://in.indeed.com/jobs?q={q}&l={l}", headers=HEADERS, timeout=15)
    s = BeautifulSoup(r.text, "html.parser")
    jobs = []
    for c in s.select(".job_seen_beacon"):
        t = c.select_one("h2 span")
        co = c.select_one(".companyName")
        a = c.select_one("a")
        if t and co and a:
            jobs.append({
                "title": t.text.strip(),
                "company": co.text.strip(),
                "location": l,
                "url": "https://in.indeed.com" + a["href"],
                "source": "Indeed"
            })
    return jobs