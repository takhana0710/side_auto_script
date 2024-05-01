import unittest
from testcase.gpg2_chromeset import ma_api, BackAPI
import logging
import inspect

class Test_SmsVerifications_api(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_GPG_SmsVerifications(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             api_url=BackAPI.infos_smsVerifications.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_agent_SmsVerifications(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.infos_smsVerifications.value)
        self.assertEqual('', res)

    def test_B_agent_SmsVerifications(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.infos_smsVerifications.value)
        self.assertEqual('', res)

    def test_C_agent_SmsVerifications(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.infos_smsVerifications.value)
        self.assertEqual('', res)

