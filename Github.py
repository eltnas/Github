from github import Github
import os

# Seu username do github
username = "eltnas"

# Seu token de acesso do GitHub
# Site: https://github.com/settings/tokens
token = ""  

# Diretório
destination_folder = "Github"


g = Github(token)
user = g.get_user(username)
repos = user.get_repos()

for repo in repos:
    repo_name = repo.name
    repo_url = repo.clone_url

    repo_path = os.path.join(destination_folder, repo_name)

    if os.path.exists(repo_path):
        print(f"O repositório '{repo_name}' já existe. Pulando...")
        continue

    os.system(f"git clone {repo_url} {repo_path}")

    print(f"Repositório '{repo_name}' clonado com sucesso!")

print("Todos os repositórios foram baixados.")
