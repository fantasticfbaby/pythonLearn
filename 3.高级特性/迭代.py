#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()。

from collections import Iterable
print('判断字符串是否可以迭代')
print(isinstance('abc', Iterable))
print()
print('判断list是否可以迭代')
print(isinstance([1,2,3], Iterable))
print()
print('判断整数是否可以迭代')
print(isinstance(12, Iterable))
print()
print('使用enumerate函数把一个list变成索引-元素对')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print()

