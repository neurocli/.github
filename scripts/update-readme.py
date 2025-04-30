import requests
import os

# GitHub API token and organization
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', input("Enter Github Token: "))
ORG_NAME = "neurocli"

def fetch_repos():
    url = f"https://api.github.com/orgs/{ORG_NAME}/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    repos = response.json()

    # Extract repository names
    repo_details = [(repo['name'], repo['html_url']) for repo in repos]
    return repo_details

def update_readme(repos):
    readme_path = "README.md"
    with open(readme_path, "r") as file:
        content = file.read()

    # Example: Replace placeholder with repo details
    updated_section = "\n".join([f"- [{name}]({url})" for name, url in repos])
    updated_content = content.replace("<repositories_placeholder>", updated_section)

    with open(readme_path, "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    repos = fetch_repos()
    update_readme(repos)
