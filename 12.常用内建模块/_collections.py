#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
# 验证创建的Point对象是tuple的一种子类
print(type(p))
print(isinstance(p, Point))
print(isinstance(p, tuple))

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)

from collections import defaultdict

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

from collections import OrderedDict

d = dict([('a', 1), ('c', 3), ('b', 2)])
print(d)
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print(od)


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            # last = True 移除最后一个加入的键值对
            # last = False 移除第一个加入的键值对
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


fifoDict = LastUpdatedOrderedDict(3)
fifoDict['name'] = 'tengfei'
fifoDict['age'] = 20
fifoDict['tel'] = '123456'
fifoDict['city'] = 'hangzhou'
print(fifoDict)



from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。