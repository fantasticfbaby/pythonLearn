#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 要想使用with xxxx() as x:     这种格式， 可以用@contextmanager 装饰一个生成器xxxx() 这个生成器里包含相关的上下文处理
# 在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现

from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self._name = name

    def query(self):
        print('Query info about %s...' % self._name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('tengfei') as q:
    q.query()

@contextmanager
def tag(name):
    print('<%s>' % name, end='')
    yield
    print('<%s>' % name)

with tag('h1'):
    print('hello world', end='')

'''
代码的执行顺序是：

with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理。
'''


# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)