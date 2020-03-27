#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
@pytest.fixture(params=['第一条',2,'tome','第四条','第五条'])
def open(request):
    print(request.param)
    print("打开浏览器")
    return request.param


def test_case1(open):
    print("test_case1")
    pass

def test_case2():
    print("test_case2")
    pass


def test_case3(open):
    print("testcase 0003")
    print(open)
    print("test_case3")
    pass

if __name__ == '__main__':
    pytest.main()