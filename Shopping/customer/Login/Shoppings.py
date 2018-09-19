#!/usr/bin/env python
# coding=utf-8

from Shopping.customer.Login.shappingorder import *
from Shopping.customer.register.zhucexitong import *

def shopping():
    rate = 1
    name = "xiaoming"
    region = "beijing"
    trades = []

    # 商品的数量
    counts = 3
    sum = 0

    print("欢迎前来购物\n")


    def er(counts, sum):
        count = 0
        with open("price")as f:
            for _trade in f:
                list=json.loads(_trade)
                print(list)
                for i in list:
                    trades.append(i['tradename'])
                print(trades)
        trade = input("请输入您购买的商品\n")
        if trade in trades:
            pass
        else:
            print("请输入已有的商品")
            er(counts, sum)

        n = input("请输入您购买的斤数\n")
        s = int(n)

        print("此商品的总价格是" + str(sumprice(trade, s, rate)))


        a = input("是否购买---是输入‘Y’,否输入'N'\n")

        if a == "Y".lower()[0]:
            print("订单=" + str(order(trade, name, region, rate, s)))
            print("此商品的总价格是" + str(sumprice(trade, s, rate)))
            Writeorder(trade, name, region, rate,s)
        else:
            print("欢迎下次光临")
            exit(0)
        b = input("是否继续购买---是输入‘Y’,否输入'N'\n")
        if b == "Y".lower()[0]:
            er(counts, sum)
        else:
            print("欢迎下次光临")
            exit(0)
    er(counts, sum)

shopping()






