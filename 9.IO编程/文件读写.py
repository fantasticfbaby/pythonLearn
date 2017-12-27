#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt

try:  # 一次性读写
    f = open('test.txt', 'r', encoding='gbk', errors='ignore')  # 强行忽略字符编码问题
    print(f.read())
finally:
    if f:
        f.close()

with open('test.txt', 'r', encoding='utf-8') as f:  # 简写
    print(f.read())

with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())  # 删掉末尾的\n

with open('test.txt', 'rb') as f:
    print(f.read())


f = open('test.txt', 'w')
f.write('hello')
f.close()

with open('test.txt', 'w') as f:
    f.write('hello\rhello')

with open('test.txt') as f: # 把hello替换成bye
    x = f.readlines()
    with open('test.txt', 'w'): pass
    for i in x:
        s = i.replace('hello', 'bye')
        with open('test.txt', 'a') as f:
            f.write(s)
