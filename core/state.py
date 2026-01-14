import json, os
STATE_FILE = "state.json"

def load_state():
    if not os.path.exists(STATE_FILE):
        return set()
    return set(json.load(open(STATE_FILE)))

def save_state(s):
    json.dump(list(s), open(STATE_FILE, "w"))