import requests


def fetch_html(url: str):
    response = requests.get(url)

    return response.text