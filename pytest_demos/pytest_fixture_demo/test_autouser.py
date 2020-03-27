#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")
    username = "1380000"
    return username

def test_search1(open):
    print(open)
    print("test_search1")
    # raise NameError
    pass

def test_search2():
    print("test_search2")
    pass


def test_search3():
    print("test_search3")
    pass


if __name__ == '__main__':
    pytest.main()