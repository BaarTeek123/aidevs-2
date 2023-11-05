import sys
import os

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import TextLoader

if __name__ == "__main__":
    load_dotenv()
    loader = TextLoader('files/02_11_docs/docs.md')
    doc = loader.load()
    # documents = doc.
    llm = ChatOpenAI(max_retries=5)


