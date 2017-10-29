#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('函数也是一个对象，函数对象有一个__name__属性，可以拿到函数名字：')

def my_function():
    print('this is my function')
    return

print(my_function.__name__)
print()
print('在代码运行期间动态增加功能, 装饰器,本质上，decorator就是一个返回函数的高阶函数')
def log(func):
    def wrap(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrap
log(my_function)()
@log
def now():
    print('2017-1-1')
print(now())
# 等同于now = log(now)

print()
print('decorator本身需要传入参数')
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('excute')
def now():
    print('2017-1-1')
print(now())
# 等同于now = log('excute')(now)
print()
print('但是now的name属性已经发生了更改')
print(now.__name__)
print()
print('使用functools.wraps解决')
print('针对不带参数的decorator：')
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

print('针对带参数的decorator：')
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
print()
print('一个既支持传参又支持不传参的decorator：')
def log(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kwargs):
            print('call %s():' % text.__name__)
            return text(*args, **kwargs)
        return wrapper
@log
def now():
    print('2017-1-1')
print(now())
@log('excute')
def now():
    print('2017-1-1')
print(now())