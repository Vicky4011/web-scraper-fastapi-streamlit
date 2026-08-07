import requests
from bs4 import BeautifulSoup


def scrape_page(url: str):

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quote_blocks = soup.find_all("div", class_="quote")

    quotes = []

    for block in quote_blocks:

        text = block.find("span", class_="text").text

        author = block.find("small", class_="author").text

        tag_elements = block.find_all("a", class_="tag")

        tags = []

        for tag in tag_elements:
            tags.append(tag.text)

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return {
        "quotes": quotes
    }