#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

t = triangles()
for i in range(10):
    print(t.__next__())