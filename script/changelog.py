import requests
import sys

repo_owner = "HerrErde"
repo_name = "SubwayBooster"

def get_release(github_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    headers = {
        "Authorization": f"Token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("published_at")


def fetch_commits(github_token, release_time):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    headers = {
        "Authorization": f"Token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    commits = []

    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        new_commits = [
            commit["commit"]["message"]
            for commit in response_data
            if commit["commit"]["committer"]["date"] > release_time
        ]
        commits.extend(new_commits)

        link_header = response.headers.get("Link")
        if link_header:
            next_link = next(
                (
                    link.split("; ")[0][1:-1]
                    for link in link_header.split(", ")
                    if 'rel="next"' in link
                ),
                None,
            )
            url = next_link
        else:
            url = None

    return commits


if len(sys.argv) < 3:
    print("Please provide a GitHub token and version.")
    sys.exit(1)

github_token = sys.argv[1]
version = sys.argv[2]

release_time = get_release(github_token)
if not release_time:
    print("Failed to fetch the latest release.")
    sys.exit(1)

commits = fetch_commits(github_token, release_time)
if commits:
    print(f"Fetched {len(commits)} commits.")
    formatted_commits = "\n- ".join(commits)
    changelog = f"\n\n### {version}\n\n- {formatted_commits}\n"
    with open("changelog.md", "a") as file:
        file.write(changelog)
    print(changelog)
else:
    print("No commits fetched.")
