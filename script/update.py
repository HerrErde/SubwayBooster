import json
import requests

gplayapi_url = "https://gplayapi.cashlessconsumer.in/api/apps/com.kiloo.subwaysurf"
json_file = "src/version.json"
season_hunt_file = "src/profile/season_hunt.json"
collections_file = "collections_data.json"


def get_version():
    response = requests.get(gplayapi_url)
    response.raise_for_status()
    return response.json()["version"]


def update_season():
    with open(collections_file, "r") as file:
        data = json.load(file)
        time_slot = data.get("timeSlot", "")
        return int(time_slot.split("_S")[1])


def update_season_hunt(season):
    with open(season_hunt_file, "r+") as file:
        season_hunt_data = json.load(file)
        season_hunt_data["data"]["currentTimeSlotId"] = f"season_S{season}"
        file.seek(0)
        json.dump(season_hunt_data, file, indent=2)


def update_version(data, season):
    version = data["version"]
    major, minor, patch = map(int, version.split("."))

    patch = (patch + 1) % 10
    minor += int(patch == 0)
    minor %= 10
    major += int(minor == 0 and patch == 0)
    major = min(major, 9)

    app_version = get_version()

    data.update(
        {
            "version": f"{major}.{minor}.{patch}",
            "appversion": app_version,
            "season": str(season),
        }
    )

    return data


def main():
    with open(json_file, "r+") as file:
        data = json.load(file)
        season = update_season()

        updated_data = update_version(data, season)

        file.seek(0)
        update_season_hunt(season)
        json.dump(updated_data, file, indent=2)
        file.truncate()
        file.write("\n")


main()
