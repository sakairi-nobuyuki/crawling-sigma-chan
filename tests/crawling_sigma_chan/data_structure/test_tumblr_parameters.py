# coding: utf-8

import pytest
from dotenv import load_dotenv
import os
from crawling_sigma_chan.data_structure import TumblrParameters, tumblr_parameters

class TestTumblrParameters:
    def test_init(self):
        tumblr_parameters = TumblrParameters()
        load_dotenv()

        assert tumblr_parameters.api_url == os.getenv("TUMBLR_API_URL")
        assert tumblr_parameters.parameters_dict["api_key"] == os.getenv("TUMBLR_API_KEY")

    def test_init_with_default_tag(self):
        tumblr_parameters = TumblrParameters(tag = "hoge")

        
        assert tumblr_parameters.tag == "hoge"

    def test_set_and_get_tag(self):
        tumblr_parameters = TumblrParameters()


        assert tumblr_parameters.tag == ""

        tumblr_parameters.tag = "hoge"

        assert tumblr_parameters.tag == "hoge"