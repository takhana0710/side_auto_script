import time
import unittest
from testcase.gpg2_chromeset import driver_eng, clean_resource, progressNotify
from selenium.webdriver.common.by import By
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
import json


class Test_Service(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)
    
    def tearDown(self):
        self.test_driver.exit()
    
    @classmethod
    def setUpClass(cls):
        progressNotify(message='服務條款內容測試開始')
    
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='服務條款內容測試完成')
    
    def test_service_guest(self):
        """測試訪客模式下是否有客服按鈕"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.service()
    
    def test_service_member(self):
        """測試會員模式下是否有客服按鈕"""
        self.test_driver.loginV2()
        self.test_driver.service()
    
    def test_service_agentMember(self):
        """測試代理會員模式下是否有客服按鈕"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.service()
    
    def test_service_list_guest(self):
        """測試訪客模式下是否有5種問題分類"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.service()
        res = self.test_driver.driver.find_elements(By.XPATH,
                                                    '//div[contains(@class,"swiper-wrapper")]/div/div[contains(@class,"game__sort__item")]')
        self.assertEqual(5, len(res))
    
    def test_service_list_member(self):
        """測試會員模式下是否有5種問題分類"""
        self.test_driver.loginV2()
        self.test_driver.service()
        res = self.test_driver.driver.find_elements(By.XPATH,
                                                    '//div[contains(@class,"swiper-wrapper")]/div/div[contains(@class,"game__sort__item")]')
        self.assertEqual(5, len(res))
    
    def test_service_list_agentMember(self):
        """測試代理會員模式下是否有5種問題分類"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.service()
        res = self.test_driver.driver.find_elements(By.XPATH,
                                                    '//div[contains(@class,"swiper-wrapper")]/div/div[contains(@class,"game__sort__item")]')
        self.assertEqual(5, len(res))
    
    def test_service_article_guest(self):
        """測試訪客模式下是否可以點擊三個按鈕"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.service()
        self.test_driver.article()
    
    def test_service_article_member(self):
        """測試會員模式下是否可以點擊三個按鈕"""
        self.test_driver.loginV2()
        self.test_driver.service()
        self.test_driver.article()
    
    def test_service_article_agentMember(self):
        """測試代理會員模式下是否可以點擊三個按鈕"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.service()
        self.test_driver.article()
    
    def test_service(self):
        """測試代理會員模式下是否可以點擊三個按鈕"""
        # self.test_driver.loginV2()
        self.test_driver.driver.get('https://gpg.ceis.tw/game/detail/5523')
        time.sleep(10)
        logs_row = self.test_driver.driver.get_log('performance')
        logs = [json.loads(lr["message"])["message"] for lr in logs_row]
        # self.api_parser(api_list=logs)
        self.test_driver.api_parser(api_list=logs)
        time.sleep(10)
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
