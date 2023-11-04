import sys
import os

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


if __name__ == "__main__":
    load_dotenv()
    secret_key = os.getenv('OPENAI_API_KEY')
    print(secret_key)
    # try:
    #
    #
    # MODEL_NAME = "gpt-3.5-turbo"
    # llm = ChatOpenAI(temperature=0, model_name=MODEL_NAME)
    #
    # conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory(), verbose=True)
    #
    # while True:
    #     question = input("You: ")
    #     if question == "exit":
    #         break
    #     response = conversation.predict(input=question)
    #     print(f"3*'\nAssistant: {response}")
