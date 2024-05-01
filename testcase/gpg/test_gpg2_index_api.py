from testcase.gpg2_chromeset import gpg_api,progressNotify,FontAPI
import unittest
from testcase.HTMLTestReportCN import HTMLTestRunner
import logging
import inspect
from script.utils import TimeSelect

time_select = TimeSelect()
class Test_Index_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        progressNotify(message='首頁API測試開始')
    
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='首頁API測試完成')
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_gameRank_api_guest(self):
        """測試訪客模式下首頁排行榜是否正常"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get', payload={},api_url=FontAPI.game_leaderboard.value)
        self.assertEqual(res['Status']['Message'], 'Success')
    
    def test_gameRank_api_member(self):
        """測試會員模式下首頁排行榜是否正常"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get', payload={},api_url=FontAPI.game_leaderboard.value)
        self.assertEqual(res['Status']['Message'], 'Success')
    
    def test_gameRank_api_agentMember(self):
        """測試代理模式下首頁排行榜是否正常"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get', payload={},api_url=FontAPI.game_leaderboard.value)
        self.assertEqual(res['Status']['Message'], 'Success')
    
    def test_gameRank_content(self):
        """測試排行榜是否有重複遊戲"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get', payload={},api_url=FontAPI.game_leaderboard.value)
        res = set(list(map(lambda x:x.get('GameID'),res['Data'])))
        self.assertEqual(len(res), 10)
        
    def test_getPetInfo_member(self):
        """測試會員模式下礦寵資訊狀態"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='get', payload={}, api_url=FontAPI.mining_getPetInfo.value)
        self.assertEqual(res['Status']['Code'], '0')
    
    def test_getPetInfo_agentMember(self):
        """測試代理會員模式下礦寵資訊狀態"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='get', payload={}, api_url=FontAPI.mining_getPetInfo.value)
        self.assertEqual(res['Status']['Code'], '0')
    
    # def test_SignIn_data(self):
    #     """測試本月簽到是否有符合規格(從google撈資料)"""
    #     logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
    #     month=time_select.MonthEnd()[:7] # ex:2022-05
    #     sheet_month = time_select.MonthEnd()[:8] # ex:2022-05-
    #     sheet_data = int(month[-2:])
    #     signFormat = SignInData(sheetName=str(sheet_data)+'月簽到',sheetMonth=sheet_month)
    #     self.api=gpg_api(token='memberToken')
    #     res = self.api.apiGetData(method='get', payload={'Month':month}, api_url=FontAPI.activity_normal_signInMonthList.value)['Data']
    #     for i in res:
    #         del i['IsSignIn']
    #         del i['BonusTypeID']
    #         del i['SignInTime']
    #     self.assertEqual(res,signFormat)

        
if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())