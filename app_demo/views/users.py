#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: users.py
@time: 2019-04-18 14:18
"""


from app_demo.apis.users import get_user

from flask import (
    jsonify,
)


def user_info(user_id):
    """
    用户信息
    """
    user_row = get_user(user_id)
    return jsonify(user_row.to_dict())
