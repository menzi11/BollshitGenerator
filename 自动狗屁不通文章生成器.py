#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

data = readJSON.读JSON文件("data.json")
data1 = readJSON.读JSON文件("famous.json")
名人名言 = data1['famous']
前面垫话 = data["before"]
后面垫话 = data['after']
废话 = data['bosh']
xx = data['title']
def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 另起一段():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            分支 = random.randint(0,100)
            if 分支 < 5:
                tmp += 另起一段()
            elif 分支 < 20 :
                tmp += 来点名人名言()
            else:
                tmp += next(下一句废话)
        tmp = tmp.replace("x",xx)
        print(tmp)