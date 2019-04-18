#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: run_app.py
@time: 2019-04-17 15:58
"""


from app_demo import app


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        debug=app.config['DEBUG'],
    )
