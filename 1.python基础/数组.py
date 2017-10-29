#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[-1]) # 倒数第一个元素
classmates.append('Adam') # 追加元素
print(classmates)
classmates.insert(1, 'Jack') # 插入元素
print(classmates)
classmates.pop() # 删除队尾元素
print(classmates)
classmates.pop(1) # 删除指定位置元素
print(classmates)

# 不可变数组,只是直接子元素不可变，间接子元素得看子元素是不是不可变数组

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
t = (1) # 定义一个元素的错误方式
print(t)
t = (1,) # 定义一个元素的正确方式
print(t)
