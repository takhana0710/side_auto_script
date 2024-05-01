import unittest
from testcase.gpg2_chromeset import ma_driver_eng,clean_resource,progressNotify
from selenium.webdriver.common.by import By
import time
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
from script.utils import TimeSelect
from datetime import datetime
time_select=TimeSelect()

class Test_PointChange(unittest.TestCase):
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='會員管理')
        self.test_driver.func_select(text='補/扣點紀錄查詢')
    def tearDown(self):
        pass
    def test_select_type_nickname(self):
        """測試搜尋類型_暱稱"""
        self.test_driver.scroll_select(label_text='搜尋類型',text='會員暱稱')
        self.test_driver.input_text(label_text='搜尋資料',text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div/span').text
        self.assertEqual('  ',res)
    def test_select_type_phone(self):
        """測試搜尋類型_手機"""
        self.test_driver.scroll_select(label_text='搜尋類型',text='手機號')
        self.test_driver.input_text(label_text='搜尋資料',text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[4]/div/span').text
        self.assertEqual('  ',res)
    def test_select_datetime(self):
        """測試搜尋時間區間資料"""
        self.test_driver.input_date(time_select.MonthStart()[:10],time_select.MonthStart()[11:19],label_text='起始時間')
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[10]/div/span').text
        res = datetime.strptime(res,'%Y-%m-%d %H:%M:%S')
        start=datetime.strptime(time_select.MonthStart()[:10],'%Y-%m-%d')
        end=datetime.strptime(time_select.MonthEnd()[:10],'%Y-%m-%d')
        self.assertTrue(start<=res<=end)