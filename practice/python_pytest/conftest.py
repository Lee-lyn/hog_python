from typing import List

import pytest
from _pytest.config import Config

from practice.python_pytest.calc import Calculator


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

