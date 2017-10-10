#-*- coding:utf-8 -*-

import os
from PIL import Image
import json

#验证码图片数量
imgNum = 100
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

keys = {}
path = "part/"
folders = [x for x in os.listdir(path) if os.path.isdir(path + x)]
for key in folders:
    imgFlag = []
    tmpPath = path + key + '/'
    files = [tmpPath + x for x in os.listdir(tmpPath) if os.path.isfile(tmpPath + x)]
    for img in files:
        im = Image.open(img).convert('L')
        im = im.point(table, '1')
        imgData = ''.join(str(x) for x in list(im.getdata()))
    for i in range(len(imgData)):
        if(len(imgFlag) <= i):
            imgFlag.append([0, 0])
        imgFlag[i][int(imgData[i])] += 1
    keys[key] = ''.join('0' if flag[0] > flag[1] else '1' for flag in imgFlag)
print json.dumps(keys, indent=2)

