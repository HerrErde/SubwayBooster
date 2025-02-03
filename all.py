import argparse
import os
import re
import shutil
import subprocess
import sys
import time

import requests

delay = 3


def version():
    url = "https://api.github.com/repos/HerrErde/subway-source/releases/latest"
    response = requests.get(url)
    data = response.json()
    return data.get("tag_name", "")


def get_rm(nodownload):
    rm_dir = ["temp/input"]

    if not nodownload:
        tmp_dir = "temp/data"
        rm_dir.insert(0, tmp_dir)

    return rm_dir


def setup():
    os.makedirs("temp", exist_ok=True)
    os.makedirs("temp/data", exist_ok=True)
    os.makedirs("temp/input", exist_ok=True)


def get_scripts(version, onlydownload, nodownload):

    if onlydownload:
        return [
            [
                f"script/setup.py",
                version,
            ]
        ]

    script_list = [
        ["script/generate_characters.py"],
        ["script/generate_boards.py"],
        ["script/playerprofile.py"],
        ["script/userstats.py"],
        ["script/collection.py"],
        ["script/challenges.py"],
        ["script/calender.py"],
        ["script/achievements.py"],
        ["script/quests.py"],
        ["script/chainoffers.py"],
        ["script/update.py"],
        ["script/convert.py"],
        ["script/zip.py"],
    ]

    if not nodownload:
        download_script = [
            f"script/setup.py",
            version,
        ]
        script_list.insert(0, download_script)

    return script_list


def cleanup(cleanup, nodownload, nocleanup):
    if nocleanup:
        return

    print("Starting cleanup")
    rm_dir = get_rm(nodownload)

    try:
        for directory in rm_dir:
            if os.path.exists(directory):
                shutil.rmtree(directory)

        print("Finished cleanup")
        if cleanup:
            sys.exit(1)
    except KeyboardInterrupt:
        print("Cleanup interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during cleanup: {e}")
        sys.exit(1)


def run_scripts(version, onlydownload, nodownload, delay):

    scripts = get_scripts(version, onlydownload, nodownload)

    try:
        print(f"Choosing version: {version}\n")
        for index, script in enumerate(scripts):
            print(f"Running {script[0]}...")

            subprocess.run(["python"] + script, check=True)
            print(f"Finished running {script[0]}.")

            # Sleep only if this is not the last script
            if index < len(scripts) - 1:
                time.sleep(delay)
                print("\n")
    except Exception as e:
        print(f"Error occurred while running script: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Script execution interrupted by user.")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Run Subway Surfers scripts.")
    parser.add_argument(
        "-v", "--version", type=str, default=None, help="Choose a specific version"
    )
    parser.add_argument(
        "-c", "--cleanup", action="store_true", help="Run cleanup function only"
    )
    parser.add_argument(
        "-nc", "--nocleanup", action="store_true", help="Prevents cleaning up any files"
    )
    parser.add_argument(
        "-ndl",
        "--nodownload",
        action="store_true",
        help="Run scripts without downloading the source files (requires pre-downloaded files)",
    )
    parser.add_argument(
        "-odl",
        "--onlydownload",
        action="store_true",
        help="Only downloads the source files",
    )
    parser.add_argument(
        "-dly",
        "--delay",
        type=int,
        default=5,
        help="Change the delay between the running scripts",
    )

    args = parser.parse_args()

    # If version is not provided, set it using the version() function
    if args.version is None:
        args.version = version()

    # Regex pattern
    version_pattern = r"^\d{1,2}-\d{1,2}-\d{1,2}$"

    # Validate 'version'
    if args.version and not re.match(version_pattern, args.version):
        print(
            "Error: 'version' has the wrong format. Please use the format 'X-Y-Z' (e.g., '3-12-2')."
        )
        sys.exit(1)

    try:
        cleanup(args.cleanup, args.nodownload, args.nocleanup)
        setup()
        run_scripts(args.version, args.onlydownload, args.nodownload, args.delay)

    except Exception as e:
        print("Error:", e)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Script terminated by user.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Script terminated by user.")
        sys.exit(1)
