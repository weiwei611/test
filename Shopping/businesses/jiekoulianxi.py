#!/usr/bin/env python
# coding=utf-8
import os
import time, json


def tradeget():
    L = []
    with open("../Shopping/customer/Login/price")as f:
        for i in f:
            m = json.loads(i)
            for i1 in m:
                L.append(i1["tradename"])
            return L


# print(tradeget())

def tradepostput(trade, price):
    count = 0
    trades = tradeget()
    d = {}
    with open("../Shopping/customer/Login/price")as f:
        for i in f:
            m = json.loads(i)
        if trade in trades:
            for i1 in trades:
                count += 1
                if i1 == trade:
                    break
            print(count)
            with open("../Shopping/customer/Login/price", 'w')as f:
                m[count - 1]['price'] = price
                m1 = json.dumps(m)
                f.write(m1)
            print(m)
        else:
            d["id"] = len(trades) + 1
            d["tradename"] = trade
            d["price"] = price
            m.append(d)
            print(m)
            with open("../Shopping/customer/Login/price", 'w')as f:
                m2=json.dumps(m)
                f.write(m2)

#tradepostput('banana', 2.5)

def tradedelete(trade):
    L=[]
    count=0
    trades = tradeget()
    with open("../Shopping/customer/Login/price")as f:
        for i in f:
            m = json.loads(i)
            for i1 in m:
                L.append(i1["tradename"])
    if trade in trades:
        for i1 in trades:
            count += 1
            if i1 == trade:
                del m[count-1]
        with open("../Shopping/customer/Login/price", 'w')as f:
            m3=json.dumps(m)
            f.write(m3)
    else:
        print("没有你要删除的水果")
        exit(0)

#trade = "pear"
#tradedelete(trade)

"""
def tradeput(trade, price):
    trades = tradeget()
    if trades.get(trade):
        trades[trade] = price
    else:
        pass
    with open("price1", "a")as f:
        for k, v in trades.items():
            f.write("|".join([str(k), str(v)]) + "\n")

    os.remove("price")
    time.sleep(3)
    os.rename("price1", "price")
"""







