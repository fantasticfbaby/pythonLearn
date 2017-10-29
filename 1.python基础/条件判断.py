#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('you age is', age)
    print('kid')

if [1]:
    print('not none')

height = 1.75
weight = 80.5
bmi = 80.5 / (1.75 * 1.75)
if bmi < 18.5:
    print('过轻：%.2f' % bmi)
elif bmi < 25 and bmi >= 18.5:
    print('正常：%.2f' % bmi)
elif bmi < 28 and bmi >= 25:
    print('过重：%.2f' % bmi)
elif bmi < 32 and bmi >= 28:
    print('肥胖：%.2f' % bmi)
else:
    print('严重肥胖：%.2f' % bmi)
