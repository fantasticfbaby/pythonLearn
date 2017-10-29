#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('匿名函数基础用法：')
print(list(map(lambda x: x * x, [1,2,3,4,5,6,7,8,9])))
print()
print('匿名函数赋值给一个变量，再利用变量来调用该函数：')
f = lambda x: x * x
print(f)
print(f(5))
print()
print('可以把匿名函数作为返回值返回：')
def build(x, y):
    return lambda:x * x + y * y
print(build(1,2)())