with open("changelog.txt", "r") as file:
    content = file.read()

strings = ["Characters", "Boards", "Outfits"]
output = []

if any(string in content for string in strings or strings2):
    if "Character" in content:
        output.append("characters")
    if "Board" in content:
        output.append("boards")
    if "Outfit" in content:
        output.append("outfits")

print(", ".join(output))
