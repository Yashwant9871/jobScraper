import hashlib

def normalize(text):
    return text.lower().replace('senior','').replace('jr','').strip()

def job_hash(j):
    base = f"{normalize(j['title'])}{j['company']}{j['url']}"
    return hashlib.md5(base.encode()).hexdigest()
