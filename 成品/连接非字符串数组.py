#!/usr/bin/env python3
# -*- coding: utf-8 -*-

li = [1,2,3,4,5]
print('-'.join(map(str, li)))
print('-'.join([str(x) for x in li]))
print('-'.join(x.__str__() for x in li))
print('-'.join(x.__repr__() for x in li))
