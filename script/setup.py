import requests
import os
import concurrent.futures

org_name = "HerrErde"
repo_name = "subway-source"


def get_release_assets():
    base_url = f"https://api.github.com/repos/{org_name}/{repo_name}/releases/latest"
    response = requests.get(base_url).json()
    return response.get("assets", [])


def download_asset(asset):
    asset_url = asset["browser_download_url"]
    asset_name = os.path.basename(asset_url)

    try:
        with open(asset_name, "wb") as file:
            file.write(requests.get(asset_url).content)
        print(f"Downloaded {asset_name}")
    except requests.RequestException as e:
        print(f"Failed to download {asset_name}: {str(e)}")


def download_assets(assets):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_asset, assets)


if __name__ == "__main__":
    release_assets = get_release_assets()
    if release_assets:
        download_assets(release_assets)
