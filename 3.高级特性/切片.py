#!/usr/bin/env python3
# -*- coding: utf-8 -*-
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('切片操作，从0开始取，到3为止，不包括3')
print(L[0:3])
print('同样支持倒着来')
print(L[-3:-1])

L = list(range(100))
print(L)
print('前十个数')
print(L[:10])
print()
print('第十一个数开始')
print(L[10:])
print()
print('后十个数')
print(L[-10:])
print()
print('11-20个数')
print(L[10:20])
print()
print('前十个数，每两个取一个')
print(L[:10:2])
print()
print('原样复制一个list')
print(L[:])
print()
print('tuple也可以切片操作，结果仍然是tuple')
print((0,1,2,3,4,5,6)[:3])
print()
print('字符串也可以切片操作，结果仍是字符串')
print('ABCDEFG'[:3])
print()
print('字符串逆置：')
print('ABCDEFG'[::-1])
print()