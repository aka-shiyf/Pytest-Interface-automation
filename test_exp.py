import pytest
import html


class TestClass:
    def setup(self):
        print("在每个用例执行前执行一次")

    def teardown(self):
        print("在每个用例执行后执行一次")

    def one(self):
        if 1 + 1 == 2:
            print("第一个用例")
        print("第一个用例")

    def two(self):
        a = 1
        b = 1
        assert a == b
        
# setup/teardown在每个用例前和之后执行一次
# setup_class/teardown_class 在每个类前/后执行一次


""""
a = 1
b = [2, 1, 3, 4, 5, 11]
c = 0
d = 1
e = None
assert bool(c) is False  # 断言布尔值c 为False
assert a in b  # 断言a在b里面
assert c not in b  # 断言c不在b里面
assert a == d  # 断言a等于b
assert a != c  # 断言a不等于b
assert a is not c  # 断言a等于c
assert e is None  # 断言e为空
assert a is not None  # 断言a不为空
print(a)
"""
