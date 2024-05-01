import time
import unittest
import logging
import inspect
import warnings
from testcase.gpg2_chromeset import gpg_api,progressNotify,FontAPI
from testcase.HTMLTestReportCN import HTMLTestRunner

class Test_sendPresent_api(unittest.TestCase):
    def setUp(self):
        # self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)
    def tearDown(self):
        # self.test_driver.exit()
        pass
    @classmethod
    def setUpClass(cls):
        progressNotify(message='贈禮打包API測試開始')
    
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='贈禮打包API測試完成')
        
    def test_sendPresent_api_gold_guest_old(self):
        """測試訪客模式是否能夠送禮(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": 1000, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res, '')

    def test_sendPresent_api_sliver_guest(self):
        """測試訪客模式是否能夠送禮(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": 100000, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res, '')
        
    def test_sendPresent_api_gold_member_new(self):
        """測試會員模式是否能夠送禮(金幣)1221 改 3000"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='memberToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": 3000, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_sendPresent_api_sliver_member(self):  # AccessCacheFailed, please verify transaction password in advance.
        """測試會員模式是否能夠送禮(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='memberToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": 100000, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_sendPresent_api_gold_agentMember_new(self):
        """測試代理會員模式是否能夠送禮(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": 3000, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_sendPresent_api_sliver_agentMember(self):
        """測試代理會員模式是否能夠送禮(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": 100000, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_sendPresent_api_gold_lowMin_guest(self):
        """測試訪客模式是否能夠送禮最小值(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": 1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res, '')

    def test_sendPresent_api_sliver_lowMin_guest(self):
        """測試訪客模式是否能夠送禮最小值(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": 1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res, '')

    def test_sendPresent_api_gold_lowMin_member(self):
        """測試會員模式是否能夠送禮最小值(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.login()
        self.api = gpg_api(token='memberToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": 1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Transaction Out of Range')

    def test_sendPresent_api_sliver_lowMin_member(self):
        """測試會員模式是否能夠送禮最小值(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.login()
        self.api = gpg_api(token='memberToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": 1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Transaction Out of Range')

    def test_sendPresent_api_gold_lowMin_agentMember(self):
        """測試代理會員模式是否能夠送禮最小值(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": 1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Transaction Out of Range')

    def test_sendPresent_api_sliver_lowMin_agentMember(self):
        """測試代理會員模式是否能夠送禮最小值(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post', data={"PointTypeID": 2, "Point": 1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Transaction Out of Range')

    def test_sendPresent_api_gold_negativeNumber_guest(self):
        """測試訪客模式是否能夠送禮負數(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": -1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res, '')

    def test_sendPresent_api_sliver_negativeNumber_guest(self):
        """測試訪客模式是否能夠送禮負數(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": -1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res, '')

    def test_sendPresent_api_gold_negativeNumber_member(self):
        """測試會員模式是否能夠送禮負數(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.login()
        self.api = gpg_api(token='memberToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": -1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Transaction Out of Range')

    def test_sendPresent_api_sliver_negativeNumber_member(self):  # AccessCacheFailed, please verify transaction password in advance.
        """測試會員模式是否能夠送禮負數(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.login()
        self.api = gpg_api(token='memberToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": -1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Transaction Out of Range')

    def test_sendPresent_api_gold_negativeNumber_agentMember(self):
        """測試代理會員模式是否能夠送禮負數(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": -1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Transaction Out of Range')

    def test_sendPresent_api_sliver_negativeNumber_agentMember(self):  # AccessCacheFailed, please verify transaction password in advance.
        """測試代理會員模式是否能夠送禮負數(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": -1, "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'], 'Transaction Out of Range')

    def test_sendPresent_api_gold_syntaxError_guest(self):
        """測試訪客模式是否能夠送禮非整數(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": "string", "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res, '')

    def test_sendPresent_api_sliver_syntaxError_guest(self):
        """測試訪客模式是否能夠送禮非整數(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.guest()
        self.api = gpg_api(token='guestToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": "string", "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res, '')

    def test_sendPresent_api_gold_syntaxError_member(self):
        """測試會員模式是否能夠送禮非整數(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.login()
        self.api = gpg_api(token='memberToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": "string", "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'],
                         'The JSON value could not be converted to System.Int64. Path: $.Point | LineNumber: 0 | BytePositionInLine: 36.')

    def test_sendPresent_api_sliver_syntaxError_member(self):
        """測試會員模式是否能夠送禮非整數(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.login()
        self.api = gpg_api(token='memberToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": "string", "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'],
                         'The JSON value could not be converted to System.Int64. Path: $.Point | LineNumber: 0 | BytePositionInLine: 36.')

    def test_sendPresent_api_gold_syntaxError_agentMember(self):
        """測試代理會員模式是否能夠送禮非整數(金幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 1, "Point": "string", "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'],
                         'The JSON value could not be converted to System.Int64. Path: $.Point | LineNumber: 0 | BytePositionInLine: 36.')

    def test_sendPresent_api_sliver_syntaxError_agentMember(self):
        """測試代理會員模式是否能夠送禮非整數(銀幣)"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        # self.test_driver.AgentLogin()
        self.api = gpg_api(token='agentToken')
        self.api.apiGetData(method='post', data={"TransactionPassword": "123456"},
                            api_url=FontAPI.transaction_verifyPassword.value)
        res = self.api.apiGetData(method='post',
                                  data={"PointTypeID": 2, "Point": "string", "TransactionPassword": "123456"},
                                  api_url=FontAPI.transaction_submitRewardPoint.value)
        self.assertEqual(res['Status']['Message'],
                         'The JSON value could not be converted to System.Int64. Path: $.Point | LineNumber: 0 | BytePositionInLine: 36.')

    

if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
