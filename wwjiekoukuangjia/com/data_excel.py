from wwjiekoukuangjia.testcase.r_excels import *
import json


def date_excel():
    L = []
    data = runExcel("../testcase/case.xls")
    for i in range(len(data)):
        L.append(json.loads(data[i][5]))
    return L

if __name__ == "__main__":
    print(date_excel())