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

major, minor, patch = map(int, version.split("."))
patch = (patch + 1) % 10
minor += patch == 0
minor %= 10
major += minor == 0 and patch == 0
major = min(major, 9)

appversion = get_version()

data.update({"version": f"{major}.{minor}.{patch}", "appversion": appversion})

with open(json_file, "w") as file:
    json.dump(data, file, indent=4)
    file.write("\n")


appversion = get_version()

data.update({"version": f"{major}.{minor}.{patch}", "appversion": appversion})

with open(json_file, "w") as file:
    json.dump(data, file, indent=4)
    file.write("\n")
