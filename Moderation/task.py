import logging
from UTILS.settings import AIDEVS2_API_KEY
from Moderation.moderate import is_flagged

# Add the parent directory to sys.path
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from utils import api_request

if __name__ == "__main__":
    ### get task
    try:
        TASK_NAME = 'moderation'
        token = api_request("POST", f"https://zadania.aidevs.pl/token/{TASK_NAME}", data={"apikey": AIDEVS2_API_KEY})['token']
    except KeyError as ke:
        logging.error('Something went wrong. No token found.')
        quit(-1)
    try:
        TASK_NAME = 'moderation'
        task = api_request("POST", f"https://zadania.aidevs.pl/task/{token}", data={"apikey": AIDEVS2_API_KEY})
    except KeyError as ke:
        logging.error('Something went wrong. No task found.')
        quit(-1)

    ###### task

    answer = api_request("POST", f"https://zadania.aidevs.pl/answer/{token}", data={"apikey": AIDEVS2_API_KEY, "answer":
                       [is_flagged(sent) for sent in task['input']]})












