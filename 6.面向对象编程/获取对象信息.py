#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(type(123))
print(type('str'))
print(type(None))

print(type(123) == type(456))
print(type(123) == type('123'))
print(type(123) == int)
import types


def fn():
    return


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
print(type(abs) == types.FunctionType)
print(type(abs) == types.BuiltinMethodType)


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1

s1 = Student('1')
s2 = Student('2')
s3 = Student('3')
print(Student.count)
