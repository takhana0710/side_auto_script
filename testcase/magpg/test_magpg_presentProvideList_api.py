import unittest
from testcase.gpg2_chromeset import ma_api, BackAPI
import logging
import inspect

class Test_PresentProvideList_api(unittest.TestCase):
    """發送清單"""
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_GPG_SendGet(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', payload={'Skip': 0,'Show': 50,
                                                    'Field': 'VoucherName',
                                                    'OrderType': 'desc',
                                                    'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherSendGet.value)
        self.assertEqual('Success', res['Status']['Message'])
    def test_A_agent_SendGet(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', payload={'Skip': 0,'Show': 50,
                                                    'Field': 'VoucherName',
                                                    'OrderType': 'desc',
                                                    'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherSendGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_agent_SendGet(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', payload={'Skip': 0,'Show': 50,
                                                    'Field': 'VoucherName',
                                                    'OrderType': 'desc',
                                                    'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherSendGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_agent_SendGet(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', payload={'Skip': 0,'Show': 50,
                                                    'Field': 'VoucherName',
                                                    'OrderType': 'desc',
                                                    'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherSendGet.value)
        self.assertEqual('Success', res['Status']['Message'])