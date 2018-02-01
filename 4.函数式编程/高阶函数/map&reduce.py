#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('map')
def f(x):
    return x * x
# 这里必须调用list，py3中map返回的是一个Iterator，只有真正去调用它才会去实现map内部代码
print(list(map(f, [1,2,3,4,5,6,7,8,9])))
print()
print('把list看所有数字转为字符串')
print(list(map(str, [1,2,3,4,5,6,7,8,9])))
print()
print('reduce')
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1,3,5,7,9]))
print('把序列【1,2,3,4,5】变成整数13579')
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1,3,5,7,9]))
print()
print('str2int')
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn, map(char2num, '13579')))
print()

print('整理')
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print(str2int('13579'))
print()

print('用lambda函数进一步简化')
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('13579'))
print()

print('利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字')
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
print()

print('Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积')
def prod(L):
    def mul(x, y):
        return x * y
    return reduce(mul, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
print()

print('利用map和reduce编写一个str2float函数，把字符串\'123.456\'转换成浮点数123.456：')
def str2float(s):
    M = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
    def char2num(s):
        return M[s]
    a = list(map(char2num, s))
    n = a.index('.')
    beforeDot = a[:n]
    afterDot = a[n+1:]
    afterDot.reverse()
    afterDot = afterDot + [0]
    def fn(x, y):
        return x * 10 + y
    def fn2(x, y):
        return x * 0.1 + y
    return reduce(fn, beforeDot) + reduce(fn2, afterDot)


print('str2float(\'123.456\') =', str2float('123.456'))