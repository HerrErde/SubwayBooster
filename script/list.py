import json


def generate(links_file, data_file, output_file):
    with open(links_file, "r") as links_json:
        links_data = json.load(links_json)

    with open(data_file, "r") as data_json:
        data = json.load(data_json)

    # remove "removed" items
    links_data = [link for link in links_data if not link.get("removed", False)]

    # markdown content
    content = "| Name | Id |\n| ---- | --- |\n"

    for link, character in zip(links_data, data):
        name = link.get("name")
        available = link.get("available")

        if available is True:
            data_id = f"``{character.get('id', 'None')}``"
        elif available is False:
            data_id = "None"
        else:
            continue

        if name and data_id:
            content += f"| {name} | {data_id} |\n"

    with open(output_file, "w") as md_file:
        md_file.write(content)


generate("temp/input/characters_links.json", "temp/input/characters_data.json", "docs/Characters.md")
generate("temp/input/boards_links.json", "temp/input/boards_data.json", "docs/Hoverboard.md")
