from ast import literal_eval
import os
from UTILS.settings import AIDEVS2_API_KEY

import requests


def api_request(method, url, api_key=AIDEVS2_API_KEY, data=None):
    """
    Make an API request using POST or GET method.

    :param method: The request method, either 'POST' or 'GET'.
    :param url: The API endpoint URL.
    :param api_key: The API key.
    :param data: The data to be sent in the request body (relevant for POST method).
    :return: The API response.
    """

    headers = {
        'Authorization': f'Bearer {api_key}',  # This assumes the API expects the API key as a Bearer token.
        'Content-Type': 'application/json',  # This is for sending JSON data. Adjust if needed.
    }

    if method.upper() == 'POST':
        response = requests.post(url, json=data, headers=headers)
    elif method.upper() == 'GET':
        response = requests.get(url, headers=headers)
    else:
        raise ValueError("Method should be either 'POST' or 'GET'")

    response.raise_for_status()  # This will raise an HTTPError if the response was an error.
    return response.json()


def get_response_os(task_name: str, main_url="https://zadania.aidevs.pl/token/", api_key=AIDEVS2_API_KEY) -> dict:
    return literal_eval(os.popen(f"""curl -d '{{"apikey":"{api_key}"}}' {main_url}{task_name}""").read())

