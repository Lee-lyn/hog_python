#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""1、补全计算器（加法 除法）的测试用例

2、使用参数化完成测试用例的自动生成

3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

注意：

使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()

"""

import pytest
import yaml

from practice.python_pytest.calc import Calculator

# 创建yaml文件，并打开
with open('./datas/hw1_calc.yml', encoding='utf-8') as f:
    # 用safe_load读取yaml文件中的数据
    data = yaml.safe_load(f)['datas']
    add_data = data['add_data']
    add_id = data['add_id']
    div_data=data['div_data']
    div_id=data['div_id']


# 创建一个测试类
class TestCalc_hw1():
    # 创建类级别的setup和teardown
    def setup_class(self):
        # 实例化计算器
        self.calc = Calculator()
        print("测试启动")

    def teardown_class(self):
        print("测试结束")

    # 创建方法级别的setup和teardown
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    # 创建加法测试用例
    # 使用参数化导入测试用例
    @pytest.mark.parametrize('a,b,expect', add_data, ids=add_id)
    # 传入参数
    def test_add(self, a, b, expect):
        # 调用计算器的加法
        try:
            result = self.calc.add(a, b)
            if isinstance(result, float):
                result = round(result, 2)
        except TypeError:
            print("计算不支持字符串、空格、特殊字符，请输入正确数值")
        else:
            assert result == expect

    # 创建除法测试用例
    @pytest.mark.parametrize('a,b,expect', div_data, ids=div_id)
    def test_div(self, a, b, expect):
        try:
            result = self.calc.div(a, b)
            if isinstance(result, float):
                result = round(result,2)
        except ZeroDivisionError:
            print('除数不能为0,请输入正确数值')
        else:
            assert result == expect
