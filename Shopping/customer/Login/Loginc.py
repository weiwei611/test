#!/usr/bin/env python
# coding=utf-8
# 登录系统
from Shopping.customer.register.zhucexitong import *

import json

def login():
    list1 = []
    list2 = []
    count = 0
    U = input("请输入用户名")
    with open("F:/PycharmProjects/Shopping/customer/register/register") as f:
        line = f.readlines()
        for i in line:
            i1 = json.loads(i)
            for i in i1:
                print(i)
                list1.append(i['username'])
                list2.append(i['pwd'])
            for i in list1:
                count += 1
                if i == U:
                    P = input("请输入密码")
                    if P == list2[count-1]:
                        print("登录成功")
                        exit(0)
                    else:
                        for i in range(3):
                            P1 = input("密码输入错误,请重新输入")
                            if P1 == list2[count-1]:
                                print("登录成功")
                                exit(0)
                            else:
                                pass
                    exit(0)

            else:
                Y = input("该用户名没有注册，进行注册“Y”")
                if Y == "Y".lower()[0] or "Y":
                    register()

#login()








