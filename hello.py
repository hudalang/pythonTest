#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from multiprocessing import Process

from urllib import request


# 定义函数
def test(x):
    if isinstance(x, int) and int(x) > 0:
        return True
    else:
        return 'x', 'y'


# 条件语句
if 1 > 0:
    print(True)
else:
    print(False)
print(10 // 3)  # 地板除法
# 字符串格式化
print('%s,%s' % ('acd', "a"))
# 列表
namelist = ['a', 'b', 'dalang']
namelist.insert(len(namelist), 'sdsfdasf')
print(namelist[-1])
sumTemp = 0
num = 0
# for num in range(1,101,5):
# 	sum += num;
numList = range(1, 101, 5)

# 循环结构
while num < len(numList):
    sumTemp += numList[num]
    num = num + 1
print(sum)
print(min(namelist))
print(test(-1))

print(math.sin(30))


class Abc(object):
    @property
    def birth(self):
        return self._brith

    @birth.setter
    def birth(self, value):
        self._birth = value

    """测试类的定义和使用"""

    def __init__(self, arg):
        self.__arg = arg

    def get_arg(self):
        return self.__arg


a = abc("abc")
a.birth = 50;
print(a.brith)


def run(name):
    print(name, 'run Process.....')


if __name__ == '__main__':

    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print(k, v)
        print('Data:', data.decode('utf-8'))

    p = Process(target=run, args=('dalang',))
    p.start()
