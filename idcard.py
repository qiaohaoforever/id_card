#!/usr/bin/python
#-*-coding:utf-8-*-
import json

locate_dic = {}
for line in open("./ID/ID.csv", "r"):
    idcard = line.strip("\r\n").split(",", 1)
    locate_dic[idcard[0]] = idcard[1]

def find(idcard):
    dict = {}
    if len(idcard) == 15:
        idcard = idcard[:6] + "19" + idcard[6:]
    dict['locate'] = locate_dic[idcard[:6]]
    dict['birthday'] = idcard[6:14]
    if int(idcard[16])%2 == 0:
        dict['gender'] = '女'
    else:
        dict['gender'] = "男"
    j = json.dumps(dict)
    return j
