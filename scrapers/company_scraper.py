import requests
import random
import time
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_company(c):
    jobs = []

    try:
        # polite delay
        time.sleep(random.uniform(3, 7))

        r = requests.get(
            c["careers_url"],
            headers=HEADERS,
            timeout=20
        )
        r.raise_for_status()

    except RequestException as e:
        # log and skip this company
        print(f"[WARN] Skipping {c['name']} → {e}")
        return jobs  # empty list, NOT crash

    soup = BeautifulSoup(r.text, "html.parser")

    for a in soup.find_all("a", href=True):
        text = a.text.lower().strip()
        if any(k in text for k in c["keywords"]):
            jobs.append({
                "title": a.text.strip(),
                "company": c["name"],
                "location": "India",
                "url": a["href"],
                "source": "Company"
            })

    return jobs
