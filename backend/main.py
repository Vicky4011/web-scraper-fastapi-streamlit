from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to the Web Scraper API"
    }


@app.get("/about")
def about():
    return {
        "application": "Web Scraper",
        "version": "1.0"
    }


@app.get("/scrape")
def scrape(url: str):
    return {
        "received_url": url
    }