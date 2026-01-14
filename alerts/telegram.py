import requests, os
from core.env import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_alert(jobs):
    if not jobs:
        return
    msg = "🔥 Job Digest (High Priority)\n\n"
    for j in jobs:
        msg += f"🏢 {j['company']}\n💼 {j['title']}\n🔗 {j['url']}\n⭐ Score: {j['score']}\n\n"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  json={"chat_id": CHAT_ID, "text": msg})
