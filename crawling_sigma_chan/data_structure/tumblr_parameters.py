# coding: utf-8


from dotenv import load_dotenv
import os
import dataclasses

@dataclasses.dataclass
class TumblrParameters:
    _api_key: str = ''
    _tag: str = ''
    _api_url: str = ''
    _before: str = ''

    def __init__(self, tag: str = None) -> None:
        load_dotenv()
        
        self._api_key = os.getenv("TUMBLR_API_KEY")
        self._tag = self._set_initial_tag(tag)
        self._api_url = os.getenv("TUMBLR_API_URL")
        self._before = ''
        

    def _set_initial_tag(self, tag: str) -> str:

        if tag is None:
            return ''
        else:
            return tag

    
    
                    
    @property
    def parameters_dict(self) -> dict:
        return {'api_key': self._api_key, 'tag': self._tag}

    @property        
    def api_url(self) -> str:
        return self._api_url

    @api_url.setter
    def api_url(self, api_url: str) -> None:
        self._api_url = api_url

    @property
    def tag(self) -> str:
        return self._tag

    @tag.setter
    def tag(self, tag: str) -> None:
        self._tag = tag
