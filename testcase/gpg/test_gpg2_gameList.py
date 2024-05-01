import unittest
from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify
from selenium.webdriver.common.by import By
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
"""
遊戲列表
"""
class Test_GameList(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()
    @classmethod
    def setUpClass(cls):
        progressNotify(message='遊戲列表測試開始')
    
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='遊戲列表測試完成')

    def test_GameList_guest(self):
        """測試訪客模式下遊戲詳細頁"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.driver.find_element(By.XPATH,'//span[text()="遊戲"]').click()
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__list__wrap")]'))
    def test_GameList_member(self):
        """測試會員模式下遊戲詳細頁"""
        self.test_driver.loginV2()
        self.test_driver.driver.find_element(By.XPATH,'//span[text()="遊戲"]').click()
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__list__wrap")]'))
    def test_GameList_agentMember(self):
        """測試代理會員模式下遊戲詳細頁"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.driver.find_element(By.XPATH,'//span[text()="遊戲"]').click()
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__list__wrap")]'))


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())