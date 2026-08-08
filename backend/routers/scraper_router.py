from fastapi import APIRouter
from services.scraper_service import scrape_page


router = APIRouter()


@router.get("/scrape")
def scrape(url: str):
    return scrape_page(url)