#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('generator')
g = (x * x for x in range(10))
print('无法直接输出')
print(g)
print('笨的输出方法')
print(next(g))
print(next(g))
print('generator是可迭代对象，可以使用for输出')
for n in g:
    print(n)
print()
print('斐波那契数列')
print('函数中包含yield关键字，这个函数就是一个generator')
print('执行流程是每次调用next的时候执行，遇到yield返回，再次执行时从上次返回的yield从继续执行')

def fib(max):
    n, a, b = 0, 0, 1 # 很方便有没有
    while n < max:
        yield b
        a,b = b,a+b
        n+=1
    return 'done'

print(fib(6))
for n in fib(6):
    print(n)

print()
print('想要拿到generator的return语句返回值，要捕获StopIteration错误')
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print()
print('杨辉三角')
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n+=1
    if n == 10:
        break