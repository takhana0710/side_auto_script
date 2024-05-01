from testcase.gpg2_chromeset import ma_driver_eng, clean_resource, progressNotify
from selenium.webdriver.common.by import By
from testcase.HTMLTestReportCN import HTMLTestRunner
from script.utils import TimeSelect
from datetime import datetime
import unittest
import time

time_select = TimeSelect()


class Test_Advertisers(unittest.TestCase):
    """廣告加盟商列表"""
    
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='廣告加盟商管理')
        self.test_driver.func_select(text='廣告加盟商列表')
    
    def tearDown(self):
        pass
    
    def test_memberID(self):
        """測試會員ID搜尋"""
        self.test_driver.scroll_select(label_text='搜尋類型', text='會員ID')
        self.test_driver.input_text(label_text='搜尋資料',text='2')
        self.test_driver.driver.find_element(By.XPATH, '//button/span[text()="搜尋"]').click()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[1]/div/span').text
        self.assertEqual(res, '2')
    def test_phone(self):
        """測試手機號搜尋"""
        self.test_driver.scroll_select(label_text='搜尋類型', text='手機號')
        self.test_driver.input_text(label_text='搜尋資料',text='+886908796886')
        self.test_driver.driver.find_element(By.XPATH, '//button/span[text()="搜尋"]').click()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[3]/div/span').text
        time.sleep(5)
        self.assertEqual(res, '+886908796886')
    
    def test_nickname(self):
        """測試會員暱稱"""
        self.test_driver.scroll_select(label_text='搜尋類型', text='會員暱稱')
        self.test_driver.input_text(label_text='搜尋資料',text='JKF')
        self.test_driver.driver.find_element(By.XPATH, '//button/span[text()="搜尋"]').click()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[2]/div/span').text
        self.assertEqual(res, 'JKF')
        
    def test_IP(self):
        """測試登入IP"""
        self.test_driver.scroll_select(label_text='搜尋類型', text='登入IP')
        self.test_driver.input_text(label_text='搜尋資料',text='125.230.252.162')
        self.test_driver.driver.find_element(By.XPATH, '//button/span[text()="搜尋"]').click()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[13]/div/div[2]').text
        self.assertEqual(res, '125.230.252.162')
        
    def test_rr(self):
        self.test_driver.scroll_select(label_text='搜尋類型',text='手機號')
        self.test_driver.fuzzy_search()