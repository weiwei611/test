import xlrd, os, sys, logging


def runExcel(testCaseFile):
    testCaseFile = os.path.join(os.getcwd(), testCaseFile)
    if not os.path.exists(testCaseFile):
        logging.error("测试用例文件不存在")
        sys.exit()
    workbook = xlrd.open_workbook(testCaseFile)
    sh = workbook.sheet_by_index(0)
    rows = sh.nrows
    cols = sh.ncols
    data = []
    for i in range(1, rows):
        data_rows = []
        for j in range(2, cols):
            d = sh.cell_value(i, j)
            # d = sh.cell(i, j).value
            if j == 2:
                if d == "off":
                    break
            data_rows.append(d)
        if data_rows:
            data.append(data_rows)

    return data


if __name__ == "__main__":
    print(runExcel("../testcase/case.xls"))




    # # 是否执行用例“是”或“否”
    # col2 = sh.col_values(2)
    # # 获取host
    # api_host = sh.col_values(3)
    # #请求类型“post”或“get”
    # request_method = sh.col_values(4)
    # #是否携带headers
    # reqest_headers = sh.col_values(5)
    # #post请求的request
    # request_data = sh.col_values(6)
    # #返回的基本类型
    # response = sh.col_values(7)
    # #print(response)
    # return [col2, api_host, request_method, reqest_headers, request_data, response]





























