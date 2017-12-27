#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('默认参数：')


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power(5))
print(power(5, 2))


def add_end(L=[]):
    L.append('End')
    return L


print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
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
        sum = sum + n * n
    return sum


print(calc())
print(calc(1, 2))
print('如果已有一个list或者tuple，要调用一个可变参数：')
nums = [1, 2, 3]
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
    print(type(city))
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

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。