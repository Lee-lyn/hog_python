#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
1、补全计算器（加减乘除）的测试用例
2、使用fixture方法，完成加减乘除用例的自动生成，添加别名
3、修改测试用例的收集规则，执行所有以 check_开头和test_ 开头的测试用例
4、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
5、将 Fixture 方法存放在conftest.py ，灵活设置scope的级别
"""



# 创建测试类
class TestCalc2:
    # 创建加法测试用例,并传入fixture
    def test_add(self, get_calc, get_add_data):
        try:
            result = get_calc.add(get_add_data[0], get_add_data[1])
            if isinstance(result, float):
                result = round(result, 2)
        except TypeError:
            print("计算不支持字符串、特殊字符、空格，请输入正确数值")
        else:
            assert result == get_add_data[2]

    # 创建除法测试用例,并传入fixture
    def test_div(self, get_calc,get_div_data):
        try:
            result = get_calc.div(get_div_data[0], get_div_data[1])
            if isinstance(result, float):
                result = round(result, 2)
        except TypeError:
            print("计算不支持字符串、特殊字符、空格，请输入正确数值")
        except ZeroDivisionError:
            print("除数不能为0")
        else:
            assert result == get_div_data[2]

    # 创建减法测试用例,并传入fixture
    def test_sub(self, get_calc, get_sub_data):
        try:
            result = get_calc.sub(get_sub_data[0], get_sub_data[1])
            if isinstance(result, float):
                result = round(result, 2)
        except TypeError:
            print("计算不支持字符串、特殊字符、空格，请输入正确数值")
        else:
            assert result == get_sub_data[2]

    # 创建乘法测试用例,并传入fixture
    def test_mul(self, get_calc, get_mul_data):
        result = get_calc.mul(get_mul_data[0], get_mul_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_data[2]
