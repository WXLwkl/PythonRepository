#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/7.
#  Filename: use_PIL

from PIL import Image, ImageFilter
# 打开一个png图片文件，注意是当前路径
im = Image.open('cell的类型.png')
# 获取图片尺寸
w, h = im.size
print('Original image size: %s*%s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用png格式保存:
im.save('thumbnail.png', 'png')



# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('thumbnail.png')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('thumbnail1.png', 'png')

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
