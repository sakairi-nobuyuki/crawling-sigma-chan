# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from data_base.data_structure import DataBaseParameters

#engine = create_engine(
#        f"{database_parameters.dialect}+{database_parameters.driver}://{database_parameters.username}:{database_parameters.password}@{database_parameters.host}:{database_parameters.port}/{database_parameters.database}?charset={database_parameters.charset_type}")
#Base = declarative_base()

class DataBaseForTumblr(Base):
    __table_name__ = 'tumblr_db'

    id = Column(Integer, primary_key=True)
    file_path = Column(String)
    response_body = Column(String)
    

#def create_data_base_engine(database_parameters):

    #engine = create_engine(
#        f"{database_parameters.dialect}+{database_parameters.driver}://{database_parameters.username}:{database_parameters.password}@{database_parameters.host}:{database_parameters.port}/{database_parameters.database}?charset={database_parameters.charset_type}")
#    return engine