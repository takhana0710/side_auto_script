import unittest
from testcase.gpg2_chromeset import gpg_api,progressNotify,FontAPI
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
import logging
import inspect
import sys
sys.path.append('../..')
from script.utils import TimeSelect
"""
轉帳紀錄-單元測試
玩家可以查31天的轉移紀錄
日期格式為yyyy/MM/dd hh:mm:ss
default:當天
from wallet:default:all
to wallet:default:all
coin type:gold,sliver
"""
time_select = TimeSelect()

class Test_transferRecord(unittest.TestCase):
    def setUp(self):
        # self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        pass
        # self.test_driver.exit()
        
    @classmethod
    def setUpClass(cls):
        progressNotify(message='轉帳紀錄測試開始')
        
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='轉帳紀錄測試完成')

    def test_transferRecord_overMonth_guest(self):
        """測試訪客模式下是否超過一個月查詢(規格不符)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='post', data={"PointTypeID": 0, "FromWalletID": -1, "ToWalletID": -1,
         "sDate": time_select.OverMonthStart(),
         "eDate": time_select.MonthEnd(),
         "Skip": 0, "Show": 1000,
         "Field": "CreateTime",
         "OrderType": "desc"}, api_url=FontAPI.wallet_transferRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_transferRecord_overMonth_member(self):
        """測試會員模式下是否超過一個月查詢(規格不符)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.login()
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='post', data=
        {"PointTypeID": 0, "FromWalletID": -1, "ToWalletID": -1,
         "sDate": time_select.MonthStart(),
         "eDate": time_select.MonthEnd(),
         "Skip": 0, "Show": 1000,
         "Field": "CreateTime",
         "OrderType": "desc"}, api_url=FontAPI.wallet_transferRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_transferRecord_overMonth_agentMember(self):
        """測試代理會員模式下是否超過一個月查詢(規格不符)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='post', data=
        {"PointTypeID": 0, "FromWalletID": -1, "ToWalletID": -1,
         "sDate": time_select.MonthStart(),
         "eDate": time_select.MonthEnd(),
         "Skip": 0, "Show": 1000,
         "Field": "CreateTime",
         "OrderType": "desc"}, api_url=FontAPI.wallet_transferRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_transferRecord_guest(self):
        """測試訪客模式下是否有轉帳紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='post', data=
        {"PointTypeID": 0, "FromWalletID": -1, "ToWalletID": -1,
         "sDate": time_select.MonthStart(),
         "eDate": time_select.MonthEnd(),
         "Skip": 0, "Show": 1000,
         "Field": "CreateTime",
         "OrderType": "desc"}, api_url=FontAPI.wallet_transferRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_transferRecord_member(self):
        """測試會員模式下是否有轉帳紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.login()
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='post', data=
        {"PointTypeID": 0, "FromWalletID": -1, "ToWalletID": -1,
         "sDate": time_select.MonthStart(),
         "eDate": time_select.MonthEnd(),
         "Skip": 0, "Show": 1000,
         "Field": "CreateTime",
         "OrderType": "desc"}, api_url=FontAPI.wallet_transferRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_transferRecord_agentMember(self):
        """測試代理會員模式下是否有轉帳紀錄"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='post', data=
        {"PointTypeID": 0, "FromWalletID": -1, "ToWalletID": -1,
         "sDate": time_select.MonthStart(),
         "eDate": time_select.MonthEnd(),
         "Skip": 0, "Show": 1000,
         "Field": "CreateTime",
         "OrderType": "desc"}, api_url=FontAPI.wallet_transferRecord.value)
        self.assertEqual(res['Status']['Message'], 'Success')


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
