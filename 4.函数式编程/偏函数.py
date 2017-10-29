#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('偏函数作用：通过设定参数的默认值，可以降低函数调用的难度')
import functools
int2 = functools.partial(int, base =2)
print(int2('100000'))

print('相当于：')
kw = {'base': 2}
print(int('100000', **kw))
print()
print('当传入：')
max2= functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
print(max2(5,6,7))
#相当于：
args = (10, 5, 6, 7)
print(max(*args))
