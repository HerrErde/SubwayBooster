import json


def process_collection(collections):
    state = {}
    for collection in collections:
        state[collection["id"]] = {
            "id": collection["id"],
            "items": [
                {
                    "id": item["id"],
                    "type": item["type"],
                    "claimed": True,
                    "lastUpdate": "0001-01-01T00:00:00Z",
                    "points": item["points"],
                }
                for item in collection["items"]
            ],
            "upgradesState": [2],
        }
    return state


def adjust_seasonal_collection(collections_data, seasonal_collections_state):
    full_collection_value = sum(
        item["points"]
        for collection in collections_data.get("collections", [])
        for item in collection.get("items", [])
    )
    seasonal_collection_value = (
        collections_data.get("meterScore", 0) - full_collection_value - 800
    )

    for collection in seasonal_collections_state.values():
        if collection["items"]:
            collection["items"][0]["points"] = seasonal_collection_value
            break  # Modify only the first applicable item

    return seasonal_collections_state


def save_collection_data(
    collections_state, seasonal_collections_state, meter_level_claimed
):
    data = {
        "lastSaved": "0001-01-01T00:00:00Z",
        "patchVersion": 2,
        "collectionsState": collections_state,
        "seasonalCollectionsState": seasonal_collections_state,
        "meterLevelClaimed": meter_level_claimed,
        "viewed": True,
        "meterViewed": True,
        "lastUpdate": "0001-01-01T00:00:00Z",
    }

    with open("src/profile/collections.json", "w", encoding="utf-8") as f:
        json.dump({"version": 1, "data": data}, f, indent=2)


if __name__ == "__main__":
    with open("temp/input/collections_data.json", "r", encoding="utf-8") as data_file:
        collections_data = json.load(data_file)

    collections_state = process_collection(collections_data.get("collections", []))
    seasonal_collections_state = process_collection(
        collections_data.get("seasonalCollections", [])
    )
    seasonal_collections_state = adjust_seasonal_collection(
        collections_data, seasonal_collections_state
    )

    meter_level_claimed = [
        {"Claimed": True, "IsAvailable": True}
        for _ in range(collections_data.get("meterTiers", 0))
    ]

    save_collection_data(
        collections_state, seasonal_collections_state, meter_level_claimed
    )
