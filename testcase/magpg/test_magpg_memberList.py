import unittest
from testcase.gpg2_chromeset import ma_driver_eng,clean_resource,progressNotify
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.by import By
import time
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner

class Test_MemberList(unittest.TestCase):
    """會員列表"""
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='會員管理')
        self.test_driver.func_select(text='會員列表')
    def tearDown(self):
       pass
    def test_select_vip(self):
        """測試VIP欄位"""
        self.test_driver.scroll_select(label_text='VIP等級',text='VIP 5')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[6]/div').text
        self.assertEqual('5',res)
    def test_select_agent(self):
        """測試上層廣告商欄位"""
        self.test_driver.scroll_select(label_text='上層廣告加盟商',text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div/div/div/span').text
        self.assertEqual('  ',res)
    def test_select_status(self):
        """測試狀態欄位"""
        self.test_driver.scroll_select(label_text='狀態',text='停用')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[7]/div/div').text
        self.assertEqual('停用',res)
    def test_select_type_mid(self):
        """測試搜尋類型_id"""
        self.test_driver.scroll_select(label_text='搜尋類型',text='會員ID')
        self.test_driver.search_button()
        res = self.test_driver.getAlertMessage()
        self.assertEqual('搜尋資料格式錯誤',res)
    
    def test_select_type_phone(self):
        """測試搜尋類型_手機號"""
        self.test_driver.scroll_select(label_text='搜尋類型',text='手機號')
        self.test_driver.input_text(label_text='搜尋資料',text='+  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[3]/div/div/span').text
        self.assertEqual('+  ',res)
        
    def test_select_type_ip(self):
        """測試搜尋類型_登入ip"""
        self.test_driver.scroll_select(label_text='搜尋類型',text='登入IP')
        self.test_driver.input_text(label_text='搜尋資料',text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[12]/div/div[2]').text
        self.assertEqual('  ',res)
    
    def test_select_type_nickname(self):
        """測試搜尋類型_暱稱"""
        self.test_driver.scroll_select(label_text='搜尋類型',text='會員暱稱')
        self.test_driver.input_text(label_text='搜尋資料',text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[4]/div/div/span').text
        self.assertEqual('  ',res)
    