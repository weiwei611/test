# coding=utf-8
from wwjiekoukuangjia.testcase.r_excels import *
from wwjiekoukuangjia.testcase.w_excel import *
from wwjiekoukuangjia.com.get_url import *
from wwjiekoukuangjia.com.crmsessionid import *
import json, requests, xlrd


def get_request():
    data = runExcel("../testcase/case1.xls")
    j = []
    for i in range(len(data)):
        host = get_host()
        uri = data[i][1]
        url = host + uri
        method = data[i][2]
        header = data[i][3]
        body = json.loads(data[i][4])
        #print(type(body))
        if "sessionid":
            crmsessionid = get_session()
            body['sessionid'] = crmsessionid
        if header:
            header = json.loads(header)
        else:
            header = None
        if method == "get":
            R = requests.get(url=url, params=body, headers=header)
        else:
            R = requests.post(url=url, data=body, headers=header)
        j.append(R.json())
    return j


if __name__ == "__main__":
    print(get_request())














