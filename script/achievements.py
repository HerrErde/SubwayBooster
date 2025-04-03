import json


with open("temp/input/achievements_data.json", "r", encoding="utf-8") as data_file:
    data = json.load(data_file)

achievements_list = {}


new_data = {
    "version": 2,
    "data": {
        "lastSaved": "1970-01-01T00:00:00Z",
        "patchVersion": 5,
        "achievementEntries": achievements_list,
    },
}


for achievement in data:
    achievements_id = achievement.get("id", "")
    tier_goals = achievement.get("tierGoals", [])
    progress = tier_goals[-1]
    

    achievements_list[achievements_id] = {
        "id": achievements_id,
        "progress": progress,
        "highestProgress": progress,
        "goals": tier_goals,
        "claimState": [True, True, True, True],
    }

with open("src/profile/achievements.json", "w", encoding="utf-8") as output_file:
    json.dump(new_data, output_file, indent=2)
