import json

with open("temp/input/boards_data.json") as f:
    data = json.load(f)

item_data_list = {}

for item in data:
    item_id = item["id"]
    item2s = item.get("upgrades", "none")

    item2_data = {}
    if item2s != "none" and item2s is not None:
        for item2 in item2s:
            item2_id = item2["id"]
            item2_data[item2_id] = {"value": True}

    list_data = {
        "value": {
            "id": item_id,
            "ownedUpgrades": {
                "default": {"value": True},
                **item2_data,
            },
        }
    }

    item_data_list[item_id] = list_data

inventory_data = {
    "version": 3,
    "data": {"selected": "default", "owned": item_data_list},
}

with open("src/profile/boards_inventory.json", "w", encoding="utf-8") as f:
    json.dump(inventory_data, f, indent=2, ensure_ascii=False)
