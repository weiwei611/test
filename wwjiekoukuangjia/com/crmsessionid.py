from wwjiekoukuangjia.com.get_host import *
import requests


def get_session():
    host = get_host()
    url = host + "/crm/login-step1"
    body = {
        "name": "18888888888",
        "password": "MTIwMTEwMiAxMjAxMjAxIDEyMDIyMDIgMTIwMjEwMiAxMjAyMjEx"
    }

    R = requests.post(url=url, data=body)
    x = R.json()
    return x['crmsessionid']

if __name__ == "__main__":
    print(get_session())
