"""
## C02L02 (L11)
"""
import json

from dotenv import load_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import TextLoader
from langchain.schema import Document, SystemMessage, HumanMessage

if __name__ == "__main__":
    load_dotenv()
    loader = TextLoader('files/02_11_docs/docs.md')
    doc = loader.load()

    documents = [list(map(lambda x: Document(page_content=x), sublist)) for sublist in  [d.page_content.split('\n\n') for d in doc]][0]

    llm = ChatOpenAI(max_retries=5, callbacks=[StreamingStdOutCallbackHandler()], streaming=True)
    SYSTEM_TEMPLATE = """Describe the following document with one of the following keywords:
            Mateusz, Jakub, Adam. Return the keyword and nothing else."""
    description_promise = [llm([SystemMessage(content=SYSTEM_TEMPLATE), HumanMessage(content=d.page_content)]).content
                           for d in documents]

    for d, metadata in zip(documents, description_promise):
        d.metadata['source']=metadata
    with open('files/02_11_docs/output.json', mode='w+') as f:
         json.dump([{'page_content': d.page_content, 'metadata': d.metadata} for d in documents], f, indent=2)



