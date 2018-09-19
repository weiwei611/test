#!/usr/bin/env python
# coding=utf-8
import requests, json
from Day11.day11.com.gettoken import *
from configparser import ConfigParser
from wwjiekoukuangjia.com.request import *

conf = ConfigParser()
conf.read("../config/config.ini")
env = conf.get("env", "env")
if env == "pre":
    host = conf.get("pre", "host")
if env == "test":
    host = conf.get("test", "host")
#uuid, login_token = token()
#crmsessionid = get_session()


def request1(method, uri, body):
    # if header:
    #     header = json.loads(header)
    # else:
    #     header = None
    #body = body
    #body["crmsessionid"] = crmsessionid
    #body["login_token"] = login_token
    if method == "get":
        r = requests.get("http://%s%s" % (host, uri), params=body)
    if method == "post":
        r = requests.post("http://%s%s" % (host, uri), data=body)
        print(r.json())


method = "post"
uri = "/crm/login-step1"
body = {
        "name": "18888888888",
        "password": "MTIwMTEwMiAxMjAxMjAxIDEyMDIyMDIgMTIwMjEwMiAxMjAyMjEx"
    }
#header = None
request1(method, uri, body)



# def get_request(method, header, body):
# data = runExcel("../testcase/case1.xls")
# j = []
#     for i in range(len(data)):
#         host = get_host()
#         uri = data[i][1]
#         url = host + uri
#         # method = data[i][2]
#         # header = data[i][3]
#         # body = json.loads(data[i][4])
#         if "sessionid":
#             crmsessionid = get_session()
#             body['sessionid'] = crmsessionid
#         if header:
#             header = json.loads(header)
#         else:
#             header = None
#         if method == "get":
#             R = requests.get(url=url, params=body, headers=header)
#         else:
#             R = requests.post(url=url, data=body, headers=header)
#         j.append(R.json())
#     return j
#
#
# if __name__ == "__main__":
#     print(get_request())














