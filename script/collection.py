import json


with open("temp/input/collections_data.json", "r", encoding="utf-8") as data_file:
    collections_data = json.load(data_file)

collections_state = {}

for collection in collections_data["collections"]:
    collection_id = collection["id"]
    items = []
    for item_info in collection["items"]:
        item_data = {
            "id": item_info["id"],
            "type": item_info["type"],
            "claimed": True,
            "lastUpdate": "0001-01-01T00:00:00Z",
            "points": item_info["points"],
        }
        items.append(item_data)

    collections_state[collection_id] = {
        "id": collection_id,
        "items": items,
        "upgradesState": [2],
    }


seasonal_collections_state = {}
seasonal_collections_data = collections_data.get("seasonalCollections", [])
for seasonal_collection in seasonal_collections_data:
    seasonal_collection_id = seasonal_collection["id"]
    seasonal_items = []
    for seasonal_item in seasonal_collection["items"]:
        seasonal_item_data = {
            "id": seasonal_item["id"],
            "type": seasonal_item["type"],
            "claimed": True,
            "lastUpdate": "0001-01-01T00:00:00Z",
            "points": seasonal_item["points"],
        }
        seasonal_items.append(seasonal_item_data)

    seasonal_collections_state[seasonal_collection_id] = {
        "id": seasonal_collection_id,
        "items": seasonal_items,
        "upgradesState": [2],
        "claimedPoints": 0,
    }


meterLevelClaimed = [
    {"Claimed": True, "IsAvailable": True}
    for _ in range(collections_data.get("meterTiers", 0))
]

full_collection_value = 0
for collection in collections_data.get("collections", []):
    for item_info in collection.get("items", []):
        full_collection_value += item_info.get("points", 0)

meterScore = collections_data.get("meterScore", 0)

collection_value = meterScore - full_collection_value

seasonal_collection_value = collection_value - 800


for collection in seasonal_collections_state.values():
    items = collection.get("items", [])
    if items:
        items[0]["points"] = seasonal_collection_value
        break  # Stop after modifying the first 'points' key


data = {
    "lastSaved": "0001-01-01T00:00:00Z",
    "patchVersion": 2,
    "collectionsState": collections_state,
    "seasonalCollectionsState": seasonal_collections_state,
    "meterLevelClaimed": meterLevelClaimed,
    "viewed": True,
    "meterViewed": True,
    "lastUpdate": "0001-01-01T00:00:00Z",
}

final_data = {"version": 1, "data": data}

with open("src/profile/collections.json", "w") as f:
    json.dump(final_data, f, indent=2)
