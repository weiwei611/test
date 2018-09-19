import time, json,os


def tradeprice_1(trade):
    trades = []
    prices = []
    count = 0
    with open("price") as f:
        for _trade in f:
            m = json.loads(_trade)
        for i in m:
            trades.append(i['tradename'])
            prices.append(i['price'])

        for i in trades:
            count += 1
            if trade == i:
                return float(prices[count - 1])


# print(tradeprice_1('apple'))
def gettrade():
    with open("price") as f:
        for t in f:
            a = t.strip().split("|")
            # print(a)
            # return trades


def sumprice(trade, s, rate):
    price = tradeprice_1(trade)
    sum_ps = price * s * rate
    return sum_ps


# print(sumprice('pear', 2, 1))

def order_id(trade, name, region, ts):
    return "%s%s%s%d" % (trade[0], name[0], region[0], ts)


ts = time.time()


def order(trade, name, region, rate, s):
    price = tradeprice_1(trade)
    sum_ps = price * s * rate
    ts_s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    L = []
    d = {}
    d["orderid"] = order_id(trade, name, region, ts)
    d["customname"] = name
    d["tradename"] = trade
    d["reg"] = region
    d["ordertime"] = ts_s
    d["quantity"] = s
    d["totalprice"] = sum_ps
    #L.append(d)
    #print(L)
    return d
#order('apple', 'weiwei', 'beijing', 1,2)

def Writeorder(trade, name, region, rate,s):
    with open("order1") as f:
        line = f.readlines()
        for i in line:
            m = json.loads(i)
            #print(m)
            #print(order(trade, name, region, rate,s))
            m.append(order(trade, name, region, rate,s))
            with open("order2","a") as f:
                W = json.dumps(m)
                #print(W)
                f.write(W)
    os.remove("order1")
    os.rename("order2","order1")

#Writeorder('pear', 'weiwei', 'beijing', 1,1)




