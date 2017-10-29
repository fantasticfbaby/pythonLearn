#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('filter:')
print('保留奇数')
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1,2,3,4,5,6,7])))
print()
print('删除空字符串')
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))
print()
print('用filter求素数')
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 100:
        print(n)
    else:
        break
print()
print('过滤非回数：')
def is_palindrome(n):
    # return n and list(str(n)) == list(reversed(str(n)))
    return n and str(n) == str(n)[::-1]
output = filter(is_palindrome, range(100, 200))
print(list(output))
