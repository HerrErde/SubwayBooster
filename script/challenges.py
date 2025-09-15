import json

kind_mapping = {"Daily": 1, "Meter": 2, "City": 4}


def challenge():
    with open("temp/input/challenges_data.json", "r") as data_file:
        data = json.load(data_file)
        challenge_data = data.get("challenges")
        eliteChallenges_data = data.get("eliteChallenges")

    challengeStates = {}

    for challenge_id, challenge in challenge_data.items():

        rewardStates = []

        rewardTiers = challenge["rewardTiers"]
        for rewardTier in rewardTiers:
            requiredScore = rewardTier["requiredScore"]
            rewards = rewardTier["rewards"]
            groupId = rewardTier.get("groupId", None)

            rewardList = []

            # Iterate through each reward in the current reward tier
            for reward in rewards:
                if "reward" in reward:
                    reward["reward"]["claimed"] = True

                    """
                    # if EventCoins, force timeslot
                    if reward["reward"].get("id") == "EventCoins":
                        reward["timeslot"] = "season_S107"
                    """

                if "fallbackReward" in reward:
                    reward["fallbackReward"]["claimed"] = True

                rewardList.append(reward)

            state = {}

            if groupId:
                state["GroupId"] = groupId

            state.update(
                {
                    "State": 10,
                    "RequiredScore": requiredScore,
                    "OriginalRequiredScore": requiredScore,
                    "Rewards": rewardList,
                }
            )

            rewardStates.append(state)

            part_req = challenge.get("participationRequirement", {})

            requirements = {
                "access": challenge.get("accessRequirement", {}),
            }
            if challenge.get("visibilityRequirement"):
                requirements["visibility"] = challenge.get("visibilityRequirement", {})

            if isinstance(part_req, dict) and part_req.get("data"):

                requirements["participation"] = part_req

        challengeStates[challenge_id] = {
            "challengeId": challenge_id,
            "challengeType": challenge["headerTitleKey"],
            "challengeServerId": challenge["serverId"],
            "currentSetEntryID": challenge["currentSetEntryID"],
            "currentSetEntryTimeSlot": challenge["currentSetEntryTimeSlot"],
            "currentScore": 2147483647,
            "highScore": 2147483647,
            "lastSeenScore": 2147483647,
            "startDate": "1970-01-01T00:00:00Z",
            # "startDate": f"{startdate}:00Z",
            "endDate": "9999-12-31T00:00:00Z",
            # "endDate": f"{enddate}:00Z",
            "sunsetPeriodInSeconds": challenge["sunsetPeriod"],
            # "multiplierOnStart": 39,
            "rewardStates": rewardStates,
            "rewardUnlockOffset": challenge["rewardUnlockOffset"],
            # "requirementsMultiplier": 1,
            # "roundingValue": 1,
            # "successParameter": 6,
            "successBehaviour": 1,
            "matchmakingId": challenge["matchmakingId"],
            "endAccess": -1,
            "requirements": requirements,
            "kind": kind_mapping.get(challenge["kind"]),
            "targetCity": challenge["targetCity"],
            "markAsSeen": True,
            "accessed": True,
            "lastInteractionTime": "2025-09-05T01:00:00Z",
            # "lastInteractionTime": "1970-01-01T00:00:00Z",
            "gameMode": challenge["gameMode"],
            # "createdInMinorVersion": 52,
            # "winStreak": 0,
            # "EventState": 0,
        }

        if challenge["skipStageCost"]:
            state["skipStageCost"] = challenge["skipStageCost"]

        if challenge_id == "dailyChallenge":

            challengeStates[challenge_id]["default"] = True

            # Stays here for now, might be needed later
            """
            elite = eliteChallenges_data.get("daily_challenge_elite_tiers", {})
            challengeStates[challenge_id]["eliteChallenge"] = {
                "id": elite.get("id"),
                "reviveHint": elite.get("reviveHint"),
                "rewardTiers": elite.get("tiers"),
                "unlockingValue": elite.get("unlockingValue", 1000000),
                "milestoneDisplayData": elite.get("milestone"),
            }
            """

    data = {
        "lastSaved": "1970-01-01T00:00:00Z",
        "patchVersion": 2,
        "challengeStates": challengeStates,
    }

    output_data = {"version": 1, "data": data}

    with open("src/profile/generic_challenges.json", "w") as f:
        json.dump(output_data, f, indent=2)


challenge()
