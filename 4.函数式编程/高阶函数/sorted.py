#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('sorted')
print(sorted([36, 5, -12, 9, -21]))
print()
print('sorted accept key of abs to sort:')
print(sorted([36, 5, -12, 9, -21], key=abs))
print()
print('string sort')
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print()
print('ignore case to sort')
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print()
print('reverse to sort')
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
print()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print('用sorted()对上述列表分别按名字排序')
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)
print()
print('再按成绩从高到低排序：')
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)
