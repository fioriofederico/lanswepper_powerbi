import requests
from .config import API_URL
from .auth import get_access_token

class LansweeperClient:
    def __init__(self):
        self.token = get_access_token()
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }

    def fetch_assets(self):
        response = requests.get(API_URL, headers=self.headers)
        response.raise_for_status()
        return response.json()["data"]
