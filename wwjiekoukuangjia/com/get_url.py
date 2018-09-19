from wwjiekoukuangjia.com.get_host import *
from wwjiekoukuangjia.testcase.r_excels import *

def get_excution():
    x = (runExcel("../testcase/case1.xls"))
    url = []
    for i in range(len(x)):
        ip = get_host()
        uri = x[i][3]
        url.append(ip+uri)
    return url

if __name__ == "__main__":
    print(get_excution())