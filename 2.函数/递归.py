#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 直接上汉诺塔
count = 0


def hannuo(n, a, b, c):
    global count;
    if n == 1:
        print('%s -> %s' % (a, c))
        count += 1
    else:
        hannuo(n-1, a, c, b)
        print('%s -> %s' % (a, c))
        hannuo(n-1, b, a, c)
        count += 1

hannuo(3, 'A', 'B', 'C')
print(count)