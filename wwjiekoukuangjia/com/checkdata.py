import json

def test_check(response, expect):
    for k in expect:
        if not isinstance(expect[k], dict):
            assert response[k] == expect[k]
            if response[k] == expect[k]:
                #print(response)
                return response
            else:
                return "测试失败"
        else:
            for k1 in expect[k]:
                if not isinstance(expect[k][k1], list):
                    assert response[k][k1] == expect[k][k1]
                    if response[k][k1] == expect[k][k1]:
                        return "测试通过"
                    else:
                        return "测试失败"
                else:
                    i = 0
                    for k2 in expect[k][k1]:
                        for k3 in k2:
                            assert response[k][k1][i][k3] == expect[k][k1][i][k3]
                            if response[k][k1][i][k3] == expect[k][k1][i][k3]:
                                return "测试通过"
                            else:
                                return "测试失败"
                        i += 1


