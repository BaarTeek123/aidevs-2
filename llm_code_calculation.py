"""
## C01L05 (L06)
Instead of simple answer return code to calculate correct answer --> allows to avoid the problems with calculations
"""
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

if __name__ == '__main__':
    load_dotenv()
    SYSTEM_TEMPLATE = """

    # Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
    # 2015 is coming in 36 hours, so today is 36 hours before.
    today = datetime(2015, 1, 1) - timedelta(hours=36)
    # One week from today,
    one_week_from_today = today + timedelta(days=7)
    # The answer formatted with MM/DD/YYYY is
    print(one_week_from_today.strftime('%m/%d/%Y'))

    # Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
    # If the first day of 2019 is a Tuesday, and today is the first Monday, then today is 6 days later.
    today = datetime(2019, 1, 1) + timedelta(days=6)
    # The answer formatted with MM/DD/YYYY is
    print(today.strftime('%m/%d/%Y'))

    # Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?
    # If the concert was scheduled for 06/01/1943 but delayed by one day, then today is one day later.
    today = datetime(1943, 6, 1) + timedelta(days=1)
    # 10 days ago,
    ten_days_ago = today - timedelta(days=10)
    # The answer formatted with MM/DD/YYYY is
    print(ten_days_ago.strftime('%m/%d/%Y'))

    # Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?
    # It is 4/19/1969 today.
    today = datetime(1969, 4, 19)
    # 24 hours later,
    later = today + timedelta(days=1)
    # The answer formatted with MM/DD/YYYY is
    print(later.strftime('%m/%d/%Y'))

    # Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?
    # If Jane thought today is 3/11/2002, but today is Mar 12, then today is 3/12/2002.
    today = datetime(2002, 3, 12)
    # 24 hours later,
    later = today + timedelta(days=1)
    # The answer formatted with MM/DD/YYYY is
    print(later.strftime('%m/%d/%Y'))

    # Q: Jane was born on the last day of February in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?
    # If Jane was born on the last day of February in 2001 and today is her 16th birthday, then today is 16 years later.
    today = datetime(2001, 2, 28) + timedelta(days=16*365)  # Not accounting for leap years
    # Yesterday,
    yesterday = today - timedelta(days=1)
    # The answer formatted with MM/DD/YYYY is
    print(yesterday.strftime('%m/%d/%Y'))
    ###
    """

    HUMAN_TEMPLATE = """Q: {question}"""
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_TEMPLATE),
        ("human", HUMAN_TEMPLATE),
    ])
    question = "Today is November 04, 2023. What will the date after 31 days from now in the format MM/DD/YYYY?"
    llm = ChatOpenAI(model_name='gpt-4')
    r = llm(chat_prompt.format_messages(
        question=question))
    print(f'User: {question}')
    ai_response = exec("""from datetime import datetime, timedelta\n""" + r.content.strip())

