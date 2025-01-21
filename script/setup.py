import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import requests

org_name = "HerrErde"
repo_name = "subway-source"
folder_path = "temp/input"


def get_release(version):
    if version != None:
        api_url = f"https://api.github.com/repos/{org_name}/{repo_name}/releases/tags/{version}"
    else:
        api_url = f"https://api.github.com/repos/{org_name}/{repo_name}/releases/latest"

    response = requests.get(api_url).json()
    assets = response.get("assets", [])

    return assets


def download_asset(session, asset):
    asset_url = asset["browser_download_url"]
    asset_name = os.path.basename(asset_url)
    download_path = os.path.join(folder_path, asset_name)

    try:
        with session.get(asset_url) as response:
            response.raise_for_status()
            with open(download_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {asset_name} to {download_path}")
    except requests.RequestException as e:
        print(f"Failed to download {asset_name}: {str(e)}")


def main(assets):
    with ThreadPoolExecutor() as executor, requests.Session() as session:
        executor.map(lambda asset: download_asset(session, asset), assets)
        executor.shutdown(wait=True)  # Wait for all threads to finish


if __name__ == "__main__":
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except Exception as e:
        print(f"Error creating folder '{folder_path}': {e}")
        sys.exit(1)

    if len(sys.argv) < 2:
        version = None
    else:
        version = sys.argv[1]
        if not re.match(r"^\d{1,2}-\d{1,2}-\d{1,2}$", version):
            print(
                "Error: Invalid version format. Please use the format 'X-Y-Z' (e.g., '3-12-2')."
            )
            sys.exit(1)

    releases = get_release(version)

    main(releases)
