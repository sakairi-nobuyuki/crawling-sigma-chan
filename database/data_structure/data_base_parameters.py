# coding: utf-8

from email import charset
from pydantic import BaseModel

class DataBaseParameters(BaseModel):
    dialect: str = 'postgresql'
    driver: str = 'default'
    user_name: str = 'user_name'
    password: str = 'password'
    host: str = 'localhost'
    port: str = 'default'
    database_name: str = 'hoge.db'
    charset_type: str = 'utf-8'
