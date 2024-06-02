from fastapi import FastAPI
from app.twitter_client import get_tweets
from app.facebook_client import get_facebook_posts
from app.terms_client import get_popular_terms
from app.sentiment_analysis import analyze_sentiment
from data_model.schemas import PopularTermsResponse, Post, SentimentResponse

app = FastAPI()

@app.get("/sentiment", response_model=SentimentResponse)
def get_sentiment(keyword: str, count: int = 100):
    tweets = get_tweets(keyword, count)
    facebook_posts = get_facebook_posts(keyword, count)
    google_trends = get_popular_terms()
    
    tweet_data = []
    facebook_data = []

    for tweet in tweets:
        score, magnitude = analyze_sentiment(tweet.text)
        tweet_data.append(Post(text=tweet.text, sentiment_score=score, sentiment_magnitude=magnitude))

    for post in facebook_posts:
        if 'message' in post:
            score, magnitude = analyze_sentiment(post['message'])
            facebook_data.append(Post(text=post['message'], sentiment_score=score, sentiment_magnitude=magnitude))

    return SentimentResponse(tweets=tweet_data, facebook_posts=facebook_data, google_trends=google_trends)

@app.get("/popular_terms", response_model=PopularTermsResponse)
def get_popular_terms_endpoint():
    terms = get_popular_terms()
    return PopularTermsResponse(terms=terms)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
