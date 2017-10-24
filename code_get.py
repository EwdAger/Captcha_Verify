#-*- coding:utf-8 -*-
import requests

imgNum = 100

cookies = requests.get('http://kdjw.hnust.cn/kdjw/verifycode.servlet').cookies
for i in range(imgNum):
    img = requests.get('http://kdjw.hnust.cn/kdjw/verifycode.servlet', cookies=cookies).content
    with open('code/%s.bmp' % i, 'wb') as f:
        f.write(img)
