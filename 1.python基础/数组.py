#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[-1])  # 倒数第一个元素
classmates.append('Adam')  # 追加元素
print(classmates)
classmates.insert(1, 'Jack')  # 插入元素
print(classmates)
classmates.pop()  # 删除队尾元素
print(classmates)
classmates.pop(1)  # 删除指定位置元素
print(classmates)
print(classmates.index('Bob', 0, classmates.__len__()))  # 返回元素在列表中第一个下标，如果没有发现元素，抛出ValueError异常
li = [1, 1, 1, 2, 2, 2]
print(li.count(1))  # 返回指定元素在列表中的个数
li = [1, 2, 3, 4]
li.remove(2) # 移除列表中的第一个指定元素
print(li)
li.reverse() # 原地反转列表
print(li)
li = [3, 1, 3, 4, 2]
li.sort()
print(li)



print()
# 不可变数组,只是直接子元素不可变，间接子元素得看子元素是不是不可变数组

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
t = (1)  # 定义一个元素的错误方式
print(t)
t = (1,)  # 定义一个元素的正确方式
print(t)
