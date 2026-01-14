import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_company(c):
    r = requests.get(c["careers_url"], headers=HEADERS, timeout=15)
    s = BeautifulSoup(r.text, "html.parser")
    jobs = []
    for a in s.find_all("a", href=True):
        if any(k in a.text.lower() for k in c["keywords"]):
            jobs.append({
                "title": a.text.strip(),
                "company": c["name"],
                "location": "India",
                "url": a["href"],
                "source": "Company"
            })
    return jobs