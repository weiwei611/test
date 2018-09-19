# coding=utf-8
from xlwt import *
from wwjiekoukuangjia.com.request import *
from xlutils.copy import copy
import xlrd, json


def reexcel():
    rb = xlrd.open_workbook("../testcase/case1.xls")
    wb = copy(rb)
    j = get_request()
    for i in range(len(j)):
        a = json.dumps(j[i])
        sheet = wb.get_sheet(0)
        sheet.write(i + 1, 7, a)
    wb.save("../testcase/case.xls")
    return j

if __name__ == "__main__":
    print(reexcel())