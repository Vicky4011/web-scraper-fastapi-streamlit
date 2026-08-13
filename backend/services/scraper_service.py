import requests
from bs4 import BeautifulSoup


def scrape_page(url: str):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Unable to access the website: {e}")

    soup = BeautifulSoup(response.text, "html.parser")

    quote_blocks = soup.find_all("div", class_="quote")

    quotes = []

    for block in quote_blocks:

        text_element = block.find("span", class_="text")
        author_element = block.find("small", class_="author")

        if text_element:
            text = text_element.get_text(strip=True)
        else:
            text = "Unknown"

        if author_element:
            author = author_element.get_text(strip=True)
        else:
            author = "Unknown"

        tag_elements = block.find_all("a", class_="tag")

        tags = []

        for tag in tag_elements:
            tags.append(tag.get_text(strip=True))     #strip=True->removes unnecessary whitespace

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return {
        "quotes": quotes
    }