import os
import json
import glob

directory = "gamedata"

file_data = {}


def find_icon_and_shortcut(data, filename):
    if isinstance(data, dict):
        icon = data.get("icon")
        shortcut = data.get("shortcut")
        if icon:
            file_data[filename]["icon"].add(icon)
        if shortcut:
            file_data[filename]["shortcut"].add(shortcut)
        for value in data.values():
            find_icon_and_shortcut(value, filename)
    elif isinstance(data, list):
        for item in data:
            find_icon_and_shortcut(item, filename)


for file_path in glob.glob(os.path.join(directory, "*.json")):
    with open(file_path, "r", encoding="utf-8") as json_file:
        filename = os.path.basename(file_path)
        data = json.load(json_file)
        file_data[filename] = {"icon": set(), "shortcut": set()}
        find_icon_and_shortcut(data, filename)


result_data = [
    {
        filename: {
            "icon": list(data["icon"]) if data["icon"] else None,
            "shortcut": list(data["shortcut"]) if data["shortcut"] else None,
        }
    }
    for filename, data in file_data.items()
    if data["icon"] or data["shortcut"]
]

with open("icon_shortcut.json", "w") as output_file:
    json.dump(result_data, output_file, indent=2)
