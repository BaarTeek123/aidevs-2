import requests
from dotenv import load_dotenv

load_dotenv()
class ApiHandler:
    def __init__(self, api_key, base_url):
        self.base_url = base_url
        self.api_key = api_key

    def _get_url(self, endpoint, token):
        if endpoint is not None and token is not None:
            return f"{self.base_url}/{endpoint}/{token}"
        return f"{self.base_url}"

    def _post_request(self, endpoint=None, token=None, data=None, headers=None):

        url = self._get_url(endpoint, token)
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def _get_request(self, endpoint, token):
        url = self._get_url(endpoint, token)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def authenticate_task(self, task_name):
        payload = {"apikey": self.api_key}
        return self._post_request('token', task_name, payload)["token"]

    def get_task(self, token):
        return self._get_request('task', token)

    def send_task(self, token, question, headers=None):
        return self._post_request('task', token, question, headers)

    def send_answer(self, token, answer, headers=None):
        return self._post_request('answer', token, answer, headers)