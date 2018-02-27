#-*- coding:utf-8 -*-
from PIL import Image

#验证码图片数量
imgNum = 1
#灰度阀值
threshold = 127
table = [0 if i < threshold else 1 for i in range(256)]
#图片信息
info = {
    "offsetWidth": 2,   #宽度偏移
    "offsetHeight": 4,  #高度偏移
    "wordNum": 4,       #字符数量
    "wordWidth": 12,    #字符宽度
    "wordHeight": 12,   #字符高度
    "wordSpace": -2     #字符空隙
}

for i in range(imgNum):
    im = Image.open("code/%s.jpg" % i)
    #分割单个字符
    for j in range(info['wordNum']):
        beginX = info['offsetWidth'] + (info['wordWidth'] + info['wordSpace']) * j
        beginY = info['offsetHeight']
        endX = beginX + info['wordWidth']
        endY = beginY + info['wordHeight']
        box = (beginX, beginY, endX, endY)
        im.crop(box).save('part/%s-%s.jpg' % (i,j))
