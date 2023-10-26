from UTILS.settings import OPENAI_API_KEY

from pathlib import Path
import sys
# Add the parent directory to sys.path
sys.path.append(str(Path(__file__).parent.parent))
from utils import api_request


def moderate_text(text):
    url = "https://api.openai.com/v1/moderations"
    data = {"input": text}

    return api_request("POST", url, OPENAI_API_KEY, data)

def is_flagged(text) -> bool:
    return moderate_text(text)["results"][0]["flagged"]

def get_reasons(text) -> list:
    return [k for k,v in moderate_text(text)["results"][0]["category"].items() if v ]