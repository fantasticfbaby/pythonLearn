#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    __slots__ = ('name', 'age','set_age','score')
s = Student()
s.name = 'Teefing'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

def set_score(self, score):
    self.score = score
Student.set_score = set_score
s.set_score(100)
print(s.score)

print(dir(s))
