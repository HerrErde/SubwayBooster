import json

# Read data from collections_data.json
with open("collections_data.json", "r") as data_file:
    collections_data = json.load(data_file)

# Create a dictionary to store the transformed data
collections_state = {}

# Transform the data from collections_data.json
for collection in collections_data["collections"]:
    collection_id = collection["id"]
    items = []
    for item_id, item_info in collection["items"].items():
        item_data = {
            "id": item_id,
            "type": item_info["type"],
            "claimed": True,
            "lastUpdate": "0001-01-01T00:00:00Z",
        }
        items.append(item_data)

    collections_state[collection_id] = {
        "id": collection_id,
        "items": items,
        "upgradesState": [2],
        "claimedPoints": None,
    }

# Add seasonalCollections data
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
        }
        seasonal_items.append(seasonal_item_data)

    seasonal_collections_state[seasonal_collection_id] = {
        "id": seasonal_collection_id,
        "items": seasonal_items,
        "upgradesState": [2],
        "claimedPoints": 0,
    }

# Create the final JSON structure
data = {
    "lastSaved": "0001-01-01T00:00:00Z",
    "collectionsState": collections_state,
    "seasonalCollectionsState": seasonal_collections_state,
    "meterLevelClaimed": [
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
        {"Claimed": True, "IsAvailable": True},
    ],
    "viewed": True,
    "meterViewed": True,
    "lastUpdate": "0001-01-01T00:00:00Z",
}

final_data = {"version": 1, "data": data}

# Write the transformed data to collections.json
with open("src/profile/collections.json", "w") as f:
    json.dump(final_data, f, indent=2)
