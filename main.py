from core.env import load_dotenv
load_dotenv()

import yaml
from scrapers.indeed import scrape_indeed
from scrapers.company_scraper import scrape_company
from core.deduplicator import job_hash
from core.state import load_state, save_state
from core.filters import keyword_match
from alerts.telegram import send_alert

seen = load_state()
new = []

roles = yaml.safe_load(open("config/roles.yml"))["roles"]
skills = yaml.safe_load(open("config/skills.yml"))["skills"]
companies = yaml.safe_load(open("config/companies.yml"))["companies"]

for r in roles:
    for j in scrape_indeed(r, "Delhi NCR"):
        h = job_hash(j)
        if h not in seen and keyword_match(j["title"], skills):
            seen.add(h)
            new.append(j)

for c in companies:
    for j in scrape_company(c):
        h = job_hash(j)
        if h not in seen:
            seen.add(h)
            new.append(j)

save_state(seen)
send_alert(new)