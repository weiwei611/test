#!/usr/bin/env python
# coding=utf-8
import json
L=[]
L1=[]
with open("F:/PycharmProjects/Shopping/customer/Login/order1") as f:
    for i in f:
        m=json.loads(i)
        print(m)
        for i in m:
            print(i)
            if i["customname"] not in L:
                L.append(i["customname"])

            if i["tradename"] not in L1:
                L1.append(i["tradename"])
        print(L1)

