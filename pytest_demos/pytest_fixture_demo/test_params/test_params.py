#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml


@pytest.mark.parametrize("a,b", yaml.safe_load(open("datas.yml",encoding='utf-8')))
def test_foo(a,b):
    print(f"a + b = {a + b}")

def test_yaml():
    print(yaml.safe_load(open("datas.yml")))