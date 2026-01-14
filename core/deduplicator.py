import hashlib
def job_hash(j): return hashlib.md5(f"{j['title']}{j['company']}{j['location']}".encode()).hexdigest()
