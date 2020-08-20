from typing import List

from _pytest.config import Config

import os

import pytest
import yaml

from practice.python_pytest.calc import Calculator

a = os.path.dirname(__file__) + "/datas/hw1_calc.yml"
# 创建yaml文件并打开
with open(a, encoding="utf-8") as f:
    datas = yaml.safe_load(f)['datas']
    add_data = datas['add_data']
    sub_data = datas['sub_data']
    mul_data = datas['mul_data']
    div_data = datas['div_data']
    add_id = datas['add_id']
    sub_id = datas['sub_id']
    mul_id = datas['mul_id']
    div_id = datas['div_id']


# 创建fixture，实例化计算器，实现在每个测试用例开始前输出’开始计算‘，测试用例结束后输出’结束计算‘
@pytest.fixture()
def get_calc():
    calc = Calculator()
    print("开始计算")
    yield calc
    print("结束计算")

# 创建fixture，获取加法数据，并为测试用例设置别名
@pytest.fixture(params=add_data, ids=add_id)
def get_add_data(request):
    add_data = request.param
    return add_data


# 创建fixture，获取减法数据，并为测试用例设置别名
@pytest.fixture(params=sub_data, ids=sub_id)
def get_sub_data(request):
    sub_data = request.param
    return sub_data


# 创建fixture，获取乘法数据，并为测试用例设置别名
@pytest.fixture(params=mul_data, ids=mul_id)
def get_mul_data(request):
    mul_data = request.param
    return mul_data


# 创建fixture，获取除法数据，并为测试用例设置别名
@pytest.fixture(params=div_data, ids=div_id)
def get_div_data(request):
    div_data = request.param
    return div_data


@pytest.fixture(scope='module')
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")


@pytest.fixture(scope='class')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


# hook 函数改写
# 如果不改写，它会按照pytest默认的规则去运行测试用例
# 如果在conftest.py 文件里定义这些hook函数，名字和参数要与官网一致
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param _pytest.main.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[_pytest.nodes.Item] items: List of item objects.
    """
    print("items")
    print(items)
    # reverse 翻转执行顺序
    # items.reverse()
    for item in items:
        # 测试用例参数的编码格式改写
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # # 如果测试用例里面有xxx字符，则自动添加一些标签，运行时可以直接按标签运行
        # if 'add' in item.nodeid:
        #     item.add_marker(pytest.mark.add)
        #
        # elif 'div' in item.nodeid:
        #     item.add_marker(pytest.mark.div)
        #
        # elif 'sub' in item.nodeid:
        #     item.add_marker(pytest.mark.sub)
        #
        # elif 'mul' in item.nodeid:
        #     item.add_marker(pytest.mark.mul)

# 注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
# env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
# parser：用户命令行参数与ini文件值的解析器
def pytest_addoption(parser):
    mygroup=parser.getgroup("hogwarts")        # group 将下面所有的option都展示在这个group下
    mygroup.addoption("--env",                 # 注册一个命令行选项
                      default='test',          # 默认值
                      dest='dev'or'st',        # 存储的变量
                      help='set your run env'  # 参数说明
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env",default='test')