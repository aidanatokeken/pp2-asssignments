import json
import os

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {"sound": True, "difficulty": "normal"}
    with open(SETTINGS_FILE) as f:
        return json.load(f)

def save_score(name, coins, distance):
    data = []

    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE) as f:
            data = json.load(f)

    data.append({
        "name": name,
        "coins": coins,
        "distance": distance,
        "score": coins + distance
    })

    # топ 10
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)