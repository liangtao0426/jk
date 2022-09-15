
import requests
import unittest
from unittest import mock
from zfb import PayApi

class TestPayApi(unittest.TestCase):
    def test_success(self):
        pay = PayApi()
        pay.auth=mock.Mock(return_value={'status_code':'200'})
        status = pay.pay('100','12','100')
        self.assertEqual(status,'支付成功')

    def test_fail(self):
        pay = PayApi()
        pay.auth=mock.Mock(return_value={'status_code':'500'})
        status = pay.pay('100','12','100')
        self.assertEqual(status,'支付失败')

    def test_error(self):
        pay = PayApi()
        pay.auth=mock.Mock(return_value={'status_code':'300'})
        status = pay.pay('100','12','100')
        self.assertEqual(status,'未知错误')

    def test_exception(self):
        pay = PayApi()
        pay.auth=mock.Mock(return_value='200')
        status = pay.pay('100','12','100')
        self.assertEqual(status,"Error,服务器异常")
if __name__=='__main__':
    unittest.main()


#


