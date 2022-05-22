from pydantic import BaseModel
from pydantic.annotated_types import Any

from http_helper import HttpHelper


class News(BaseModel):
    id: str = '00x00'
    message: str = 'no message'
    link: str = ''
    date: str = ''
    image_link: str = ''

    def __init__(self, news_id: str, message: str, link: str, date: str, image_link: str, **data: Any):
        super().__init__(**data)
        self.id = news_id
        self.message = message
        self.link = link
        self.date = date
        self.image_link = image_link

    def to_string(self):
        return f'''
        id: {self.id}
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


def warframe_news(url: str = None):
    http_response = HttpHelper.get_request(url)
    decoded_data = HttpHelper.decode_content(http_response)
    return decoded_data
