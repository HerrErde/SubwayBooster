import json
import re

quests_file = "src/profile/quests.json"
challenges_file = "temp/upload/challenges_data.json"


def get_latest_season():
    with open(challenges_file, "r", encoding="utf-8") as file:
        text = file.read()
    seasons = [int(n) for n in re.findall(r"season_S(\d+)", text)]
    if not seasons:
        raise ValueError(f"No season timeslots found in {challenges_file}")
    return f"season_S{max(seasons)}"


def update_quests(season):
    with open(quests_file, "r+") as file:
        quests_data = json.load(file)
        quests_data["data"]["timeSlot"] = season
        for quest_type in ["daily", "seasonal"]:
            quests_data["data"]["questStates"][quest_type]["globalTimeslotId"] = season
        file.seek(0)
        file.truncate()
        json.dump(quests_data, file, indent=2)


update_quests(get_latest_season())
