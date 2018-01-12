#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools, time

# itertools提供的几个“无限”迭代器
naturals = itertools.count(1) # 参数表示从多少开始计数，默认是0，
# for n in naturals:
#     print(n)
#     time.sleep(1)

# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)
#     time.sleep(1)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
naturals = itertools.count()
ns = itertools.takewhile(lambda x: x <= 10, naturals)
# print(list(ns))

# itertools提供的几个迭代器操作函数更加有用

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)


# groupby()把迭代器中相邻的重复元素挑出来放在一起
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))

#实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
# 而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
for key, group in itertools.groupby('aAAbBBcCAAA', lambda c: c.upper()):
    print(key, list(group))


# 练习，计算圆周率
def pi(N):
    # 计算pi的值
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_list = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x<=2*N-1, odd_list)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: 求和:
    _sum = 0
    a = 4
    for i in ns:
        _sum = _sum + a / i
        a = -a
    return _sum

# 优化
def pi2(N):
    loop4 = itertools.cycle([4, -4])
    odd_list = itertools.count(1, 2)
    return sum([next(loop4)/next(odd_list) for i in range(N)])

# 测试:
print(pi2(10))
print(pi2(100))
print(pi2(1000))
print(pi2(10000))
assert 3.04 < pi2(10) < 3.05
assert 3.13 < pi2(100) < 3.14
assert 3.140 < pi2(1000) < 3.141
assert 3.1414 < pi2(10000) < 3.1415
print('ok')