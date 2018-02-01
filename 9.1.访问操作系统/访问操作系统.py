#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import pprint
import json

print('balabala')
print()
print()  # 换行

print('获取文件系统编码')
print(sys.getfilesystemencoding())
print()  # 换行

print('获取用户名')
print(os.getlogin())
print()  # 换行

print('查看用户掩码')
origin = os.umask(0b111111111)  # 设置新的掩码并返回旧的掩码
print(bin(origin))
os.umask(origin)  # 将掩码设置为初始值
print()  # 换行

print('操作系统名称, 常用')
print(os.name)
print()  # 换行

print('操作系统平台')
print(sys.platform)
print()  # 换行

print('终端模拟器大小')
print(shutil.get_terminal_size())
print()  # 换行

print('获取当前进程ID')
print(os.getpid())
print()  # 换行

print('获取父进程ID,本例中是操作系统shell')
print(os.getppid())
print()  # 换行

print('当前工作目录')
print(os.getcwd())
print()  # 换行

print('环境变量')
print(os.environ)
print()  # 换行



