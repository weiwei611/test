#!/usr/bin/env python
# coding=utf-8
import random, string


def verification():
    chars = string.digits + string.ascii_letters
    chars = random.sample(chars, 6)
    i1 = "".join(chars)
    print(i1)
    print("请输入6位的验证码")
    a = input()
    if a == i1:
        print("注册成功")
        exit(0)

    else:
        print("验证码错误请重新输入")
        verification()
