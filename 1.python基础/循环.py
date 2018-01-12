#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# for
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
print(list(range(5)))
sum = 0
for x in range(101):
    sum += x
print(sum)

# while
sum = 0
n = 100
while n > 0:
    sum+=n;
    n-=1;
print(sum)

# break同C语言，同理还有continue，同C语言
n=1
while n<=100:
    if n>10:
        break
    print(n)
    n+=1
print('END')
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('Hello, %s!' % i)

# enumerate
for number, line in enumerate(open('helloworld.py')):
    print(number, '\t', line)

for number, line in enumerate(open('helloworld.py'), 1):
    print(number, '\t', line)