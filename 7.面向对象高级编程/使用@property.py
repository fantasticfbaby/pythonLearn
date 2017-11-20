#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student(object):
# def get_score(self):
#     return self._score
#
# def set_score(self, value):
#     if not isinstance(value, int):
#         raise ValueError('score must be an integer!')
#     if value < 0 or value > 100:
#         raise ValueError('score must between 0 - 100')
#     self._score = value

class Student(object):
    @property
    def score(self):
        return self.__score # 不能写self.score 不然会循环调用

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100')
        self.__score = value

s = Student()
s.score = 100
print(s.score)
print(s._Student__score)
s.__score = 200
print(s.score)
for item in dir(s):
    print(item)

