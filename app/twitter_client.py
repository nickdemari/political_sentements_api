import tweepy
from .config import settings

auth = tweepy.OAuth1UserHandler(
    settings.TWITTER_CONSUMER_KEY,
    settings.TWITTER_CONSUMER_SECRET,
    settings.TWITTER_ACCESS_TOKEN,
    settings.TWITTER_ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

def get_tweets(keyword: str, count: int = 100):
    tweets = api.search(q=keyword, lang='en', count=count)
    return tweets
