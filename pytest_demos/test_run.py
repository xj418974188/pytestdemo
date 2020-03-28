#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
class TestDemo():
    def test_a(self):
        print("test a")


    def test_b(self):
        print("test b")
        # assert 'h' in 'this'

if __name__ == '__main__':
    pytest.main(['-v','-s', 'test_run.py::TestDemo::test_a'])