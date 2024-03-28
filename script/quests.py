import json

quests_file = "src/profile/quests.json"
collections_file = "collections_data.json"


def update_quests(season):
    with open(quests_file, "r+") as file:
        quests_data = json.load(file)
        quests_data["data"]["timeSlot"] = season
        for quest_type in ["daily", "seasonal"]:
            quests_data["data"]["questStates"][quest_type]["globalTimeslotId"] = season
        file.seek(0)
        file.truncate()
        json.dump(quests_data, file, indent=2)


with open(collections_file) as f:
    season = json.load(f).get("timeSlot", "")

update_quests(season)
