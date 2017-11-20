#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'name : %s' % self.name
print(Student('teefing'))
#
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100:
#             raise StopIteration()
#         return self.a
#
# for n in Fib():
#     print(n)

class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            end = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(end):
                if x > start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib()
print(f[0:5])