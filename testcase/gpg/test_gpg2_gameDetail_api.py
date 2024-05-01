import time
from testcase.gpg2_chromeset import gpg_api,progressNotify,FontAPI
import unittest
from testcase.HTMLTestReportCN import HTMLTestRunner
import logging
import inspect

class Test_GameDetail_api(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    @classmethod
    def setUpClass(cls):
        progressNotify(message='遊戲詳細API測試開始')
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='遊戲詳細API測試開始')
        
    def test_GameDetail_api_guest(self):
        """測試訪客模式下遊戲詳細頁-api"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get', payload={'GameID':3},
                                  api_url=FontAPI.game_gameInfo.value)
        self.assertEqual(res['Status']['Message'], 'Success')
    def test_GameDetail_api_member(self):
        """測試會員模式下遊戲詳細頁-api"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='get', payload={'GameID':3},
                                  api_url=FontAPI.game_gameInfo.value)
        self.assertEqual(res['Status']['Message'], 'Success')
    def test_GameDetail_api_agentMember(self):
        """測試代理會員模式下遊戲詳細頁-api"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='get', payload={'GameID':3},
                                  api_url=FontAPI.game_gameInfo.value)
        self.assertEqual(res['Status']['Message'], 'Success')
    
    
if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())