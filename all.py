import subprocess
import requests
import os
import shutil
import time
import glob

delay = 3


def version():
    url = "https://gplayapi.herrerde.xyz/api/apps/com.kiloo.subwaysurf"
    response = requests.get(url)
    data = response.json()
    return data.get("version", "").replace(".", "-")


rm_dir = ["temp"]


scripts = [
    ["script/setup.py"],
    ["script/generate_characters.py"],
    ["script/generate_boards.py"],
    ["script/playerprofile.py"],
    ["script/userstats.py"],
    ["script/collection.py"],
    ["script/calender.py"],
    ["script/quests.py"],
    ["script/update.py"],
    ["script/convert.py"],
    ["script/zip.py"],
]


def cleanup():
    print(f"Starting cleanup")
    try:
        for directory in rm_dir:
            if os.path.exists(directory):
                shutil.rmtree(directory)
        print(f"Finished cleanup\n")
    except KeyboardInterrupt:
        print("Cleanup interrupted by user.")
        raise


def run_scripts():
    try:
        os.makedirs("temp", exist_ok=True)
        for script in scripts:
            print(f"Running {script[0]}...")
            subprocess.run(["python"] + script, check=True)
            print(f"Finished running {script[0]}.\n")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Script execution interrupted by user.")
        raise


def main():
    try:
        cleanup()
        run_scripts()
    except KeyboardInterrupt:
        print("Script terminated by user.")


if __name__ == "__main__":
    main()
