import time
import unittest
from selenium.webdriver.common.by import By
import warnings
from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify
from testcase.HTMLTestReportCN import HTMLTestRunner
"""
贈禮-單元測試
規格文件整理 
有初設密碼 需要收簡訊
金幣快速面額 3000,5000, 10,000
銀幣快速面額 100,000,300,000,500,000
金幣送禮金額，最低3,000 (更動於2021/12/21)
銀幣送禮金額，最低100,000
"""

class Test_sendPresent(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()
        
    @classmethod
    def setUpClass(cls):
        progressNotify(message='贈禮打包測試開始')
    
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='贈禮打包測試完成')

    def test_sendPresent_gold_member(self):
        """測試會員模式下贈禮-金幣"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin()
        self.test_driver.sendPresent()

    def test_sendPresent_sliver_member(self):
        """測試會員模式下贈禮-銀幣"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin(coin='sliver')
        self.test_driver.sendPresent()

    def test_sendPresent_gold_agentMember(self):
        """測試代理會員模式下贈禮-金幣"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin()
        self.test_driver.sendPresent()

    def test_sendPresent_sliver_agentMember(self):
        """測試代理會員模式下贈禮-銀幣"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin(coin='sliver')
        self.test_driver.sendPresent()

    def test_sendPresent_resetPassword_agentMember(self):
        """測試代理會員模式下寄送重設密碼簡訊"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.driver.find_element(By.XPATH, '//div[text()="送禮"]').click()
        self.test_driver.driver.find_element(By.XPATH, '//div[text()="忘記贈禮密碼？"]').click()
        self.assertEqual(self.test_driver.driver.find_element(By.XPATH, '//div[text()="請輸入您收到的簡訊驗證碼"]').text,'請輸入您收到的簡訊驗證碼')

    def test_sendPresent_gold_quickButton_member(self):
        """測試會員模式下金幣快速按鈕是否累加"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin()
        list(map(lambda x: x.click(), self.test_driver.driver.find_elements(By.XPATH,'//button[contains(@class,"gift-packing__quick-item")]')))
        self.assertEqual('總共金幣 21,000', self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"packing__count")]').text)

    def test_sendPresent_sliver_quickButton_member(self):
        """測試會員模式下金幣快速按鈕是否累加"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin(coin='sliver')
        list(map(lambda x: x.click(), self.test_driver.driver.find_elements(By.XPATH,'//button[contains(@class,"gift-packing__quick-item")]')))
        self.assertEqual('總共銀幣 1,000,000',self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"packing__count")]').text)

    def test_sendPresent_gold_quickButton_agentMember(self):
        """測試代理會員模式下金幣快速按鈕是否累加"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin()
        list(map(lambda x: x.click(), self.test_driver.driver.find_elements(By.XPATH,'//button[contains(@class,"gift-packing__quick-item")]')))
        self.assertEqual('總共金幣 21,000', self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"packing__count")]').text)

    def test_sendPresent_sliver_quickButton_agentMember(self):
        """測試代理會員模式下銀幣快速按鈕是否累加"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin(coin='sliver')
        list(map(lambda x: x.click(), self.test_driver.driver.find_elements(By.XPATH,'//button[contains(@class,"gift-packing__quick-item")]')))
        self.assertEqual('總共銀幣 1,000,000',self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"packing__count")]').text)

    def test_sendPresent_gold_lowMin_member(self):
        """測試會員模式下金幣最小值是否會有提示警告提示"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin()
        self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"minus")]').click()
        self.assertEqual('最低贈禮為3,000金幣', self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"packing__count")]').text)

    def test_sendPresent_gold_lowMin_agentMember(self):
        """測試代理會員模式下金幣最小值是否會有警告提示"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin()
        self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"minus")]').click()
        self.assertEqual('最低贈禮為3,000金幣', self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"packing__count")]').text)

    def test_sendPresent_sliver_lowMin_member(self):
        """測試會員模式下銀幣最小值是否會有警告提示"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin(coin='sliver')
        self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"minus")]').click()
        self.assertEqual('最低贈禮為100,000銀幣', self.test_driver.driver.find_element(By.XPATH,
                                                                                '//div[contains(@class,"packing__count")]').text)

    def test_sendPresent_sliver_lowMin_agentMember(self):
        """測試代理會員模式下銀幣最小值是否會有警告提示"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin(coin='sliver')
        self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"minus")]').click()
        self.assertEqual('最低贈禮為100,000銀幣', self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"packing__count")]').text)

    def test_sendPresent_gold_Max_member(self):
        """測試代理會員模式下金幣最大值是否會有警告提示(一千萬上限)"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin()
        self.test_driver.driver.find_element(By.XPATH,'//input[@id="number__input"]').clear()
        self.test_driver.driver.find_element(By.XPATH,'//input[@id="number__input"]').send_keys(10000001)
        self.test_driver.driver.find_element(By.XPATH,'//button[contains(@class,"packing__submit") and text()="完成"]').click()
        time.sleep(1)
        self.assertEqual('超過交易金額上／下限',self.test_driver.driver.find_element(By.XPATH, '//div[contains(@id,"message")]').text)

    def test_sendPresent_sliver_Max_member(self):
        """測試代理會員模式下銀幣最大值是否會有警告提示(10億)"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect(fun_text='會員中心')
        self.test_driver.choiceCoin(coin='sliver')
        self.test_driver.driver.find_element(By.XPATH,'//input[@id="number__input"]').clear()
        self.test_driver.driver.find_element(By.XPATH,'//input[@id="number__input"]').send_keys(1000000001)
        self.test_driver.driver.find_element(By.XPATH,'//button[contains(@class,"bg-giftBtnBg") and text()="完成"]').click()
        time.sleep(1)
        self.assertEqual('超過交易金額上／下限',self.test_driver.driver.find_element(By.XPATH, '//div[contains(@id,"message")]').text)
        
    


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
