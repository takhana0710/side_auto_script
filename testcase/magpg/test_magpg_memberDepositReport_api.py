import unittest
from testcase.gpg2_chromeset import env, ma_api, BackAPI
from script.utils import TimeSelect
import logging
import inspect
time_select = TimeSelect()


class Test_MemberDepositReport(unittest.TestCase):
    """會員儲值紀錄"""
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_GPG_MemberDepositReport_API(self):
        """測試總代理的會員儲值紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'StoredStatusID': -1},
                             api_url=BackAPI.dataReport_memberDepositReport.value)
        self.assertEqual('Success', res['Status']['Message'])
    
    def test_A_Agent_MemberDepositReport_API(self):
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        """測試A代理的會員儲值紀錄是否正常成功"""
        api = ma_api(account='QAminiag20', password='QAminiag20')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'StoredStatusID': -1, },
                             api_url=BackAPI.dataReport_memberDepositReport.value)
        self.assertEqual('', res)
    
    def test_B_Agent_MemberDepositReport_API(self):
        """測試B代理的會員儲值紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag21', password='QAminiag21')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'StoredStatusID': -1, },
                             api_url=BackAPI.dataReport_memberDepositReport.value)
        self.assertEqual('', res)
    
    def test_C_Agent_MemberDepositReport_API(self):
        """測試C代理的會員儲值紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag22', password='QAminiag22')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'StoredStatusID': -1, },
                             api_url=BackAPI.dataReport_memberDepositReport.value)
        self.assertEqual('', res)
