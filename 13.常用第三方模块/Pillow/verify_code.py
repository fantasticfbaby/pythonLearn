#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

# 随机字母:
def rndChar(num):
    return random.sample(string.ascii_uppercase + string.digits, num)


def create_verify_code(rndList):

    # 随机颜色1:
    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


    # 随机颜色2:
    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建Font对象:
    font = ImageFont.truetype('arial.ttf', 36)

    # 创建Draw对象:
    draw = ImageDraw.Draw(image)

    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    # 输出文字:
    for i in range(4):
        draw.text((60 * i + 10, 10), rndList[i], font=font, fill=rndColor2())

    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')

if __name__ == '__main__':

    rndList = rndChar(4)
    create_verify_code(rndList)