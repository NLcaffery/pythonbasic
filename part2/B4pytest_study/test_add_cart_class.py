# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_add_cart_class.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/4/16 17:09
# @Copyright: 北京码同学
from requests_study.mtxshop_apis import login_buyer, add_cart


class TestAddCart:

    def test_add_cart(self):
        login_buyer()
        resp = add_cart()
        # 断言状态码
        assert resp.status_code == 200