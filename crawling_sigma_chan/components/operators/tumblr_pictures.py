# coding: utf-8


import requests

class TumblrPictures:
    def __init__(self) -> None:
        pass


    def get_picture_urls(self, url: str, parameters: dict) -> list:
        self.response = requests.get(url, params=parameters).json()