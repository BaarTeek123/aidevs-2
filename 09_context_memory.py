"""
## C02L02 (L09)
"""
from dotenv import load_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.document_loaders import TextLoader

if __name__ == '__main__':
    load_dotenv()
    doc = TextLoader("files/02_09_context.md")
    doc.load()

    llm = ChatOpenAI(callbacks=[StreamingStdOutCallbackHandler()], streaming =True)
    SYSTEM_TEMPLATE = f"""Answer questions as truthfully using the context below and nothing more. If you don't know the answer, say "don't know".
        context###""" + '\n'.join([k.page_content for k in doc.load()]) + "###"

    llm([
        SystemMessage(content=SYSTEM_TEMPLATE),
        HumanMessage(content='Who is overment?')

    ])













