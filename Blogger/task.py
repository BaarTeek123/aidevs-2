import logging
from UTILS.settings import AIDEVS2_API_KEY

# Add the parent directory to sys.path
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from utils import api_request
from langchain.chat_models import ChatOpenAI
from UTILS.settings import  OPENAI_API_KEY
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SYSTEM_TEMPLATE = """As a Famous author of a cookbooks who writes his own blog IN POLISH LANGUAGE and nothing more and truthfully says "don't know" when the CONTEXT is not enough to give an answer.
Write short blog post (IN POLISH LANGUAGE, 4-5 sentences) about the following topic: {topic}"""


OPENAI_MODEL ='gpt-3.5-turbo'
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, streaming=True)
memory = ConversationBufferWindowMemory(k=1)
chain = ConversationChain(llm=chat, memory=memory)



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


    answer = api_request("POST", f"https://zadania.aidevs.pl/answer/{token}", data={"apikey": AIDEVS2_API_KEY, "answer":
                       [f"Rozdział {i+1}"+ chain.invoke(SYSTEM_TEMPLATE.format(topic=topic))['response'] for i, topic in enumerate(task['blog'])]})

    print(answer)

















