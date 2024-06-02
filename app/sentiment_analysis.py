import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str):
    sentiment = sia.polarity_scores(text)
    score = sentiment['compound']
    magnitude = abs(sentiment['pos'] - sentiment['neg'])
    return score, magnitude
