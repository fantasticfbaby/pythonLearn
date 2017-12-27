#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('也可被next函数调用不断返回下一个值的对象成为迭代器：iterator')
from collections import Iterator
print('判断生成器是不是Iterator对象')
print(isinstance((x for x in range(10)), Iterator))
print()
print('判断list是不是Iterator对象')
print(isinstance([], Iterator))
print()
print('判断dict是不是Iterator对象')
print(isinstance({}, Iterator))
print()
print('判断tuple是不是Iterator对象')
print(isinstance((), Iterator))
print()
print('判断字符串是不是Iterator对象')
print(isinstance('abc', Iterator))
print()
print('把list,dict,str等Iterable变成Iterator，使用iter()')
print(isinstance(iter([]), Iterator))
print()

'''
为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的
'''
