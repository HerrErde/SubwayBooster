import json
import requests

json_file = "Android/data/com.kiloo.subwaysurf/files/version.json"


def get_version():
    gplayapi_response = requests.get(
        "https://gplayapi.srik.me/api/apps/com.kiloo.subwaysurf"
    )
    gplayapi_data = gplayapi_response.json()
    gplayapi_version = gplayapi_data["version"]

    return gplayapi_version


with open(json_file, "r") as file:
    data = json.load(file)
    version = data["version"]
    season = int(data.get("season", 0))  # Convert to integer

major, minor, patch = map(int, version.split("."))
patch = (patch + 1) % 10
minor += int(patch == 0)
minor %= 10
major += int(minor == 0 and patch == 0)
major = min(major, 9)
season += 1

appversion = get_version()

data.update(
    {
        "version": f"{major}.{minor}.{patch}",
        "appversion": appversion,
        "season": str(season),
    }
)

with open(json_file, "w") as file:
    json.dump(data, file, indent=4)
    file.write("\n")
