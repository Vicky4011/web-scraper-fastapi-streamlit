from pydantic import BaseModel, HttpUrl


class Quote(BaseModel):
    text: str
    author: str
    tags: list[str]


class QuoteResponse(BaseModel):
    quotes: list[Quote]


class ScrapeRequest(BaseModel):
    url: HttpUrl