import json


# Read the input file
with open("characters_data.json") as f:
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
            item2_data.append('{"value":"' + item2_id + '"}')

    item2_list = ",".join(item2_data)
    list_data = (
        f'"{item_id}":{{"value":{{"id":"{item_id}","ownedOutfits":[{item2_list}]}}}}'
    )

    item_data_list[item_id] = list_data

# Generate the output
inventory_data = ",".join(item_data_list.values())

output_data = {
    "version": 3,
    "data": '{"selected":{"character":"Jake","outfit":"default"},"owned":{'
    + inventory_data
    + "}}",
}

# Write the output file
with open("characters_inventory.json", "w") as f:
    json.dump(output_data, f, indent=2)
