import os
from dotenv import load_dotenv
load_dotenv()
from tiktoken import get_encoding
from langchain.chat_models import ChatOpenAI


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL ='gpt-3.5-turbo'


chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, streaming=True)
print(chat)

    # llm, = OpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    # results = llm.predict()

