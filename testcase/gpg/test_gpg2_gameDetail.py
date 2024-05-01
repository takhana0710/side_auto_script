import unittest
from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify
from selenium.webdriver.common.by import By
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner

class Test_GameDetail(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()

    @classmethod
    def setUpClass(cls):
        progressNotify(message='遊戲詳細測試開始')

    @classmethod
    def tearDownClass(cls):
        progressNotify(message='遊戲詳細測試開始')

    def test_GameDetail_guest(self):
        """測試訪客模式下遊戲詳細頁"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.asideBarSelect(fun_text="遊戲")
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__container")]/div/div'))

    def test_GameDetail_member(self):
        """測試會員模式下遊戲詳細頁"""
        self.test_driver.loginV2()
        self.test_driver.asideBarSelect(fun_text="遊戲")
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__container")]/div/div'))
    def test_GameDetail_agentMember(self):
        """測試代理會員模式下遊戲詳細頁"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.asideBarSelect(fun_text="遊戲")
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__container")]/div/div'))


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())