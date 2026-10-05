import json

output_file = "src/profile/quests.json"
quests_file = "temp/gamedata/quests.json"


def update_quests(season):
    with open(output_file, "r+") as file:
        quests_data = json.load(file)
        quests_data["data"]["timeSlot"] = season
        for quest_type in ["daily", "seasonal"]:
            quests_data["data"]["questStates"][quest_type]["globalTimeslotId"] = season
        file.seek(0)
        file.truncate()
        json.dump(quests_data, file, indent=2)


with open(quests_file) as f:
    season = json.load(f).get("global", {}).get("timeSlot", "")

update_quests(season)
