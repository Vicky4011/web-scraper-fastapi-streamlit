from fastapi import FastAPI
from scraper import fetch_html

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to the Web Scraper API"
    }


@app.get("/scrape")
def scrape(url: str):
    html = fetch_html(url)

    return {
        "html": html
    }