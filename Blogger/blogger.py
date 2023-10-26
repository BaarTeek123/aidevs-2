from langchain.prompts import ChatPromptTemplate


SYSTEM_TEMPLATE = """As a Famous author of a cookbooks who answers the questions IN POLISH LANGUAGE using CONTEXT below 
and nothing more and truthfully says "don't know" when the CONTEXT is not enough to give an answer.
"""


chatPrompt = ChatPromptTemplate.fromPromptMessages([
    ["system", SYSTEM_TEMPLATE],
    ["human", HUMAN_TEMPLATE],
]);