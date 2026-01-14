def score_job(job, skills):
    score = 0
    title = job['title'].lower()
    for s in skills:
        if s in title:
            score += 1
    if 'ai' in title or 'ml' in title:
        score += 2
    if 'remote' in title:
        score += 1
    return score
