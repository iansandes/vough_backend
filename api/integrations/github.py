import os
import requests
import json


class GithubApi:
    def __init__(self):
        self.GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        headers = {'Authorization': self.GITHUB_TOKEN}
        response = requests.get(
            f'https://api.github.com/orgs/{login}', headers=headers)
        return response.json(), response.status_code

    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        headers = {'Authorization': self.GITHUB_TOKEN}
        response = requests.get(
            f'https://api.github.com/orgs/{login}/members', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response
