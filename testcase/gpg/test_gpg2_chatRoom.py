import unittest
from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify
from selenium.webdriver.common.by import By
from testcase.HTMLTestReportCN import HTMLTestRunner
import warnings

class Test_ChatRoom(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()
    @classmethod
    def setUpClass(cls):
        progressNotify(message='聊天室測試開始')
        
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='聊天室測試完成')

    def test_chatRoomIcon_guest(self):
        """測試訪客模式下是否有聊天入口"""
        self.test_driver.loginV2(identity='guest')
        res = self.test_driver.driver.find_element(By.XPATH, '//img[contains(@class,"message__img")]')
        self.assertIsNotNone(res)

    def test_chatRoomIcon_member(self):
        """測試會員模式下是否有聊天入口"""
        self.test_driver.loginV2()
        res = self.test_driver.driver.find_element(By.XPATH, '//img[contains(@class,"message__img")]')
        self.assertIsNotNone(res)

    def test_chatRoomIcon_memberAgent(self):
        """測試代理會員模式下是否有聊天入口"""
        self.test_driver.loginV2(identity='agent')
        res = self.test_driver.driver.find_element(By.XPATH, '//img[contains(@class,"message__img")]')
        self.assertIsNotNone(res)

    def test_chatGPGMemberGuide_guest(self):
        """測試訪客模式聊天室系統客服"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.driver.find_element(By.XPATH, '//img[contains(@class,"message__img")]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"drawer__view")]')
        self.assertIsNotNone(res)

    def test_chatGPGMemberGuide_member(self):
        """測試會員模式聊天室系統客服"""
        self.test_driver.loginV2()
        self.test_driver.chatRoom()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//div[contains(@class,"chat-item__name") and text()="GPG會員提示"]').text
        self.assertEqual(res, 'GPG會員提示')

    def test_chatGPGMemberGuide_memberAgent(self):
        """測試代理會員模式聊天室系統客服"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.chatRoom()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//div[contains(@class,"chat-item__name") and text()="GPG會員提示"]').text
        self.assertEqual(res, 'GPG會員提示')

    def test_SendChat_guest(self):
        """測試訪客模式下是否可以聊天"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.driver.find_element(By.XPATH, '//img[contains(@class,"message__img")]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"drawer__view")]')
        self.assertIsNotNone(res)

    def test_chatGPGService_guest(self):
        """測試訪客模式聊天室系統客服"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.driver.find_element(By.XPATH, '//img[contains(@class,"message__img")]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"drawer__view")]')
        self.assertIsNotNone(res)

    def test_chatGPGService_member(self):
        """測試會員模式聊天室系統客服"""
        self.test_driver.loginV2()
        self.test_driver.chatRoom()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//div[contains(@class,"chat-item__name") and text()="GPG系統客服"]').text
        self.assertEqual(res, 'GPG系統客服')

    def test_chatGPGService_memberAgent(self):
        """測試代理會員聊天室系統客服"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.chatRoom()
        res = self.test_driver.driver.find_element(By.XPATH,
                                                   '//div[contains(@class,"chat-item__name") and text()="GPG系統客服"]').text
        self.assertEqual(res, 'GPG系統客服')

    def test_chatSearchFriend_guest(self):
        """測試訪客模式聊天室搜尋"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.driver.find_element(By.XPATH, '//img[contains(@class,"message__img")]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"drawer__view")]')
        self.assertIsNotNone(res)

    def test_chatSearchFriend_member(self):
        """測試會員模式聊天室搜尋"""
        self.test_driver.loginV2()
        self.test_driver.chatRoom()
        self.test_driver.Addfriend()
        self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"chat-aside__icon")]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[@class="chat-search__container"]')
        self.assertIsNotNone(res)

    def test_chatSearchFriend_memberAgent(self):
        """測試代理會員聊天室搜尋"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.chatRoom()
        self.test_driver.Addfriend()
        self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"chat-aside__icon")]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[@class="chat-search__container"]')
        self.assertIsNotNone(res)

    def test_chatQRCode_guest(self):
        """測試訪客模式聊天室的是否有QRCode"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.driver.find_element(By.XPATH, '//img[contains(@class,"message__img")]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"drawer__view")]')
        self.assertIsNotNone(res)
    def test_QRCode_member(self):
        """測試會員模式聊天室的是否有QRCode"""
        self.test_driver.loginV2()
        self.test_driver.chatRoom()
        self.test_driver.Addfriend()
        self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"chat-aside__icon")]').click()
        self.test_driver.driver.find_element(By.XPATH, '//div[@class="chat-aside__container"]/div/div[2]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"qr-code__label")]').text
        self.assertEqual(res, '即將推出')

    def test_QRCode_memberAgent(self):
        """測試代理會員聊天室的是否有QRCode"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.chatRoom()
        self.test_driver.Addfriend()
        self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"chat-aside__icon")]').click()
        self.test_driver.driver.find_element(By.XPATH, '//div[@class="chat-aside__container"]/div/div[2]').click()
        res = self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"qr-code__label")]').text
        self.assertEqual(res, '即將推出')


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
