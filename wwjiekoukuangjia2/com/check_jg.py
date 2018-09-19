from wwjiekoukuangjia.testcase.w_excel import *
from wwjiekoukuangjia.com.data_excel import *
from wwjiekoukuangjia.com.checkdata import *
import allure



#@pytest.mark.parametrize("_,testcase,method,uri,header,body,exception", data)

    #allure.attach("测试用例", testcase)

R = reexcel()
E = date_excel()
print(R)
print(E)
for i in range(len(E)):
    response = E[i]
    expect = R[i]
    #print(test_check(response, expect))

# os.system("pytest check_jg.py --alluredir allure-report")
# os.system("allure serve allure-report")



    # address = readConfig("config/config.ini", "excel", "address")
    # # ticket = readConfig("config/config.ini","ticket","ticket")
    # caseList = getCaseInfo(address)
    # @pytest.mark.parametrize("url,header,body,method,expect", caseList)
    # def test_main(url, header, body, method, expect):
    # if header:
    # header = json.loads(header)
    # else:
    # header = None
    # if body:
    # body = json.loads(body)
    # else:
    # body = None
    # expect = json.loads(expect)
    # response = request_get(method, url, header, body)
    # check(response, expect)







