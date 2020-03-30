#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class TestMark:
    @pytest.mark.demo1
    def test_case1(self):
        print("testcase1")

    @pytest.mark.demo1
    def test_case2(self):
        print("testcase1")

    @pytest.mark.demo2
    def test_case3(self):
        print("testcase1")

    @pytest.mark.demo2
    def test_case4(self):
        print("testcase1")
if __name__ == '__main__':
    pytest.main(['-v','-s','test_mark.py','-m','demo1'])