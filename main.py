from fastapi import FastAPI

from app.models.user import UserProfile
from app.routers.news import news
from app.routers.user import user

app = FastAPI(title="playground")

app.include_router(news.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return news.get_warframe_news()


if __name__ == '__main__':
    rs = news.read_news('62696304e8729e682710a8a7')
    print(rs)

    usr = UserProfile(user_id=1, name='julio', email='julio@tati.com')
    print(usr.to_string())

    usr.copy_with(name='yuri')
    print(usr.to_string())
