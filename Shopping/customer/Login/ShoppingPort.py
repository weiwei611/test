
#!/usr/bin/env python
# coding=utf-8
import os
import time


def tradeget():
    with open("price")as f:
        trades = {}
        for i in f:
            _trade = i.strip().split("|")
            trades[_trade[0].strip()] = float(_trade[1].strip())
        return trades


def tradepost(trade, price):
    trades = tradeget()
    if trades.get(trade):
        pass
    else:
        with open("price", "a") as f:
            f.write("|".join([trade, str(price)]) + "\n")


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


def tradedelete(trade):
    trades = tradeget()
    if trades.get(trade):
        del trades[trade]

    else:
        pass
    print(trades)
    with open("price1", "a")as f:
        for k, v in trades.items():
            f.write("|".join([str(k), str(v)]) + "\n")

    os.remove("price")
    time.sleep(3)
    os.rename("price1", "price")


trade = "pear"
tradedelete(trade)



