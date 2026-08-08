from fastapi import FastAPI
from routers.scraper_router import router as scraper_router


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to the Web Scraper API"
    }


app.include_router(scraper_router)