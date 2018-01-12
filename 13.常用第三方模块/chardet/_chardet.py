#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# chardet用来检测编码

import chardet

print(chardet.detect(b'hello world'))
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。

# 检测GBK编码的中文
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

# 对UTF-8编码进行检测
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))

# 对日文进行检测
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))

# 用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理