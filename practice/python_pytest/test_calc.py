# 在命令行中执行pytest，出现找不到路径的情况，需要在最开始加入以下命令
import os

yamlfilepath = os.path.dirname(__file__) + "/datas/calc.yml"

# 导入该文件需要的库
import pytest
import yaml

# 导入开发的源码
from practice.python_pytest.calc import Calculator

# 通过 with open('路径') as 别名 语句读取yaml文件
with open(yamlfilepath) as f:
    # 只能 safe_load 一次，需要保存到变量中
    datas = yaml.safe_load(f)['add']
    # 获取yaml中的具体值要留意其数据格式，以正确的方式获取值（字典（用key值获取）、列表（用下标获取））
    adddatas = datas['datas']
    myid = datas['myid']


# 创建一个测试类，不要包含__init__()方法
class TestCalc:
    # 创建类级别的setup
    def setup_class(self):
        print("开始计算")
        # 实例化计算器，前面加self变成实例变量
        self.calc = Calculator()

    # 创建类级别的teardown
    def teardown_class(self):
        print("结束计算")

    # 使用参数化方式从yaml文件里获取数据
    @pytest.mark.parametrize('a,b,expect', adddatas, ids=myid)
    # 创建测试方法，并定义参数
    def test_add1(self, a, b, expect):
        # 调用源码中的某个方法，此处是计算器的加法
        result = self.calc.add(a, b)
        # 判断计算结果是不是浮点数，需要保留几位
        if isinstance(result, float):
            # round()函数实现四舍五入，确定小数点位数
            result = round(result, 2)
        # 断言实际结果是否和预期结果相等
        assert result == expect
