#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: users.py
@time: 2019-04-17 18:21
"""

# from app_demo.clients.client_pg import db_session_pg
from app_demo.database import db_session
from app_demo.models.demo import Users
# db_session = db_session_pg()


# def list_user():
#     sql = '''SELECT * FROM users'''
#     params = None
#     user_rows = db_session.execute(sql, params).fetchall()
#     return user_rows


# def get_user(user_id):
#     sql = '''SELECT * FROM users WHERE id=:id'''
#     params = {
#         'id': user_id,
#     }
#     user_row = db_session.execute(sql, params).fetchone()
#     return user_row

def get_user(user_id):
    result = db_session.query(Users).get(user_id)
    return result
