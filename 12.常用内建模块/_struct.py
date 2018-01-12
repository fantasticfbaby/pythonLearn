#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct, base64

# struct模块来解决bytes和其他二进制数据类型的转换

# struct的pack函数把任意数据类型变成bytes：
print(struct.pack('>I', 10240099))  # 把一个32位无符号整数变成字节
'''
pack的第一个参数是处理指令，'>I'的意思是：

>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

后面的参数个数要和处理指令一致。
'''

# unpack把bytes变成相应的数据类型：
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。

# bmp图片分析

bmp_data = base64.b64decode(
    'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

print('bmp图片分析')
'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
'''

def bmp_info(data):
        bmpData = struct.unpack('<ccIIIIIIHH', data[:30])
        if bmpData[0] == b'B' and (bmpData[1] == b'M' or bmpData[1] == b'A'):
            return {
                'width': bmpData[-4],
                'height': bmpData[-3],
                'color': bmpData[-1]
            }
        else:
            return '''It's not a bmp'''


bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

with open('test.bmp', 'rb') as f:
    data = f.read(30)
    bmpData = struct.unpack('<ccIIIIIIHH', data[:30])
    if bmpData[0] == b'B' and (bmpData[1] == b'M' or bmpData[1] == b'A'):
        print('size:', bmpData[2])
        print('width:', bmpData[-4])
        print('height:', bmpData[-3])
        print('color:', bmpData[-1])
    else:
        print("It's not a bmp")
