import requests

class SN6API:
    BASE_URL = "https://ifgames.win/api/v2"
    PUBLIC_API = "https://ifgames.win/api"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def post_event(self, title, description, cutoff):
        """
        Create a new event
        """
        url = f"{self.BASE_URL}/events"
        payload = {
            "title": title,
            "description": description,
            "cutoff": cutoff
        }

        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_event(self, event_id):
        """
        Get details of a specific event
        """
        url = f"{self.PUBLIC_API}/events/{event_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_predictions(self, event_id):
        """
        Get latest predictions per miner for the given event
        """
        url = f"{self.PUBLIC_API}/events/{event_id}/predictions"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_community_prediction(self, event_id):
        """
        Get community prediction for the given event
        """
        url = f"{self.PUBLIC_API}/events/{event_id}/community_prediction"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
