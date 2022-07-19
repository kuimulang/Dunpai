# -*- coding: UTF-8 -*-
# https://www.jb51.net/article/199936.htm
import unittest
import requests

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # 请求豆瓣首页
        param = {"q":"西游记"}
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Mobile Safari/537.36'}
        r = requests.get("https://www.douban.com",headers=headers,params=param)
        print(r.status_code)
        print(r.url)
        print(r.text)
       # self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
