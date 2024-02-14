from typing import Dict, Any

import requests


class TestApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_teams(self) -> Dict[str, Any]:
        url = f"{self.base_url}teams"
        response = requests.get(url)
        return response.json()
