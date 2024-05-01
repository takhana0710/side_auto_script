import unittest
from testcase.gpg2_chromeset import ma_driver_eng, clean_resource, progressNotify
from selenium.webdriver.common.by import By
from testcase.HTMLTestReportCN import HTMLTestRunner
from script.utils import TimeSelect
from datetime import datetime

time_select = TimeSelect()


class Test_Deposit(unittest.TestCase):
    """儲值報表"""
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='報表管理')
        self.test_driver.func_select(text='儲值報表')
    
    def tearDown(self):
        pass
    
    def test_select_datetime(self):
        """測試搜尋時間區間資料"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//table[@class="el-table__body"]/tbody/tr/td[10]/div/span').text
        res = datetime.strptime(res, '%Y-%m-%d %H:%M:%S')
        start = datetime.strptime(time_select.MonthStart()[:10], '%Y-%m-%d')
        end = datetime.strptime(time_select.MonthEnd()[:10], '%Y-%m-%d')
        self.assertTrue(start <= res <= end)
