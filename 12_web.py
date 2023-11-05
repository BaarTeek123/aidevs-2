import json

from dotenv import load_dotenv
import html2text
import requests
from bs4 import BeautifulSoup
from langchain.schema import Document
import re

def webpage_to_markdown(url):
    # Fetch the content of the webpage
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    main_content = soup.find('main')
    if not main_content:
        main_content = soup

    # Convert HTML to Markdown
    converter = html2text.HTML2Text()
    converter.ignore_links = False

    return converter.handle(str(main_content))

def extract_links_from_markdown(markdown_content):
    return set(re.findall(r'\]\(([^)]+)\)', markdown_content))


if __name__ == "__main__":
    load_dotenv()
    urls = ["https://brain.overment.com"]


    docs = [Document(page_content=webpage_to_markdown(url),
                    metadata=
                    {'source': url, **{f'${i}': v for i, v in
                                       enumerate(extract_links_from_markdown(webpage_to_markdown(url)))}}) for url in urls]
    with open('files/02_12_web.json', mode='w+') as f:
        json.dump([{'page_content': d.page_content, 'metadata': d.metadata} for d in docs], f, indent=2)

