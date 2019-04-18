#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2019-04-17 15:55
"""


from __future__ import unicode_literals
from __future__ import print_function

import os
from importlib import import_module


MODE = os.environ.get('MODE') or 'default'


try:
    current_config = import_module('config.' + MODE)
    print('[√] 当前环境变量: %s' % MODE)
except ImportError:
    print('[!] 配置错误，请初始化环境变量')
