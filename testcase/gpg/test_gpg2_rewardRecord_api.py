import time
from testcase.gpg2_chromeset import gpg_api,env,progressNotify,FontAPI
import unittest
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
import sys
import logging
import inspect
sys.path.append('../..')
from script.utils import TimeSelect

time_select = TimeSelect()
class Test_RewardRecord_api(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
    def tearDown(self):
        pass
        
    @classmethod
    def setUpClass(cls):
        progressNotify(message='訂單記錄API測試開始')

    @classmethod
    def tearDownClass(cls):
        progressNotify(message='訂單記錄API測試開始')
    
    def test_Reward_TransactionRecord_api_Member(self):
        """測試會員模式下API能否兌換"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method nam
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='get',payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd(), 'RecordType': 1, 'Skip': 0, 'Show': 9999},api_url=env['font_api']+'Transaction/TransactionRecord')
        tid = list(filter(lambda x:x['MTCodeDisclosed'] == False,res['Data'])).pop()
        res = self.api.apiGetData(method='post',data={"TID":tid['TID']},api_url=FontAPI.transaction_discloseSerialNo.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_Reward_TransactionRecord_api_agentMember(self):
        """測試代理會員模式下API能否兌換"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='get',payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd(), 'RecordType': 1, 'Skip': 0, 'Show': 9999},api_url=env['font_api']+'Transaction/TransactionRecord')
        tid = list(filter(lambda x:x['MTCodeDisclosed'] == False,res['Data'])).pop()
        res = self.api.apiGetData(method='post',data={"TID":tid['TID']},api_url=FontAPI.transaction_discloseSerialNo.value)
        self.assertEqual(res['Status']['Message'], 'Success')
        
    def test_RewardRecord_OrderList_api_guest(self):
        """測試訪客模式下是否可以查詢訂單記錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get', payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},
                                  api_url=FontAPI.member_orderList.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_RewardRecord_OrderList_api_member(self):
        """測試會員模式下是否可以查詢訂單記錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='get', payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},
                                  api_url=FontAPI.member_orderList.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_RewardRecord_OrderList_api_agentMember(self):
        """測試會員模式下是否可以查詢訂單記錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='get', payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},
                                  api_url=FontAPI.member_orderList.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_RewardRecord_TransactionRecord_sendPresent_api_guest(self):
        """測試訪客模式下是否可以查詢贈禮紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get',
                                  payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd(), 'RecordType': 1, 'Skip': 0,
                                           'Show': 9999},
                                  api_url=FontAPI.transaction_transactionRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_RewardRecord_TransactionRecord_sendPresent_api_member(self):
        """測試會員模式下是否可以查詢贈禮紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='get',
                                  payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd(), 'RecordType': 1, 'Skip': 0,
                                           'Show': 9999},
                                  api_url=FontAPI.transaction_transactionRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_RewardRecord_TransactionRecord_sendPresent_api_agentMember(self):
        """測試代理會員模式下是否可以查詢贈禮紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='get',
                                  payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd(), 'RecordType': 1, 'Skip': 0,
                                           'Show': 9999},
                                  api_url=FontAPI.transaction_transactionRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_RewardRecord_TransactionRecord_receive_api_guest(self):
        """測試訪客模式下是否可以查詢收禮紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get',
                                  payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd(), 'RecordType': 2, 'Skip': 0,
                                           'Show': 9999},
                                  api_url=FontAPI.transaction_transactionRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_RewardRecord_TransactionRecord_receive_api_member(self):
        """測試會員模式下是否可以查詢收禮紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='get',
                                  payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd(), 'RecordType': 2, 'Skip': 0,
                                           'Show': 9999},
                                  api_url=FontAPI.transaction_transactionRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_RewardRecord_TransactionRecord_receive_api_agentMember(self):
        """測試代理會員模式下是否可以查詢收禮紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='get',
                                  payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd(), 'RecordType': 2, 'Skip': 0,
                                           'Show': 9999},
                                  api_url=FontAPI.transaction_transactionRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())