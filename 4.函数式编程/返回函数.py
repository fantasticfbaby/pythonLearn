#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('闭包')
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
print('无法得出正确结果')
print()
print('正确结果')
def count():
    fs = []
    def f(j):
        def g():
            return j * j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

f = sum([1,2,3])
print(f)