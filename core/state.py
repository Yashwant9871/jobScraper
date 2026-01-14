import json, os, time
STATE_FILE = "state.json"

def load_state():
    if not os.path.exists(STATE_FILE):
        return {}
    return json.load(open(STATE_FILE))

def save_state(s):
    json.dump(s, open(STATE_FILE, "w"))
