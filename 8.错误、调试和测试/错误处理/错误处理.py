#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0') # 所调用的内部函数出错，错误也会传出到外部函数
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')
#
# main()

from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()