import csv
import os
import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "history.csv")

def log(job, alerted):
    # Ensure logs directory exists
    os.makedirs(LOG_DIR, exist_ok=True)

    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "company", "title", "url", "alerted"])

        writer.writerow([
            datetime.date.today().isoformat(),
            job["company"],
            job["title"],
            job["url"],
            alerted
        ])
