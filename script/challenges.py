import json
from datetime import datetime, timedelta, timezone

kind_mapping = {"Daily": 1, "Meter": 2, "City": 4}


def gen_enddate():
    future_date = datetime.now(timezone.utc) + timedelta(weeks=4)
    formatted_date = future_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    return formatted_date


def challenge():
    with open("temp/input/challenges_data.json", "r") as data_file:
        challenge_data = json.load(data_file)

    enddate = gen_enddate()

    challengeStates = {}

    for challenge_id, challenge in challenge_data.items():

        rewardStates = []

        rewardTiers = challenge["rewardTiers"]
        for rewardTier in rewardTiers:
            requiredScore = rewardTier["requiredScore"]
            rewards = rewardTier["rewards"]
            rewards = rewardTier["rewards"]

            rewardList = []

            # Iterate through each reward in the current reward tier
            for reward in rewards:
                if "reward" in reward:
                    reward["reward"]["claimed"] = True
                if "fallbackReward" in reward:
                    reward["fallbackReward"]["claimed"] = True

                rewardList.append(reward)

            state = {
                "State": 10,
                "RequiredScore": requiredScore,
                "OriginalRequiredScore": requiredScore,
                "Rewards": rewardList,
            }

            rewardStates.append(state)

            part_req = challenge.get("participationRequirement", {})

            # Check if 'participationRequirement' is a dictionary and if it has a 'data' key
            if isinstance(part_req, dict):
                part_data = part_req.get("data", [])[0]
                operator = part_req.get("operator")
                part_data_meta = part_data.get("meta", [])

                participation = {
                    "type": part_data.get("type"),
                    "operator": part_data.get("operator"),
                    "value": part_data.get("value"),
                    "meta": part_data_meta,
                }

            partreq = {
                "data": [participation],
                "operator": operator,
            }

            requirements = {
                "access": challenge["accessRequirement"],
                "participation": partreq,
            }

        challengeStates[challenge_id] = {
            "challengeId": challenge_id,
            "challengeType": challenge["headerTitleKey"],
            "challengeServerId": challenge["serverId"],
            "currentSetEntryID": challenge_id,
            "currentSetEntryTimeSlot": f"season_{challenge_id}",
            "currentScore": 2147483647,
            "highScore": 2147483647,
            "startDate": "0001-01-01T00:00:00Z",
            # "endDate": "9999-12-31T00:00:00Z",
            "endDate": enddate,
            # "sunsetPeriodInSeconds": 604800,
            # "multiplierOnStart": 1,
            "rewardStates": rewardStates,
            "rewardUnlockOffset": challenge["rewardUnlockOffset"],
            "matchmakingId": challenge["matchmakingId"],
            "requirements": requirements,
            "kind": kind_mapping.get(challenge["kind"]),
            "targetCity": challenge["targetCity"],
            "markAsSeen": True,
            "gameMode": challenge["gameMode"],
        }

    data = {
        "lastSaved": "0001-01-01T00:00:00Z",
        "patchVersion": 1,
        "challengeStates": challengeStates,
    }

    output_data = {"version": 1, "data": data}

    with open("src/profile/generic_challenges.json", "w") as f:
        json.dump(output_data, f, indent=2)


challenge()
