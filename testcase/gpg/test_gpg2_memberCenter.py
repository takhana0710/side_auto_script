import unittest
from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify
from selenium.webdriver.common.by import By
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner

class Test_MemberCenter(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()
    @classmethod
    def setUpClass(cls):
        progressNotify(message='會員中心測試開始')
    
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='會員中心測試完成')

    def test_memberCenter_guest(self):
        """測試訪客模式下是否有會員中心"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)


    def test_SendPresent_guest(self):
        """測試訪客模式下是否送禮"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_sendPresent_member(self):
        """測試會員模式下是否送禮"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("會員中心")
        self.test_driver.choiceCoin()
        self.test_driver.sendPresent()

    def test_sendPresent_memberAgent(self):
        """測試代理會員下是否送禮"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("會員中心")
        self.test_driver.choiceCoin()
        self.test_driver.sendPresent()

    def test_iconBoard_guest(self):
        """測試訪客模式下頭像框彈窗是否出現"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_iconBoard_member(self):
        """測試會員模式下頭像框彈窗是否出現"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//div[text()="頭像框"]')
        self.assertIsNotNone(res)

    def test_iconBoard_memberAgent(self):
        """測試代理會員下頭像框彈窗是否出現"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//div[text()="頭像框"]')
        self.assertIsNotNone(res)

    def test_mini_guest(self):
        """測試訪客模式下是否有礦機"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_mini_member(self):
        """測試會員模式下是否有礦機"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//button[text()="點我領取"]')
        self.assertIsNotNone(res)

    def test_mini_memberAgent(self):
        """測試代理會員下是否有礦機"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//button[text()="點我領取"]')
        self.assertIsNotNone(res)

    def test_editMemberInfo_guest(self):
        """測試訪客模式下是否編輯會員資料按鈕"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_editMemberInfo_member(self):
        """測試會員模式下是否編輯會員資料按鈕"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//a[@href="/center/edit"]')
        self.assertIsNotNone(res)

    def test_editMemberInfo_memberAgent(self):
        """測試代理會員下是否編輯會員資料按鈕"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//a[@href="/center/edit"]')
        self.assertIsNotNone(res)

    def test_copyLink_guest(self):
        """測試訪客模式下複製邀請連結"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_copyLink_member(self):
        """測試會員模式下複製邀請連結"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"invite-share__container")]/button').text
        self.assertEqual(res,'複製邀請連結')

    def test_copyLink_memberAgent(self):
        """測試代理會員下複製邀請連結"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"invite-share__container")]/button').text
        self.assertEqual(res,'複製邀請連結')

    def test_memberImage_guest(self):
        """測試訪客模式下是否有會員頭像"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_memberImage_member(self):
        """測試會員模式下是否有會員頭像"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text="會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"info__wrap")]/div')
        self.assertIsNotNone(res)

    def test_memberImage_memberAgent(self):
        """測試代理會員下是否有會員頭像"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect(fun_text="會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"info__wrap")]/div')
        self.assertIsNotNone(res)

    def test_memberNickName_guest(self):
        """測試訪客模式下是否有會員暱稱"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_memberNickName_member(self):
        """測試會員模式下是否有會員暱稱"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"info__name")]')
        self.assertIsNotNone(res)

    def test_memberNickName_memberAgent(self):
        """測試代理會員模式下是否有會員暱稱"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"info__name")]')
        self.assertIsNotNone(res)

    def test_memberRecord_guest(self):
        """測試訪客模式下是否有會員交易紀錄"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_memberRecord_member(self):
        """測試會員模式下是否有會員交易紀錄"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("訂單")

    def test_memberRecord_memberAgent(self):
        """測試代理會員模式下是否有會員交易紀錄"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("訂單")

    def test_memberCoin_guest(self):
        """測試訪客模式下是否有會員金銀幣"""
        self.test_driver.memberSelect(fun_text='會員中心')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_memberCoin_member(self):
        """測試會員模式下是否有會員金銀幣"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//img[@src="/img/coin/i_money_gold.svg"]')
        self.assertIsNotNone(res)

    def test_memberCoin_memberAgent(self):
        """測試代理會員模式下是否有會員金銀幣"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("會員中心")
        res = self.test_driver.driver.find_element(By.XPATH,'//img[@src="/img/coin/i_money_gold.svg"]')
        self.assertIsNotNone(res)

if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())