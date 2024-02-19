import requests
import os
from concurrent.futures import ThreadPoolExecutor

org_name = "HerrErde"
repo_name = "subway-source"


def get_release():
    base_url = f"https://api.github.com/repos/{org_name}/{repo_name}/releases/latest"
    response = requests.get(base_url).json()
    return response.get("assets", [])


def download_asset(session, asset):
    asset_url = asset["browser_download_url"]
    asset_name = os.path.basename(asset_url)

    try:
        with session.get(asset_url) as response:
            response.raise_for_status()
            with open(asset_name, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {asset_name}")
    except requests.RequestException as e:
        print(f"Failed to download {asset_name}: {str(e)}")


def download_assets(assets):
    with ThreadPoolExecutor() as executor, requests.Session() as session:
        executor.map(download_asset, [session] * len(assets), assets)
        executor.shutdown(wait=True)  # Wait for all threads to finish


download_assets(get_release())
