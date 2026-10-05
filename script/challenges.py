import json

kind_mapping = {"Daily": 1, "CoinMeter": 2, "City": 4}


def challenge():
    with open("temp/input/challenges_data.json", "r") as data_file:
        data = json.load(data_file)
        eliteChallenges_data = data.get("eliteChallenges")

    challengeStates = {}

    for challenge_id, challenge in data.get("challenges", {}).items():
        rewardTiers = challenge.get("rewardTiers")
        if not rewardTiers:
            print(f"Skipping {challenge_id}: no reward tiers")
            continue

        rewardStates = []

        for rewardTier in rewardTiers:
            requiredScore = rewardTier["requiredScore"]

            rewardList = []

            # Iterate through each reward in the current reward tier
            for reward in rewardTier["rewards"]:
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

            reward_state = {
                "State": 10,
                "RequiredScore": requiredScore,
                "OriginalRequiredScore": requiredScore,
                "Rewards": rewardList,
            }

            if rewardTier.get("groupId"):
                reward_state["GroupId"] = rewardTier["groupId"]

            rewardStates.append(reward_state)

        requirements = {"access": challenge.get("accessRequirement", {})}
        if challenge.get("visibilityRequirement"):
            requirements["visibility"] = challenge.get("visibilityRequirement", {})
        if challenge.get("participationRequirement", {}).get("data"):
            requirements["participation"] = challenge.get("participationRequirement", {})

        challenge_state = {
            "challengeId": challenge_id,
            "challengeType": challenge.get("headerTitleKey", ""),
            "challengeServerId": challenge.get("serverId", ""),
            "currentSetEntryID": challenge.get("currentSetEntryID", ""),
            "currentSetEntryTimeSlot": challenge.get("currentSetEntryTimeSlot", ""),
            "currentScore": 2147483647,
            "highScore": 2147483647,
            "lastSeenScore": 2147483647,
            "startDate": "1970-01-01T00:00:00Z",
            # "startDate": f"{startdate}:00Z",
            "endDate": "9999-12-31T00:00:00Z",
            # "endDate": f"{enddate}:00Z",
            "sunsetPeriodInSeconds": challenge.get("sunsetPeriod", 0),
            # "multiplierOnStart": 39,
            "rewardStates": rewardStates,
            "rewardUnlockOffset": challenge.get("rewardUnlockOffset", []),
            # "requirementsMultiplier": 1,
            # "roundingValue": 1,
            # "successParameter": 6,
            "successBehaviour": 1,
            "matchmakingId": challenge.get("matchmakingId", ""),
            "endAccess": -1,
            "requirements": requirements,
            "kind": kind_mapping.get(challenge.get("kind")),
            "targetCity": challenge.get("targetCity", ""),
            "markAsSeen": True,
            "accessed": True,
            "lastInteractionTime": "2025-09-05T01:00:00Z",
            # "lastInteractionTime": "1970-01-01T00:00:00Z",
            "gameMode": challenge.get("gameMode", ""),
            # "createdInMinorVersion": 52,
            # "winStreak": 0,
            # "EventState": 0,
        }

        if challenge.get("skipStageCost"):
            challenge_state["skipStageCost"] = challenge["skipStageCost"]

        if challenge_id == "dailyChallenge":

            challenge_state["default"] = True

            # Stays here for now, might be needed later
            """
            elite = eliteChallenges_data.get("daily_challenge_elite_tiers", {})
            challenge_state["eliteChallenge"] = {
                "id": elite.get("id"),
                "reviveHint": elite.get("reviveHint"),
                "rewardTiers": elite.get("tiers"),
                "unlockingValue": elite.get("unlockingValue", 1000000),
                "milestoneDisplayData": elite.get("milestone"),
            }
            """

        challengeStates[challenge_id] = challenge_state

    output_data = {
        "version": 1,
        "data": {
            "lastSaved": "1970-01-01T00:00:00Z",
            "patchVersion": 2,
            "challengeStates": challengeStates,
        },
    }

    with open("src/profile/generic_challenges.json", "w") as f:
        json.dump(output_data, f, indent=2)


challenge()