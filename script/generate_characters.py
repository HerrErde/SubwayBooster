import json

# Read the input file
with open("temp/input/characters_data.json") as f:
    data = json.load(f)

# Process the data
item_data_list = {}

for item in data:
    item_id = item["id"]
    item2s = item.get("outfits", "none")

    item2_data = []
    if item2s != "none":
        for item2 in item2s:
            item2_id = item2["id"]
            item2_data.append({"value": item2_id})

    item_data_list[item_id] = {"value": {"id": item_id, "ownedOutfits": item2_data}}

# Generate the output
inventory_data = {
    "version": 3,
    "data": {
        "selected": {"character": "jake", "outfit": "default"},
        "owned": item_data_list,
    },
}

# Write the output file
with open("src/profile/characters_inventory.json", "w", encoding="utf-8") as f:
    json.dump(inventory_data, f, indent=2, ensure_ascii=False)
