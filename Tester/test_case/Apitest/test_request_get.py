import unittest

from Tester.commom.Apitest.request_get import request_get


class MyTestCase(unittest.TestCase):
    def test_something(self):
        url = "http://localhost:9186/v2/department/getDepartments4"
        request_param = {"scene": "homepage"}
        a = request_get(url, request_param)
        print(a)
        # self.assertEqual(True, False)  # add assertion here
if __name__ == '__main__':
    unittest.main()
