import unittest
from testcase.gpg2_chromeset import env, ma_api, BackAPI
from script.utils import TimeSelect
time_select=TimeSelect()
import inspect
import logging
class Test_Index(unittest.TestCase):
    """會員交易紀錄"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_TransactionRecord_API(self):
        """測試總代理的會員交易紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'PointTypeID': 0,
                                      'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_transactionRecord.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_TransactionRecord_API(self):
        """測試A代理的會員交易紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag20', password='QAminiag20')
        res = api.apiGetData(method='get',
                             payload={'PointTypeID': 0,
                                      'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_transactionRecord.value)
        self.assertEqual('', res)

    def test_B_Agent_TransactionRecord_API(self):
        """測試B代理的會員交易紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag21', password='QAminiag21')
        res = api.apiGetData(method='get',
                             payload={'PointTypeID': 0,
                                      'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_transactionRecord.value)
        self.assertEqual('', res)

    def test_C_Agent_TransactionRecord_API(self):
        """測試C代理的會員交易紀錄是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag22', password='QAminiag22')
        res = api.apiGetData(method='get',
                             payload={'PointTypeID': 0,
                                      'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_transactionRecord.value)
        self.assertEqual('', res)
