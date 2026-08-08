from pydantic import BaseModel

class Quote(BaseModel):
    text: str
    author: str
    tags: list[str]


class QuoteResponse(BaseModel):
    quotes: list[Quote]