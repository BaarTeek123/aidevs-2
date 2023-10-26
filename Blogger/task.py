import logging
from UTILS.settings import AIDEVS2_API_KEY

# Add the parent directory to sys.path
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from utils import api_request

if __name__ == "__main__":
    ### get task
    try:
        TASK_NAME = 'blogger'
        token = api_request("POST", f"https://zadania.aidevs.pl/token/{TASK_NAME}", data={"apikey": AIDEVS2_API_KEY})['token']
    except KeyError as ke:
        logging.error('Something went wrong. No token found.')
        quit(-1)
    try:
        TASK_NAME = 'moderation'
        task = api_request("POST", f"https://zadania.aidevs.pl/task/{token}", data={"apikey": AIDEVS2_API_KEY})
        print(task)
    except KeyError as ke:
        logging.error('Something went wrong. No task found.')
        quit(-1)















