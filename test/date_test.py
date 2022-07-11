#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   date_test.py
@Time    :   2022/07/11 17:40:07
@Author  :   Desire
@Version :   1.0
@Contact :   yangyin@addcn.com
@Desc    :   None
"""

import os
import sys


# 把项目根路径插入到路径查询列表中
sys.path.insert(1, os.getcwd())
# here put the import lib

from tools import date


class TestDate(object):

    def test_get_days_date_before(self):
        days_date_before = date.get_days_date_before(days=31)
        print(days_date_before)

    def test_get_now_date(self):
        now_date = date.get_now_date(fmt="%Y-%m-%d %H:%M:%S")
        print(now_date)
