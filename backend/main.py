from fastapi import FastAPI
from services.scraper import scrape_page

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to the Web Scraper API"
    }


@app.get("/scrape")
def scrape(url: str):
    return scrape_page(url)