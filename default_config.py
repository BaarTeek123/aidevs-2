
import os

AIDEVS2_API_KEY = os.getenv('AIDEVS2_API_KEY')

DEFAULT_OPENAI_MODERATE_REQUEST_CONF = {
    "method": "POST",
    "url": "https://api.openai.com/v1/moderations",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AIDEVS2_API_KEY}"
    },
    "json": {
        "input": "Sample text goes here"
    }
}

print(os.environ)
