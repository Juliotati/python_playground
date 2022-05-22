from fastapi import FastAPI

from news import warframe_news, News

app = FastAPI()


@app.get("/")
def read_root():
    return read_news()


@app.get("/news/{news_id}")
def read_news(news_id: str):
    data: [] = warframe_news()
    requested_news = None

    for item in data:
        if item['id'] == news_id:
            requested_news = item
            break

    return requested_news


# For testing on the console
if __name__ == '__main__':
    read_news('62696304e8729e682710a8a7')
