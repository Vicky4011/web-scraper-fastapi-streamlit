from fastapi import APIRouter

from models.schemas import QuoteResponse
from services.scraper_service import scrape_page


router = APIRouter()


@router.get("/scrape", response_model=QuoteResponse)
def scrape(url: str):
    return scrape_page(url)