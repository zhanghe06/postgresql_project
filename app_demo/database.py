#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: database.py
@time: 2019-04-18 14:10
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import current_config

SQLALCHEMY_DATABASE_URI = current_config.SQLALCHEMY_DATABASE_URI
SQLALCHEMY_POOL_SIZE = current_config.SQLALCHEMY_POOL_SIZE

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=SQLALCHEMY_POOL_SIZE, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from app_demo import models
    # from app_demo.models.demo import *
    Base.metadata.create_all(bind=engine)
