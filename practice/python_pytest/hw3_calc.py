#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
1、编写用例顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
"""

import pytest
@pytest.mark.first
def test_case(cmdoption):
    print(f"这是{cmdoption}环境")

# 创建测试类
class TestCalc2:
    # 创建加法测试用例,并传入fixture
    # 使用ordering插件控制用例执行顺序
    @pytest.mark.run(order=1)
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
    @pytest.mark.run(order=4)
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

    @pytest.mark.run(order=2)
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

    @pytest.mark.run(order=3)
    # 创建乘法测试用例,并传入fixture
    def test_mul(self, get_calc, get_mul_data):
        result = get_calc.mul(get_mul_data[0], get_mul_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_data[2]
