from pytrends.request import TrendReq
from pytrends.exceptions import ResponseError

from data_model.schemas import Post
from .sentiment_analysis import analyze_sentiment

def get_popular_terms():
    pytrends = TrendReq()

    try:
        # Build payload with broader keywords
        pytrends.build_payload(
            kw_list=["election", "covid-19", "vaccine", "stock market", "crypto", "polotics"], 
            cat=0, 
            timeframe='now 7-d', 
            geo='US', 
            gprop='news'
        )
        trends = pytrends.interest_over_time()
        
        print("Trends Data:", trends)  # Debug statement

        popular_terms = []
        for keyword in trends.columns[:-1]:  # Skip the 'isPartial' column
            if keyword in trends:
                for date, value in trends[keyword].items():
                    print(f"Processing {keyword} on {date}: {value}")  # Debug statement
                    if value > 0:  # Only consider non-zero values
                        sentiment_score, sentiment_magnitude = analyze_sentiment(keyword)
                        popular_terms.append(Post(
                            text=f"{keyword} ({date.strftime('%Y-%m-%d')})",
                            sentiment_score=sentiment_score,
                            sentiment_magnitude=sentiment_magnitude
                        ))
        
        print("Popular Terms:", popular_terms)  # Debug statement
        return popular_terms
    except ResponseError as e:
        print(f"An error occurred: {e}")
        return []
