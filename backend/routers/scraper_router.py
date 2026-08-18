from fastapi import APIRouter, HTTPException

from models.schemas import QuoteResponse, ScrapeRequest
from services.scraper_service import scrape_page


router = APIRouter()


@router.post("/scrape", response_model=QuoteResponse)
def scrape(request: ScrapeRequest):

    try:
        return scrape_page(str(request.url))

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )