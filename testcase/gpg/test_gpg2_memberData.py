import unittest
from testcase.gpg2_chromeset import driver_eng,env,clean_resource,progressNotify
from selenium.webdriver.common.by import By
import os
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner


class Test_MemberData(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()
        
    @classmethod
    def setUpClass(cls):
        progressNotify(message='會員資料測試開始')
        
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='會員資料測試完成')


    def test_memberData_guest(self):
        """測試訪客模式下會員資料"""

    def test_memberData_member(self):
        """測試會員模式下會員資料"""

    def test_memberData_memberAgent(self):
        """測試代理會員下會員資料"""


    def test_editNick_member(self):
        """測試會員模式下編輯會員名字"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect('會員資料')
        self.test_driver.editNickName(name='mebmerQAABC123')

    def test_editNick_memberAgent(self):
        """測試代理會員模式下編輯會員名字"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect('會員資料')
        self.test_driver.editNickName(name='  ')

    # def test_uploadImage_member(self):
    #     """測試會員模式下上傳會員頭像"""
    #     self.test_driver.loginV2()
    #     self.test_driver.memberSelect('會員資料')
    #     path_to_image  =  os.path.join(os.getcwd(),'testcase\\autoTest.jpg')
    #     self.test_driver.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(path_to_image)

    # def test_uploadImage_memberAgent(self):
    #     """測試代理會員模式下上傳會員頭像"""
    #     self.test_driver.loginV2(identity='agent')
    #     self.test_driver.memberSelect('會員資料')
    #     path_to_image  =  os.path.join(os.getcwd(),'testcase\\autoTest.jpg')
    #     self.test_driver.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(path_to_image)

    def test_inviteCode_member(self):
        """測試會員模式下是否有邀請碼"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect('會員資料')
        res=self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"edit__list")]/div[3]').text
        res = res.replace('\n','')
        self.assertEqual('我的邀請碼{member_introduction}分享邀請碼'.format(member_introduction=env['member_introduction']),res)

    def test_inviteCode_memberAgent(self):
        """測試代理會員模式下是否有邀請碼"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect('會員資料')
        res=self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"edit__list")]/div[3]').text
        res = res.replace('\n','')
        self.assertEqual('我的邀請碼{agent_introduction}分享邀請碼'.format(agent_introduction=env['agent_introduction']),res)

    def test_mobileValidate_member(self):
        """測試會員模式下是否有手機驗證"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect('會員資料')
        res=self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"edit__list")]/div[4]').text
        res = res.replace('\n','')
        self.assertEqual('手機號碼{member_account}已驗證'.format(member_account=env['member_account']),res)

    def test_mobileValidate_memberAgent(self):
        """測試代理會員模式下是否有手機驗證"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect('會員資料')
        res=self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"edit__list")]/div[4]').text
        res = res.replace('\n','')
        self.assertEqual('手機號碼{agent_mobile}已驗證'.format(agent_mobile=env['agent_mobile']),res)

if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())