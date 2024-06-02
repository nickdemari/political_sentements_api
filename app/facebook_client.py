import facebook
from .config import settings

graph = facebook.GraphAPI(access_token=settings.FACEBOOK_ACCESS_TOKEN)

def get_facebook_posts(keyword: str, limit: int = 100):
    posts = graph.request(f"/search?q={keyword}&type=post&limit={limit}")
    return posts['data']
