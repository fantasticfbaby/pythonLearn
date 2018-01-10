#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))
if re.match(r'^\d{3}-\d{3,8}$', '010-12345'):
    print('OK')
else:
    print('ERROR')

print('!!!!!!!!!!!!!!')
# 切分字符串
print(re.split(r'[\s,;]+','a, b ;;c   d'))
print('@@@@@@@@@@@@@@@')
# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())
'''
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。
如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。

注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
'''
print('#################')

# 贪婪匹配
#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
print(re.match(r'^(\d+)(0*)$', '102300').groups())
'''
由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。

必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
'''
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
print('$$$$$$$$$$$$$$$$$$$')
# 编译优化
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print('%%%%%%%%%%%%%%%%%')

