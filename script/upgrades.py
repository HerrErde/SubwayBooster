import json


modifier_mapping = {"RunMultiplier": 0, "RunAdder": 2}


subtype_mapping = {
    "Coin": 0,
    "ScoreMultiplier": 3,
    "SeasonToken": 2,
    "RaceBoardCharge": 101,
    "RaceLeagueTrophy": 102,
}

strategy_mapping = {"Run": 1, "Score": 2, "Time": 3}


def modifier_entry(
    mod, parent_id, duration, expiration_context=None, expiration_strategy=None
):
    entry = {
        "value": {
            "id": mod.get("id", parent_id),
            "type": modifier_mapping.get(mod.get("modifierType"), 0),
            "subType": subtype_mapping.get(mod.get("modifierSubType"), 0),
            "value": mod.get("value", 0),
        }
    }

    if duration != 0:
        entry["expirationValue"] = duration
        entry["expirationType"] = 2

    if expiration_strategy is not None:
        entry["contextType"] = strategy_mapping.get(expiration_strategy, 1)  #
    if expiration_context:
        entry["contextData"] = expiration_context

    return entry


def main():
    with open("temp/input/products_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    score_modifiers = {}
    currency_pickup_modifiers = {}

    for key, entry in data.get("modifiers", {}).items():
        mods = entry.get("modifiers", [])
        duration = entry.get("duration", 0)
        expiration_context = entry.get("expirationContext")
        expiration_strategy = entry.get("expirationStrategy")

        for mod in mods:
            entry_data = modifier_entry(
                mod, key, duration, expiration_context, expiration_strategy
            )
            sub_type = mod.get("modifierSubType", "")
            if sub_type == "ScoreMultiplier":
                score_modifiers[key] = entry_data
            else:
                currency_pickup_modifiers[key] = entry_data

    output_data = {
        "version": 3,
        "data": {
            "lastSaved": "1970-01-01T00:00:00Z",
            "patchVersion": 2,
            "scoreModifiers": score_modifiers,
            "currencyPickupModifiers": currency_pickup_modifiers,
            "powerupLevels": {
                "jetpack": 6,
                "superSneakers": 6,
                "magnet": 6,
                "doubleScore": 6,
            },
        },
    }

    with open("src/profile/upgrades.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)


if __name__ == "__main__":
    main()
