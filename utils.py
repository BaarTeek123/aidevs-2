from ast import literal_eval
import os
from UTILS.settings import API_KEY


def get_response(main_url="https://zadania.aidevs.pl/token/", api_key=API_KEY, task_name=""):
    return literal_eval(os.popen(f"""curl -d '{{"apikey":"{api_key}"}}' {main_url}{task_name}""").read())


