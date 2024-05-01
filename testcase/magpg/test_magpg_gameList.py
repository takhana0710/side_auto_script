import unittest
from testcase.gpg2_chromeset import ma_driver_eng,clean_resource,progressNotify
from selenium.webdriver.common.by import By

class Test_GameList(unittest.TestCase):
    def setUp(self):
        self.test_driver = ma_driver_eng()
        self.test_driver.login()
        self.test_driver.side_select(text='遊戲管理')
        self.test_driver.func_select(text='遊戲列表')
    def tearDown(self):
        pass
    def test_select_type_VAbattle(self):
        """測試搜尋類型_VAbattle"""
        self.test_driver.scroll_select(label_text='遊戲商',text='')
        self.test_driver.search_button()
        res = len(self.test_driver.driver.find_elements(By.XPATH,'//div[contains(@class,"el-table__body-wrapper")]/table[@class="el-table__body"]/tbody/tr[@class="el-table__row"]'))
        self.assertEqual(5,res)
    
    def test_select_type_ifun(self):
        """測試搜尋類型_ifun"""
        self.test_driver.scroll_select(label_text='遊戲商',text='')
        self.test_driver.search_button()
        res = len(self.test_driver.driver.find_elements(By.XPATH,'//div[contains(@class,"el-table__body-wrapper")]/table[@class="el-table__body"]/tbody/tr[@class="el-table__row"]'))
        self.assertEqual(20,res)
        
    def test_select_type_VASlot(self):
        """測試搜尋類型_VASlot"""
        self.test_driver.scroll_select(label_text='遊戲商',text='')
        self.test_driver.search_button()
        res = len(self.test_driver.driver.find_elements(By.XPATH,'//div[contains(@class,"el-table__body-wrapper")]/table[@class="el-table__body"]/tbody/tr[@class="el-table__row"]'))
        self.assertEqual(50,res)