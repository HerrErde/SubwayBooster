import requests


org_name = "HerrErde"
repo_name = "subway-source"


files = [
    "boards_data.json",
    "boards_links.json",
    "characters_data.json",
    "characters_links.json",
]


def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "wb") as file:
        file.write(response.content)


def download_latest_files():
    base_url = f"https://github.com/{org_name}/{repo_name}/releases/latest/download/"
    for file in files:
        url = base_url + file
        download_file(url, file)


if __name__ == "__main__":
    download_latest_files()
