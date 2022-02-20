# coding: utf-8


from dotenv import load_dotenv
import os
import dataclasses

@dataclasses.dataclass
class TumblrParameters:
    api_key: str = None
    tag: str = None


    def __init__(self, tag: str = None) -> dict:
        load_dotenv()
        self.api_key = os.getenv("TUMBLR_API_KEY")
        self.tag = tag
        self.api_url = os.getenv("TUMBLR_API_URL")

        return {'api_key': self.api_key, 'tag': self.tag}
        