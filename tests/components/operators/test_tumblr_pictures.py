# coding: utf-8

from crawling_sigma_chan.components.operators import TumblrPictures
from crawling_sigma_chan.data_structure import TumblrParameters
import pytest 


import pprint

class TestTumblrPictures:
    def test_init(self):
        tumblr_pictures = TumblrPictures()
        assert isinstance(tumblr_pictures, TumblrPictures)
    def test_get_pictures_url(self):
        tumblr_parameters = TumblrParameters(tag='')
        tumblr_pictures = TumblrPictures()
        tumblr_pictures.get_picture_urls(tumblr_parameters.api_url, tumblr_parameters.parameters_dict)
        print(type(tumblr_pictures))
        print(type(tumblr_pictures.response['response']))
        pprint.pprint(tumblr_pictures.response)
        
                          
