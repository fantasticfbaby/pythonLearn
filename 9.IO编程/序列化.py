#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

d = dict(name='Frank', age=20, score=88)
print(pickle.dumps(d))  # 将d的内容转储

# 转储至文件
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

# 将转储的内容从文件中载入
with open('dump.txt', 'rb') as f:
    d = pickle.load(f)

print(d)

'''
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
'''

# 转JSON

import json

d = dict(name='Frank', age=20, score=88)
print(json.dumps(d))
print(type(json.dumps(d)))
'''
dumps()方法返回一个str，内容就是标准的JSON。
类似的，dump()方法可以直接把JSON写入一个file-like Object。
'''

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
print(type(json.loads(json_str)))

# 对象序列化
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


wang = Student('wang', 20)


def student2dict(std):
    return std.__dict__

# 无法直接将对象变成一个可序列为JSON的对象，需要写一个转换函数，再把函数传进去
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(wang, default=student2dict))

print(json.dumps(wang, default=lambda obj: obj.__dict__))