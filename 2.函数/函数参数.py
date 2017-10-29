#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('默认参数：')
def power(x , n=2):
    s = 1
    while n > 0:
        n-=1
        s=s*x
    return s
print(power(5))
print(power(5,2))

def add_end(L=[]):
    L.append('End')
    return L
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())
print(add_end())
print('所以默认参数必须指向不变对象')
print('优化：')
def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L
print(add_end())
print(add_end())
print(add_end())

print('可变参数：')
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc())
print(calc(1,2))
print('如果已有一个list或者tuple，要调用一个可变参数：')
nums = [1,2,3]
print(calc(*nums))
print('*nums表示把nums这个list的所有元素作为可变参数传入')

print('关键字参数:')
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

print('命名关键字参数：')
def person(name, age, *, city, job):
    print(name, age, city, job)
person('a', 2, city='a', job='a')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('a', 2, city='a', job='a')
person('a', 2, 2, 3, 4, city='a', job='a')

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('a', 2, job='a')

print('参数组合：')
# 用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

