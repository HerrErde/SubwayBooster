import json
import requests

gplayapi_url = "https://gplayapi.srik.me/api/apps/com.kiloo.subwaysurf"
json_file = "Android/data/com.kiloo.subwaysurf/files/version.json"
version_file_path = "Android/data/com.kiloo.subwaysurf/files/profile/season_hunt.json"


def get_version():
    return requests.get(gplayapi_url).json()["version"]


def update_season(data, old_season, new_season):
    return json.loads(
        json.dumps(data).replace(f"season_S{old_season}", f"season_S{new_season}")
    )


def update_version():
    with open(json_file, "r+") as file:
        data = json.load(file)

        old_season = int(data.get("season", 0))
        version = data["version"]
        major, minor, patch = map(int, version.split("."))

        patch = (patch + 1) % 10
        minor += int(patch == 0)
        minor %= 10
        major += int(minor == 0 and patch == 0)
        major = min(major, 9)

        season = old_season + 1

        app_version = get_version()

        data.update(
            {
                "version": f"{major}.{minor}.{patch}",
                "appversion": app_version,
                "season": str(season)
            }
        )

        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()
        file.write("\n")

        with open(version_file_path, "r+") as version_file:
            version_data = json.load(version_file)
            new_version_data = update_season(version_data, old_season, season)
            version_file.seek(0)
            json.dump(new_version_data, version_file, indent=2)
            version_file.truncate()
            version_file.write("\n")


update_version()
