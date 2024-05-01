import unittest
from testcase.gpg2_chromeset import ma_driver_eng,clean_resource,progressNotify
from selenium.webdriver.common.by import By
import time
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
from script.utils import TimeSelect
from datetime import datetime
time_select=TimeSelect()

class Test_MemberWalletChange(unittest.TestCase):
    """會員點數異動紀錄"""
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='報表管理')
        self.test_driver.func_select(text='會員點數異動紀錄')
    def tearDown(self):
        pass
    def test_select_type_nickname(self):
        """測試搜尋類型_暱稱"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='搜尋類型',text='會員暱稱')
        self.test_driver.input_text(label_text='搜尋資料',text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[4]/div/div/span').text
        print(self.test_driver.proxy.har)
        self.assertEqual('  ',res)
    
    def test_select_type_coinGold(self):
        """測試搜尋類型_金幣"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='幣別',text='金幣')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[6]/div').text
        self.assertEqual('金幣',res)
    
    def test_select_type_coinSliver(self):
        """測試搜尋類型_銀幣"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='幣別',text='銀幣')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[6]/div').text
        self.assertEqual('銀幣',res)
    
    def test_select_type_phone(self):
        """測試搜尋類型_手機"""
        self.test_driver.input_date(time_select.MonthStart()[:10],time_select.MonthStart()[11:19],label_text='起始時間')
        self.test_driver.scroll_select(label_text='搜尋類型',text='手機號')
        self.test_driver.input_text(label_text='搜尋資料',text='  ')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[3]/div/div/span').text
        self.assertEqual('  ',res)
        
    def test_select_datetime(self):
        """測試搜尋時間區間資料"""
        self.test_driver.input_date(time_select.MonthStart()[:10],time_select.MonthStart()[11:19],label_text='起始時間')
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[10]/div/span').text
        res = datetime.strptime(res,'%Y-%m-%d %H:%M:%S')
        start=datetime.strptime(time_select.MonthStart()[:10],'%Y-%m-%d')
        end=datetime.strptime(time_select.MonthEnd()[:10],'%Y-%m-%d')
        self.assertTrue(start<=res<=end)
        
    def test_select_type_walletChange(self):
        """測試搜尋類型_錢包金額補正"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='異動類型',text='錢包金額補正')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('錢包金額補正',res)
    
    def test_select_type_walletTransfer(self):
        """測試搜尋類型_遊戲轉帳"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='異動類型',text='遊戲轉帳')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('遊戲轉帳',res)
        
    def test_select_type_signIn(self):
        """測試搜尋類型_簽到送禮"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='異動類型',text='簽到送禮')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('簽到送禮',res)
    
    def test_select_type_sentPresentGet(self):
        """測試搜尋類型_會員交易-接收"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='異動類型',text='會員交易-接收')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('會員交易-接收',res)
        
    def test_select_type_sentPresentSent(self):
        """測試搜尋類型_會員交易-贈禮"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='異動類型',text='會員交易-贈禮')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('會員交易-贈禮',res)
    
    def test_select_type_PointChange(self):
        """測試搜尋類型_人工補扣點"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='異動類型',text='人工補扣點')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('人工補扣點',res)
        
    def test_select_type_getMining(self):
        """測試搜尋類型_礦機提領"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='異動類型',text='礦機提領')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('礦機提領',res)
        
    def test_select_type_Deposit(self):
        """測試搜尋類型_儲值禮包入點"""
        self.test_driver.input_date(time_select.MonthStart()[:10], time_select.MonthStart()[11:19], label_text='起始時間')
        self.test_driver.scroll_select(label_text='異動類型',text='儲值禮包入點')
        self.test_driver.search_button()
        res = self.test_driver.driver.find_element(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[5]/div').text
        self.assertEqual('儲值禮包入點',res)
    
    