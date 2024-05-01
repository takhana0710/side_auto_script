import unittest
from testcase.gpg2_chromeset import ma_api, BackAPI
from script.utils import TimeSelect
import logging
import inspect
time_select = TimeSelect()
class Test_MiningReceipts_api(unittest.TestCase):
    """會員礦機領取紀錄"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_MiningReceipts_API(self):
        """測試總代理的會員礦機領取紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_miningReceipts.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_MiningReceipts_API(self):
        """測試A代理的會員礦機領取紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_miningReceipts.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_MiningReceipts_API(self):
        """測試B代理的會員礦機領取紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_miningReceipts.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_MiningReceipts_API(self):
        """測試C代理的會員礦機領取紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_miningReceipts.value)
        self.assertEqual('Success', res['Status']['Message'])
