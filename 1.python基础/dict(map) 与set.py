#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d ={'Michael':95, 'Bob':75, 'Tracy':85}
print(d)
print(d['Michael'])
d['Michael'] = 94
print(d['Michael'])
print('Thomas' in d) # 判断 Thomas是否在d中
print(d.get('Thomas'))
print(d.get('Thomas', -1))
d.pop('Bob')
print(d)

d['A']=1 # 插入方式一
print(d)
d.setdefault('B',2) # 插入方式二
print(d)

#遍历
print('遍历方式一：')
for key in d:
    print('key is %s, value is %s' % (key, d[key]))

print('遍历方式二：')
for key,value in d.items():
    print('key is %s, value is %s' % (key, value))


s = set([1,2,3]) # set创建
print(s)
s = set([1,1,2,2,2,3,3]) # 过滤
print(s)
s.add(4) # 追加
print(s)
s.remove(4) # 移除
print(s)
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2) # 求交
print(s1 | s2) # 求并

print('遍历set：')
for i in s:
    print(i)
