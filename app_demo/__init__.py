#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2019-04-17 15:56
"""


from __future__ import unicode_literals

from config import current_config

from flask import Flask

# from app_demo.database import init_db
from app_demo.database import db_session
from app_demo import views
from app_demo.views import users

from app_demo.helpers.lazy_load import LazyView

app = Flask(__name__)
app.config.from_object(current_config)

# init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# 注册路由
# app.add_url_rule('/', view_func=views.index)
# app.add_url_rule('/user/<user_id>', view_func=views.users.user_info)

# 注册路由(lazy load 方式)
app.add_url_rule('/', view_func=LazyView('app_demo.views.index'))
app.add_url_rule('/user/<user_id>', view_func=LazyView('app_demo.views.users.user_info'))
