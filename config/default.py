#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: default.py
@time: 2019-04-17 15:58
"""


from __future__ import unicode_literals

import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

CSRF_ENABLED = True

# >>> import os
# >>> os.urandom(24)
SECRET_KEY = '\x03\xabjR\xbbg\x82\x0b{\x96f\xca\xa8\xbdM\xb0x\xdbK%\xf2\x07\r\x8c'

PREFERRED_URL_SCHEME = 'https'

# requests 超时设置
REQUESTS_TIME_OUT = (30, 30)

HOST = '0.0.0.0'

# 数据库 PostgresQL
DB_PG = {
    'host': HOST,
    'user': 'www',
    'password': '123456',
    'port': 5432,
    'database': 'demo'
}

SQLALCHEMY_DATABASE_URI_PG = \
    'postgresql://%s:%s@%s:%s/%s' % \
    (DB_PG['user'], DB_PG['password'], DB_PG['host'], DB_PG['port'], DB_PG['database'])

SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_PG

SQLALCHEMY_POOL_SIZE = 5
