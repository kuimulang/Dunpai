import json
import requests

def request_get(url, param):
    fails = 0
    while True:
        try:
            if fails >= 20:
                break
            ret = requests.get(url=url, params=param, timeout=10)

            if ret.status_code == 200:
                text = json.loads(ret.text)
            else:
                continue
        except:
            fails += 1
            print('网络连接出现问题, 正在尝试再次请求: ', fails)
        else:
            break
    return text