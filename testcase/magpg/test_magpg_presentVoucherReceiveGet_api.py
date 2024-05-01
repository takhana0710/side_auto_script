import unittest
from testcase.gpg2_chromeset import ma_api, BackAPI
import logging
import inspect

class Test_VoucherReceiveGet_api(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_GPG_VoucherReceiveGet(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', payload={'Skip': 0,'Show': 50,
                                                    'Field': 'MemberName',
                                                    'OrderType': 'desc',
                                                    'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherReceiveGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_agent_VoucherReceiveGet(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', payload={'Skip': 0,'Show': 50,
                                                    'Field': 'MemberName',
                                                    'OrderType': 'desc',
                                                    'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherReceiveGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_agent_VoucherReceiveGet(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', payload={'Skip': 0,'Show': 50,
                                                    'Field': 'MemberName',
                                                    'OrderType': 'desc',
                                                    'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherReceiveGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_agent_VoucherReceiveGet(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', payload={'Skip': 0,'Show': 50,
                                                    'Field': 'MemberName',
                                                    'OrderType': 'desc',
                                                    'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherReceiveGet.value)
        self.assertEqual('Success', res['Status']['Message'])

