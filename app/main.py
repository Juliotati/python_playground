from fastapi import FastAPI
from psycopg2 import Error

from app.routers.news import news
from app.routers.user import user

app = FastAPI(title="playground")

app.include_router(news.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return news.get_warframe_news()


if __name__ == '__main__':
    import psycopg2

    try:
        connection = psycopg2.connect(
            user="juliotati",
            password="123456",
            host="127.0.0.1",
            port="5432",
            database="playground")

        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        cursor.execute(
            '''
            CREATE table expenses (
            id INT NOT null PRIMARY KEY,
            name TEXT
        )''')
        connection.commit()

        print(record)
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
