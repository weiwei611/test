#!/usr/bin/env python
# coding=utf-8
import json,os


def password():
    P = input("请输入注册密码")
    if 8 <= len(P) <= 20 and P[0].isalpha():
        P1 = input("请再次输入注册密码")
        if P == P1:
            with open("register")as f:
                line = f.readlines()
            for i in line:
                m = json.loads(i)
                m[len(m) - 1]["pwd"] = P1
                print(m)
                with open("register1", "a")as f:
                    m1 = json.dumps(m)
                    f.write(m1)
            os.remove("register")
            os.rename("register1", "register")

    else:
        print("密码非法请重新输入")
        password()


#password()
