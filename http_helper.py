import json

import requests
from requests import Response


class HttpHelper:

    @staticmethod
    def get_request(url: str = None):
        return requests.get(url or 'https://api.warframestat.us/ps4/news')

    @staticmethod
    def decode_content(data: Response):
        return json.loads(data.content.decode('utf-8'))
