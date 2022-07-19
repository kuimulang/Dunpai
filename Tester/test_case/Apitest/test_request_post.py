import unittest
from Tester.commom.Apitest.request_post import request_post

class MyTestCase(unittest.TestCase):
    def test_something(self):
        url = "http://localhost:9186/common/login"
        request_param = {"phoneArea": "86","phoneNumber": "20000000000","password": "netease123"}
        a = request_post(url, request_param)
        print(a)
        # self.assertEqual(True, False)  # add assertion here
if __name__ == '__main__':
    unittest.main()
