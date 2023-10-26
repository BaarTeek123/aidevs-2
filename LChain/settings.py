from langchain.prompts import ChatPromptTemplate
DEFAULT_ROLE = 'Python Senior Developer'
SYSTEM_TEMPLATE = """As a {role} who answers the questions ultra-concisely using CONTEXT below 
and nothing more and truthfully says "don't know" when the CONTEXT is not enough to give an answer.

context: ###{context}###
"""

HUMAN_TEMPLATE = """{text}"""


chatPrompt = ChatPromptTemplate.fromPromptMessages([
    ["system", SYSTEM_TEMPLATE],
    ["human", HUMAN_TEMPLATE],
]);