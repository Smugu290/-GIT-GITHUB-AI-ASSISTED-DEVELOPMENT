import requests


def fetch_github_profile(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_repositories(username: str) -> list:
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main() -> None:
    username = input("Enter a GitHub username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    try:
        profile = fetch_github_profile(username)
    except requests.HTTPError as error:
        if error.response.status_code == 404:
            print(f"GitHub user '{username}' not found.")
        else:
            print(f"Error fetching profile: {error}")
        return

    followers = profile.get("followers", 0)
    public_repos = profile.get("public_repos", 0)
    name = profile.get("name") or profile.get("login")
    bio = profile.get("bio")

    print(f"\nGitHub Profile: {name}")
    if bio:
        print(f"Bio: {bio}")
    print(f"Followers: {followers}")
    print(f"Public repos: {public_repos}")

    try:
        repos = fetch_repositories(username)
    except requests.HTTPError as error:
        print(f"Error fetching repositories: {error}")
        return

    if repos:
        print("\nRepositories:")
        for repo in repos:
            print(f"- {repo.get('name')}")
    else:
        print("\nNo public repositories found.")


if __name__ == "__main__":
    main()
