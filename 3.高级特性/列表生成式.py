#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('基础列表生成式')
print([x * x for x in range(1, 11)])
print()
print('加上判断')
print([x * x for x in range(1, 11) if x % 2 == 0])
print()
print('使用两重循环生成全排列')
print([m+n for m in 'ABC' for n in 'XYZ'])
print()
print('列出当前目录下所有文件和目录名')
import os
print([d for d in os.listdir('.')])
print()
print('使用两个变量来生成list')
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k,v in d.items()])
print()
print('把list中所有字符串变成小写')
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print()
print('练习')
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])
print([s.lower() if isinstance(s, str) else s for s in L1])
