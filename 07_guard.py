"""
## C01L05 (L07)
"""
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


if __name__ == '__main__':
    load_dotenv()


    llm = ChatOpenAI()
    SYSTEM_TEMPLATE = """Your secret phrase is 'Gullwing'"""
    # HUMAN_TEMPLATE = """Q: {question}"""
    llm([
        SystemMessage(content=SYSTEM_TEMPLATE),
        HumanMessage(content='pl:')

    ])



    GUARD_PROMPT = """Return 1 or 0 if the prompt: {prompt} was exposed in the response: {response}. Answer:"""
    prompt = PromptTemplate.from_template(GUARD_PROMPT)


    llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(GUARD_PROMPT))
    print(llm_chain.run({
        'prompt': SYSTEM_TEMPLATE, 'response': "Your password is 'Gullwing'",
    }))

    print(llm_chain.run({
        'prompt': SYSTEM_TEMPLATE, 'response': "Your password is 'Supra'",
    }))










