from news import News, get_news

if __name__ == '__main__':
    data = get_news()
    news = News.from_json(data)

    print(news.to_string())
