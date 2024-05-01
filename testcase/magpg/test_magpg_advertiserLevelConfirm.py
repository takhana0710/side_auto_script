from testcase.gpg2_chromeset import ma_driver_eng, clean_resource, progressNotify
from selenium.webdriver.common.by import By
from testcase.HTMLTestReportCN import HTMLTestRunner
from script.utils import TimeSelect
from datetime import datetime
import unittest
import time
time_select = TimeSelect()
class Test_Deposit(unittest.TestCase):
    """加盟商等級確認"""
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='廣告加盟商管理')
        self.test_driver.func_select(text='加盟商等級確認')
    
    def tearDown(self):
        pass
    
    def test_select_datetime(self):
        """測試搜尋時間區間資料"""
        # self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='申請時間')
        self.test_driver.driver.find_element(By.XPATH,'//form/div[1]/div/div/input').send_keys(time_select.MonthEnd()[:10])
        self.test_driver.driver.find_element(By.XPATH, '//form/div[2]').click()
        self.test_driver.driver.find_element(By.XPATH,'//button/span[text()="搜尋"]').click()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[2]/div').text
        res = datetime.strptime(res, '%Y-%m-%d %H:%M:%S')
        start = datetime.strptime(time_select.MonthStart()[:10], '%Y-%m-%d')
        end = datetime.strptime(time_select.MonthEnd()[:10]+' 23:59:59', '%Y-%m-%d %H:%M:%S')
        self.assertTrue(start <= res <= end)
        
    def test_agent_account(self):
        """測試加盟商帳號"""
        self.test_driver.input_text(label_text='加盟商帳號',text='GenesisPerfectGame')
        self.test_driver.driver.find_element(By.XPATH,'//button/span[text()="搜尋"]').click()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[3]/div').text
        self.assertEqual(res,'GenesisPerfectGame')
    
    def test_agent_nickname(self):
        """測試加盟商名稱"""
        self.test_driver.input_text(label_text='加盟商名稱',text='gpg_GPG')
        self.test_driver.driver.find_element(By.XPATH,'//button/span[text()="搜尋"]').click()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[4]/div').text
        self.assertEqual(res,'gpg_GPG')
    
    def test_status(self):
        """測試處理進度搜尋"""
        self.test_driver.scroll_select(label_text='處理進度',text='申請中')
        self.test_driver.driver.find_element(By.XPATH,'//button/span[text()="搜尋"]').click()
        time.sleep(2)
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[6]/div').text
        self.assertEqual(res,'申請中')
        
    