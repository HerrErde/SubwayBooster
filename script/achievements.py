import json


with open("temp/input/achievements_data.json", "r", encoding="utf-8") as data_file:
    data = json.load(data_file)

achievements_list = {}


new_data = {
    "version": 3,
    "data": {
        "lastSaved": "0001-01-01T00:00:00Z",
        "patchVersion": 5,
        "achievementEntries": achievements_list,
    },
}


for achievement in data:
    achievements_id = achievement.get("id", "")
    tier_goals = achievement.get("tierGoals", [])

    achievements_list[achievements_id] = {
        "id": achievements_id,
        "goals": tier_goals,
        "currentTier": 4,
        "highestProgress": 0,
        "claimState": [True, True, True, True],
    }

with open("src/profile/achievements.json", "w", encoding="utf-8") as output_file:
    json.dump(new_data, output_file, indent=2)
