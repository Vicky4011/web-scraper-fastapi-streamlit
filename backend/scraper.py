import requests
from bs4 import BeautifulSoup


def scrape_page(url: str):

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quote_tags = soup.find_all("span", class_="text")

    quotes = []

    for quote in quote_tags:
        quotes.append(quote.text)

    return {
        "quotes": quotes
    }