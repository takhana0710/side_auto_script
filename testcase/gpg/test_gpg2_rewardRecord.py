import unittest
from selenium.webdriver.common.by import By
import warnings
from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify
from testcase.HTMLTestReportCN import HTMLTestRunner
"""
會員儲值、贈禮紀錄
本月查詢範圍：這個月1號-今天
上月查詢範圍：上個月1號-上個月底
更多：去年今天-今天
"""
class Test_RewardRecord(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()
        
    @classmethod
    def setUpClass(cls):
        progressNotify(message='訂單記錄測試開始')
    
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='訂單記錄測試完成')

    def test_RewardRecord_guest(self):
        """測試訪客模式下是否有訂單記錄"""
        self.test_driver.loginV2(identity='guest')
        try:
            res = self.test_driver.memberSelect('訂單')
        except:
            res = None
        self.assertIsNone(res)

    def test_RewardRecord_member(self):
        """測試會員模式下是否有訂單記錄"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect('訂單')
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"record__wrap")]'))

    def test_RewardRecord_agentMember(self):
        """測試代理會員模式下是否有訂單記錄"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect('訂單')
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"record__wrap")]'))

    def test_RewardRecord_TransactionRecord_ChangeCode_member(self):
        """測試會員模式下是否可以兌換禮物"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("訂單")
        present_code, order_no = self.test_driver.memberSendRecord()
        self.assertIsNotNone(present_code)

    def test_RewardRecord_TransactionRecord_ChangeCode_agentMember(self):
        """測試代理會員模式下是否可以兌換禮物"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("訂單")
        present_code, order_no = self.test_driver.memberSendRecord()
        self.assertIsNotNone(present_code)
        
    def test_TransactionRecord_Cancel_member(self):
        self.test_driver.loginV2()
        self.test_driver.memberSelect('訂單')
    def test_TransactionRecord_Cancel_agentMember(self):
        pass


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())