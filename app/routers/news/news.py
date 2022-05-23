from app.models.news import News
from app.utils.error_response import ErrorResponse
from fastapi import APIRouter

from app.utils.http_helper import HttpHelper

router = APIRouter(
    prefix="/news",
    tags=["News"]
)


@router.get("/{news_id}")
def read_news(news_id: str):
    data: [] = get_warframe_news()
    requested_news = None

    for item in data:
        if item['id'] == news_id:
            requested_news = item
            break

    if requested_news is None:
        raise ErrorResponse.not_found(news_id)

    return News.from_json(requested_news).dict()


@router.put("/{news_id}")
def update_news(news_id: str, news: News):
    return {"news_id": news_id, "news_message": news.message, "link": news.link, "date": news.date,
            "image_link": news.image_link}


@router.post("/")
def add_news(news: News):
    return news


@router.delete("/{news_id}")
def update_news(news_id: str):
    return {"message": f"Deleted news item with id {news_id}"}


def get_warframe_news(url: str = None):
    http_response = HttpHelper.get_request(url)
    decoded_data = HttpHelper.decode_content(http_response)
    return decoded_data
