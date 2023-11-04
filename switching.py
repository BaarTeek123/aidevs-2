"""
## C02L02 (L10)
"""
from dotenv import load_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.document_loaders import TextLoader



if __name__ == '__main__':
    load_dotenv()

    sources = [
        {'name': 'Jakub', 'source': 'files/02_10_switching/jakub.md'},
        {'name': 'Adam', 'source': 'files/02_10_switching/adam.md'},
        {'name': 'Mateusz', 'source': 'files/02_10_switching/mateusz.md'}
    ]

    llm = ChatOpenAI(callbacks=[StreamingStdOutCallbackHandler()], streaming =True)
    SYSTEM_TEMPLATE = f"""`Pick one of the following sources related to the query and return filename and nothing else. 
    If you don't know the answer, say "don't know". 
    Sources### """ + "\n".join(["->".join(k.values()) for k in sources])
    # question = 'Where Mateusz was born?'
    # question = 'Where Pablito was born?'
    question='Where Jakub works?'
    file_name = llm([
        SystemMessage(content=SYSTEM_TEMPLATE),
        HumanMessage(content=question)
    ]).content
    print()
    if file_name != "don't know":
        doc = TextLoader(file_name)
        doc.load()

        llm = ChatOpenAI(callbacks=[StreamingStdOutCallbackHandler()], streaming =True)
        SYSTEM_TEMPLATE = f"""Answer questions as truthfully using the context below and nothing more. If you don't know the answer, say "don't know".
        context###""" + '\n'.join([k.page_content for k in doc.load()]) + "###"

        llm([
        SystemMessage(content=SYSTEM_TEMPLATE),
        HumanMessage(content=question)

        ])














