#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
# 不带参数的fixture默认参数为 scope=function
@pytest.fixture()
def login():
    print("这是个登录方法")

def pytest_configure(config):
    marker_list = ["search","login"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )