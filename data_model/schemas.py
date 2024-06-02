from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    text: str
    sentiment_score: float
    sentiment_magnitude: float

class SentimentResponse(BaseModel):
    tweets: List[Post]
    facebook_posts: List[Post]
    google_trends: List[Post]

class PopularTermsResponse(BaseModel):
    terms: List[Post]
