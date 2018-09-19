#!/usr/bin/env python
# coding=utf-8
import json, os


def phone():
    m = []
    x = {}
    n1 = []
    count = 1
    H = input("请输入用户名----手机号")
    a = ['135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '187', '188', '153']
    if len(H) == 11 and H.isdigit() and H[:3] in a:
        with open('F:/PycharmProjects/Shopping/customer/register/register') as f:
            line = f.readlines()
        for i in line:
            m = json.loads(i)
            for i in m:
                count += 1
                n1.append(i['username'])
            if H in n1:
                h = input("该手机号已经注册完毕，想重新注册'y'")
                if h == "Y".lower()[0] or "Y":
                    phone()
                else:
                    exit(0)

        with open('register1', 'a') as f:
            x['id'] = count
            x['username'] = H
            m.append(x)
            m2 = json.dumps(m)
            f.write(m2)
            print(m2)
        os.remove("register")
        os.rename("register1", "register")

    else:
        print("号码非法请重新输入")
        phone()


#phone()


