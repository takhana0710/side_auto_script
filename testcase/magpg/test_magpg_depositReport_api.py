import unittest
from testcase.gpg2_chromeset import env, ma_api, BackAPI
from script.utils import TimeSelect
import logging
import inspect
time_select = TimeSelect()
class Test_DepositReport_api(unittest.TestCase):
    """儲值報表"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_DepositReport_API(self):
        """測試總代理的儲值報表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'PayTypeID': 0,
                                      'sDate': time_select.MonthStart()[:7],
                                      'eDate': time_select.MonthEnd()[:7],
                                      'Skip': 0,
                                      'Show': 9999,
                                      'Field': 'Date',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_depositReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_DepositReport_API(self):
        """測試A代理的儲值報表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'PayTypeID': 0,
                                      'sDate': time_select.MonthStart()[:7],
                                      'eDate': time_select.MonthEnd()[:7],
                                      'Skip': 0,
                                      'Show': 9999,
                                      'Field': 'Date',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_depositReport.value)
        self.assertEqual('', res)

    def test_B_Agent_DepositReport_API(self):
        """測試B代理的儲值報表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'PayTypeID': 0,
                                      'sDate': time_select.MonthStart()[:7],
                                      'eDate': time_select.MonthEnd()[:7],
                                      'Skip': 0,
                                      'Show': 9999,
                                      'Field': 'Date',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_depositReport.value)
        self.assertEqual('', res)

    def test_C_Agent_DepositReport_API(self):
        """測試C代理的儲值報表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'PayTypeID': 0,
                                      'sDate': time_select.MonthStart()[:7],
                                      'eDate': time_select.MonthEnd()[:7],
                                      'Skip': 0,
                                      'Show': 9999,
                                      'Field': 'Date',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_depositReport.value)
        self.assertEqual('', res)
