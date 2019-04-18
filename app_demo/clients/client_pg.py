#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: client_pg.py
@time: 2019-04-17 16:48
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from config import current_config

SQLALCHEMY_DATABASE_URI_PG = current_config.SQLALCHEMY_DATABASE_URI_PG
SQLALCHEMY_POOL_SIZE = current_config.SQLALCHEMY_POOL_SIZE


# 方式一：默认开启连接池，不设连接回收时间，连接永不回收（需要自己维护连接，两种方式：悲观处理、乐观处理，都需要动代码）
# engine_pg = create_engine(SQLALCHEMY_DATABASE_URI_PG, pool_size=SQLALCHEMY_POOL_SIZE, max_overflow=0)

# 方式二：开启连接池，设置连接回收时间（web应用，短连接推荐这种方式）
engine_pg = create_engine(SQLALCHEMY_DATABASE_URI_PG, pool_recycle=200, pool_size=SQLALCHEMY_POOL_SIZE, max_overflow=0)

# 方式三：禁用连接池，适合长连接、多任务场景
# engine_pg = create_engine(SQLALCHEMY_DATABASE_URI_PG, poolclass=NullPool)

db_session_pg = sessionmaker(bind=engine_pg, autocommit=True)
