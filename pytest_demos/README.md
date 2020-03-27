## pytest测试框架
霍格活兹测试学院拉勾名企直推营录播课程

## Quit Start
 - pytest介绍
   
   pytest是一个非常成熟的全功能的Python测试框架 
简单灵活，容易上手;
支持参数化; 
测试用例的skip和xfail，自动失败重试等处理; 
能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appnium等自动化测试、接口自动化测试(pytest+requests); 
pytest具有很多第三方插件，并且可以自定义扩展， 比较好用的如 pytest-allure(完美html测试报告生成) ，pytest-xdist(多CPU分发) 等; 
可以很好的和jenkins集成;
文档 :https://docs.pytest.org/en/latest/contents.html#toc 
第三方库:https://pypi.org/search/?q=pytest

 - pytest依赖包
  ```$xslt
pip install –U pytest U表示升级 
pip install pytest-sugar   
pip install pytest-rerunfailures 
pip install pytest-xdist
pip install pytest-assume
pip intall pytest-html ……
pip list查看 
pytest –h 帮助 
```
 - pytest测试用例识别与运行
 ```$xslt
识别测试文件
test_*.py
*_test.py
识别测试用例
Test*类包含的所有test_*的方法(测试类不能带有__init__方法)
不在class中的所有的test_*方法
pytest也可以执行unittest框架写的用例和方法 
```
```$xslt
终端执行
pytest/py.test
pytest –v (最高级别信息--verbose)  打印详细运行日志信息
pytest -v -s 文件名 (s是带控制台输出结果，也是输出详细)  
pytest 文件名.py       执行单独一个pytest模块
pytest 文件名.py::类名                    运行某个模块里面某个类
pytest 文件名.py::类名::方法名      运行某个模块里面某个类里面的方法
pytest -v -k "类名 and not 方法名”   跳过运行某个用例
pytest -m [标记名]         @pytest.mark.[标记名] 将运行有这个标记的测试用例
pytest -x 文件名   一旦运行到报错就停止 运行
pytest  —maxfail=[num]          当运行错误达到num的时候就停止 运行
```
 - pytest 框架结构
 ```import pytest 类似的setup,teardown同样更灵活， 
模块级(setup_module/teardown_module)模块始末，全局的（优先最高） 
函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
类级(setup_class/teardown_class)只在类中前后运行一次（在类中） 
方法级(setup_method/teardown_methond)开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后```