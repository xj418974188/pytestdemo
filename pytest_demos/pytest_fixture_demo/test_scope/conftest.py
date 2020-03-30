#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 作用域：module是在模块之前执行， 模块之后执行
import pytest

@pytest.fixture(scope="session")
def open():
    print("打开浏览器")
    yield

    print("执行teardown !")
    print("最后关闭浏览器")

def pytest_configure(config):
    marker_list = ["demo1","demo2"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )