#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 获得Unicode编码
print(ord('A'))
print(ord('中'))
# 获得Unicode对应的字符
print(chr(66))
print(chr(25991))
# 以十六进制输出字符
print('\u4e2d\u6587')

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))
