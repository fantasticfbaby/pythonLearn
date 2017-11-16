#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 标准注释，第一行可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码

# 模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
' a text module'

# 特殊变量，有特殊用途，可以被直接引用，这里把作者写进去当公开源代码后别人可以瞻仰大名
__author__ = 'Teefing'


# 使用sys模块的第一步，导入sys模块
import sys

def test():
    # sys模块有一个argv变量，用list存储了命令行所有的参数。
    # 它至少有一个参数，即文件名本身
    args = sys.argv
    if len(args) == 1:
        print('hello, world!')
    elif len(args) == 2:
        print('hello, %s' % args[1])
    else:
        print('too many arguments!')

# 当一个module作为整体被执行，即是主程序的时候，__name__的值是__main__，如果一个module被其他module引用，__name__将是module自己的名字
# 用来测试再合适不过
if __name__ == '__main__':
    test()
