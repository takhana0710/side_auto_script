from testcase.gpg2_chromeset import ma_driver_eng, clean_resource, progressNotify
from selenium.webdriver.common.by import By
from testcase.HTMLTestReportCN import HTMLTestRunner
from script.utils import TimeSelect
from datetime import datetime
import unittest
import time

time_select = TimeSelect()


class Test_Promote(unittest.TestCase):
    """推廣連結管理"""
    
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='廣告加盟商管理')
        self.test_driver.func_select(text='推廣連結管理')
    
    def tearDown(self):
        pass
    
    def test_rank_gpg(self):
        """測試層級-總廣告商"""
        self.test_driver.scroll_select(label_text='層級', text='總廣告商')
        self.test_driver.search_button()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        self.assertEqual(res, '總廣告商')
    
    def test_rank_A_agent(self):
        """測試層級-特約經銷"""
        self.test_driver.scroll_select(label_text='層級', text='特約經銷')
        self.test_driver.search_button()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        self.assertEqual(res, '特約經銷')
    
    def test_rank_B_agent(self):
        """測試層級-特約經銷"""
        self.test_driver.scroll_select(label_text='層級', text='區域總經銷')
        self.test_driver.search_button()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        self.assertEqual(res, '區域總經銷')
    
    def test_rank_C_agent(self):
        """測試層級-廣告代理"""
        self.test_driver.scroll_select(label_text='層級', text='廣告代理')
        self.test_driver.search_button()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        self.assertEqual(res, '廣告代理')
    
    def test_status_open(self):
        """測試狀態-啟用"""
        self.test_driver.scroll_select(label_text='狀態', text='啟用')
        self.test_driver.search_button()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[9]/div/div').get_attribute('aria-checked')
        self.assertEqual(res, 'true')
        
    def test_status_close(self):
        """測試狀態-啟用"""
        self.test_driver.scroll_select(label_text='狀態', text='停用')
        self.test_driver.search_button()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[9]/div/div').get_attribute('aria-checked')
        self.assertEqual(res, 'false')
    
    def test_memberID(self):
        """測試會員ID搜尋"""
        self.test_driver.scroll_select(label_text='搜尋類型', text='會員ID')
        self.test_driver.input_text(label_text='搜尋資料',text='2')
        self.test_driver.search_button()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[2]/div/div[1]/div/span').text
        self.assertEqual(res, '2')