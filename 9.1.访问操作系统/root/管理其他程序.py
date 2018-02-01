#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess as sub
import os

print(sub.call(['ls']))  # 返回操作系统返回码
sub.call(['ls'], stdout=open('ls.txt', 'w'))
sub.call(['cmd', '/c', 'dir', '/b'], stdout=open('ls.txt', 'w'))
sub.call(['cmd', '/c', 'type', 'ls.txt'])
for line in open('ls.txt'):
    print(line)
print(os.startfile('ls.txt', 'open'))