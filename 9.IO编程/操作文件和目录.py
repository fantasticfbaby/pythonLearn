#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)

# 操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)

# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))
# for path in os.environ.get('PATH').split(';'):
#     print(path)

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 得到当前工作目录，即当前Python脚本工作的目录路径:
print(os.getcwd())

# 返回指定目录下的所有文件和目录名
print(os.listdir('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
newPath = os.path.join(os.path.abspath('.'), 'testidr')
print(newPath)
# 然后创建一个目录:如果不存在该目录则创建，存在不创建
if os.path.exists(newPath):
    print('已存在新目录')
    pass
else:
    os.mkdir(newPath)
    print('目录创建成功')

# # 设置一定时间延迟
# time.sleep(2)
# # 删掉一个目录:
os.rmdir(newPath)

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split(newPath))

# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

# 创建空文件
f = open('1.txt', 'w')
print('已创文件')
f.close()

# 对文件重命名:
os.rename('1.txt', '2.txt')
print('已重命名')

# 删掉文件:
os.remove('2.txt')
print('已删除文件')

# 复制文件
import shutil
shutil.copyfile('test.txt', 'testcopy.txt')
print('已复制文件')
os.remove('testcopy.txt')

# 列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])