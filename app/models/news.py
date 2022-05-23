import datetime

from pydantic import BaseModel
from pydantic.annotated_types import Any


class News(BaseModel):
    news_id: str = ''
    message: str = ''
    link: str = ''
    date: str = f'{datetime.date.today()}'
    image_link: str = ''

    def __init__(self, news_id: str, message: str, link: str, date: str, image_link: str, **data: Any):
        super().__init__(**data)
        self.news_id = news_id
        self.message = message
        self.link = link
        self.date = date
        self.image_link = image_link

    def to_string(self):
        return f'''
        id: {self.news_id}
        message: {self.message}
        link: {self.link}
        date: {self.date}
        image_link: {self.image_link}
        '''

    @staticmethod
    def from_json(data: {}):
        return News(
            data['id'],
            data['message'],
            data['link'],
            data['date'],
            data['imageLink'],
        )
