#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

str = 'abcdefg'

print(str*2)

str = 'abcdedefg'
print(str.count('de', 0, str.__len__() - 1))
str = 'abcdefg'

print(str.endswith('fg'))
print(str.find('de'))

# format
print('my name is {}, age is {}'.format(
    'tengfei',
    18
))
print('my name is {0}, age is {1}'.format(
    'tengfei',
    18
))
print('my name is {1}, age is {0}'.format(
    'tengfei',
    18
))
li = ['tengfei', 18]
print('my name is {0}, age is {1}'.format(*li))

hash = {'name': 'tengfei', 'age': 18}
print('my name is {name}, age is {age}'.format(name='tengfei', age=18))
print('my name is {name}, age is {age}'.format(**hash))

print('{0:*>10}'.format(10))
print('{0:?<10}'.format(10))
print('{0:@^10}'.format(10))

print('{0:.2f}'.format(1 / 3))
print('{0:b},{1:b}'.format(10, 20))
print('{0:o}'.format(10))
print('{0:x}'.format(10))
print('{:,}'.format(123456789))

print('my name is {0[0]}, age is {0[1]}'.format(li))

print(','.join(list(['1','1','1'])))
print(str.ljust(10,'*'))
print(str.rjust(10,'&'))
print(str.center(10, '*'))

print('    abc   '.strip())
print('    abc   '.lstrip())
print('    abc   '.rstrip())
print("a,b,c".partition(','))
print("a,b,c".split(','))
print('adfadsfs\nasdfs'.splitlines())
print('adfadsfs\nasdfs'.splitlines(keepends=True))
print("a is b".title())
print("a is b".capitalize())

