from core.env import load_dotenv
load_dotenv()

import yaml, random
from scrapers.company_scraper import scrape_company
from core.state import load_state, save_state
from core.deduplicator import job_hash
from core.scoring import score_job
from core.logger import log
from alerts.telegram import send_alert

settings = yaml.safe_load(open("config/settings.yml"))
skills = yaml.safe_load(open("config/skills.yml"))["skills"]
companies = yaml.safe_load(open("config/companies.yml"))["companies"]

state = load_state()
alerts = []

random.shuffle(companies)

for c in companies:
    jobs = scrape_company(c)
    for j in jobs:
        h = job_hash(j)
        if h in state:
            continue
        score = score_job(j, skills)
        j["score"] = score
        state[h] = True
        if score >= settings["min_score"]:
            alerts.append(j)
            log(j, True)
        else:
            log(j, False)

alerts = sorted(alerts, key=lambda x: x["score"], reverse=True)
alerts = alerts[:settings["alert_limit"]]

save_state(state)
send_alert(alerts)
