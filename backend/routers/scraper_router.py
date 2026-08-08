from fastapi import APIRouter, HTTPException

from models.schemas import QuoteResponse
from services.scraper_service import scrape_page


router = APIRouter()


@router.get("/scrape", response_model=QuoteResponse)
def scrape(url: str):

    try:
        return scrape_page(url)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )