import unittest
from testcase.gpg2_chromeset import env, ma_api, BackAPI
from script.utils import TimeSelect
time_select = TimeSelect()
import logging
import inspect
class Test_WalletChangeReport(unittest.TestCase):
    """會員點數異動紀錄"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_WalletChangeReport_API(self):
        """測試總代理的會員點數異動紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'PointTypeID': 0,
                                      'ChangeTypeID': 0,
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'IsGuest': False, },
                             api_url=BackAPI.dataReport_walletChangeReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_WalletChangeReport_API(self):
        """測試A代理的會員點數異動紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'PointTypeID': 0,
                                      'ChangeTypeID': 0,
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'IsGuest': False, },
                             api_url=BackAPI.dataReport_walletChangeReport.value)
        self.assertEqual('', res)

    def test_B_Agent_WalletChangeReport_API(self):
        """測試B代理的會員點數異動紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'PointTypeID': 0,
                                      'ChangeTypeID': 0,
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'IsGuest': False, },
                             api_url=BackAPI.dataReport_walletChangeReport.value)
        self.assertEqual('', res)

    def test_C_Agent_WalletChangeReport_API(self):
        """測試C代理的會員點數異動紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'PointTypeID': 0,
                                      'ChangeTypeID': 0,
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'IsGuest': False, },
                             api_url=BackAPI.dataReport_walletChangeReport.value)
        self.assertEqual('', res)
