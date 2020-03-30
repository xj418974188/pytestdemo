#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.mark.usefixtures("open")
def test_search1():
    print("test_search1")
    pass


def test_search2(open):
    print("test_search2")
    pass


def test_search3(open):
    print("test_search3")
    pass


if __name__ == '__main__':
    pytest.main()
