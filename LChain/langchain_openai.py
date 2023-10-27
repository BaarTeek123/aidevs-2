from langchain.chat_models import ChatOpenAI
from UTILS.settings import  OPENAI_API_KEY
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OPENAI_MODEL ='gpt-3.5-turbo'


chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL, streaming=True)
memory = ConversationBufferWindowMemory(k=1)
chain = ConversationChain(llm=chat, memory=memory)
resp = chain.invoke()






