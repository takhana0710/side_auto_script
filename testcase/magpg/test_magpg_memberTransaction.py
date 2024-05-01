import unittest
from testcase.gpg2_chromeset import ma_driver_eng, clean_resource, progressNotify
from selenium.webdriver.common.by import By
import time
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
from script.utils import TimeSelect
from datetime import datetime

time_select = TimeSelect()


class Test_MemberTransaction(unittest.TestCase):
    """會員交易紀錄"""
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='報表管理')
        self.test_driver.func_select(text='會員交易紀錄')
    
    def tearDown(self):
        pass
    
    def test_select_type_sent_nickname(self):
        """測試搜尋類型_贈與方會員暱稱"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='搜尋類型', text='贈與方會員暱稱')
        self.test_driver.input_text(label_text='搜尋資料', text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[2]/div/span').text
        self.assertEqual('  ', res)
    
    def test_select_type_sent_id(self):
        """測試搜尋類型_贈與方會員ID"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='搜尋類型', text='贈與方會員ID')
        self.test_driver.input_text(label_text='搜尋資料', text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[1]/div/span').text
        self.assertEqual('  ', res)
    
    def test_select_type_sent_phone(self):
        """測試搜尋類型_贈與方手機號"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='搜尋類型', text='贈與方手機號')
        self.test_driver.input_text(label_text='搜尋資料', text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[3]/div/span').text
        self.assertEqual('  ', res)
    
    def test_select_type_get_nickname(self):
        """測試搜尋類型_接收方會員暱稱"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='搜尋類型', text='接收方會員暱稱')
        self.test_driver.input_text(label_text='搜尋資料', text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[2]/div/span').text
        self.assertEqual('  ', res)
    
    def test_select_type_get_id(self):
        """測試搜尋類型_接收方會員ID"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='搜尋類型', text='接收方會員ID')
        self.test_driver.input_text(label_text='搜尋資料', text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[1]/div/span').text
        self.assertEqual('  ', res)
    
    def test_select_type_get_phone(self):
        """測試搜尋類型_接收方手機號"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='搜尋類型', text='接收方手機號')
        self.test_driver.input_text(label_text='搜尋資料', text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//table[@class="el-table__body"]/tbody/tr/td[3]/div/div[3]/div/span').text
        self.assertEqual('  ', res)
    
    def test_select_type_coinGold(self):
        """測試搜尋類型_金幣"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='幣別', text='金幣')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('金幣', res)
    
    def test_select_type_coinSliver(self):
        """測試搜尋類型_銀幣"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='幣別', text='銀幣')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('銀幣', res)
    
    def test_select_datetime(self):
        """測試搜尋時間區間資料"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//table[@class="el-table__body"]/tbody/tr/td[10]/div/span').text
        res = datetime.strptime(res, '%Y-%m-%d %H:%M:%S')
        start = datetime.strptime(time_select.MonthStart()[:10], '%Y-%m-%d')
        end = datetime.strptime(time_select.MonthEnd()[:10], '%Y-%m-%d')
        self.assertTrue(start <= res <= end)
