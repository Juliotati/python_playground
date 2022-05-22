from fastapi import FastAPI

from error_response import ErrorResponse
from news import warframe_news, News

app = FastAPI()


@app.get("/")
def read_root():
    return warframe_news()


@app.get("/news/{news_id}")
def read_news(news_id: str):
    data: [] = warframe_news()
    requested_news = None

    for item in data:
        if item['id'] == news_id:
            requested_news = item
            break

    if requested_news is None:
        raise ErrorResponse.not_found(news_id)

    return News.from_json(requested_news).dict()


@app.put("/news/{news_id}")
def update_news(news_id: str, news: News):
    return {"news_id": news_id, "news_message": news.message, "link": news.link, "date": news.date,
            "image_link": news.image_link}


@app.post("/news")
def add_news(news: News):
    return news


@app.delete("/news/{news_id}")
def update_news(news_id: str):
    return {"message": f"Deleted news item with id {news_id}"}


if __name__ == '__main__':
    rs = read_news('62696304e8729e682710a8a7')
    print(rs)
