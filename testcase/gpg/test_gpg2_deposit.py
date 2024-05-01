import time
import unittest
from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify,By
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
import random
import re
class Test_Deposit(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        # pass
        self.test_driver.exit()
    @classmethod
    def setUpClass(cls):
        progressNotify(message='儲值測試開始')
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='儲值測試完成')
    """未來重構 2022/12/15備註"""
    
    """
    2022/12/23 備註:
      這邊UI測試測試流程與欄位
      可能搭配未來未定案之第三種幣別UI測試商城
      api端以使用restful+礦寵websocket測試禮包之派發與內容
    """
    def test_company_code(self):
        """測試統一編號"""
        self.test_driver.loginV2()
        self.test_driver.asideBarSelect(fun_text='商城')
        res = self.test_driver.depositType(type='超值禮包')
        self.test_driver.depositPayWay(pay_way='統一編號', package=res[0],info={'companyName': '羲奕研策股份有限公司', 'companyCode': '83184736'})
        self.test_driver.depositFinishWay()
        
    def test_package_count(self):
        """測試複數禮包(包括加減按鈕)"""
        self.test_driver.loginV2()
        self.test_driver.asideBarSelect(fun_text='商城')
        res = self.test_driver.depositType(type='超值禮包')
        rnd=random.randint(2,10)
        res = self.test_driver.depositPayWay(pay_way='捐贈', package=res[0],info={},count=rnd)
        self.assertEqual(res,str(rnd))
        
    def test_email_pay(self):
        """測試載具email"""
        self.test_driver.loginV2()
        self.test_driver.asideBarSelect(fun_text='商城')
        res = self.test_driver.depositType(type='超值禮包')
        self.test_driver.depositPayWay(pay_way='載具類型', package=res[0],info={'email': 'huahung@ceis.tw', 'cellphoneCode': 'H2PL7A5'})
        self.test_driver.depositFinishWay()
        
    def test_email_nature_pay(self):
        """測試自然人憑證email"""
        self.test_driver.loginV2()
        self.test_driver.asideBarSelect(fun_text='商城')
        res = self.test_driver.depositType(type='超值禮包')
        self.test_driver.depositPayWay(pay_way='載具類型', package=res[0],info={'email': 'huahung@ceis.tw', 'nature': 'AA11111111111111'})
        self.test_driver.depositFinishWay()
        
    def test_donateCode_pay(self):
        """測試愛心碼"""
        self.test_driver.loginV2()
        self.test_driver.asideBarSelect(fun_text='商城')
        res = self.test_driver.depositType(type='超值禮包')
        self.test_driver.depositPayWay(pay_way='捐贈', package=res[0],info={'donateCode': '817123'})
        self.test_driver.depositFinishWay()
        
    def test_donate_pay(self):
        """測試愛心碼"""
        self.test_driver.loginV2()
        self.test_driver.asideBarSelect(fun_text='商城')
        res = self.test_driver.depositType(type='超值禮包')
        self.test_driver.depositPayWay(pay_way='捐贈', package=res[0],info={})
        self.test_driver.depositFinishWay()

    def test_limit_package(self):
        """測試限定禮包是否賣完"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.asideBarSelect(fun_text='商城')
        res = self.test_driver.depositType(type='限量禮包')
        self.test_driver.depositPayWay(pay_way='捐贈', package=res[4],info={})
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"package__item") and contains(@class,"grayscale")]'))
    def test_package_record(self):
        """測試購買禮包是否有在記錄內"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.asideBarSelect(fun_text='商城')
        res = self.test_driver.depositType(type='超值禮包')
        self.test_driver.depositPayWay(pay_way='捐贈', package=res[0],info={})
        time.sleep(2)
        orderId = re.compile('?transId=(.+)',re.S).findall(self.test_driver.driver.current_url).pop()
        self.test_driver.depositFinishWay(way='record')
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,f'//div[text()="{orderId}"]'))


if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())