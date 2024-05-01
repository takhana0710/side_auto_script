import time
import unittest
from testcase.gpg2_chromeset import driver_eng,env,ma_api,clean_resource,progressNotify,BackAPI,gpg_api,FontAPI
import warnings
from selenium.webdriver.common.by import By
from testcase.HTMLTestReportCN import HTMLTestRunner

class Test_ChangeCode(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore',ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()
    @classmethod
    def setUpClass(cls):
        progressNotify(message='兌換碼測試開始')
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='兌換碼測試完成')

    # @unittest.skipIf(env['env'] == 'prod','正式站跳過')
    # def test_00_delete(self):
    #     """測試兌換碼測試的前置作業"""
    #     api = ma_api()
    #     member = list()
    #     res =list(map(lambda x:api.apiGetData(method='get', api_url=BackAPI.member_memberList.value
    #     ,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc','IsGuest': False, 'PhoneNumber': x})['Data'],
    #                    []))
    #     for i in res:
    #         member.extend(i)
    #     list(map(lambda x:api.apiGetData(method='post', api_url=BackAPI.member_disable.value,data={"MemberId": x.get('MemberID')}),member))

    def test_ChangeCode_TransactionRecord_ExChangePresent_guest(self):
        """測試訪客模式下是否可以輸入兌換碼"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.orderNo(present_code='2333333',mode='noAlter')
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__view")]'))


    def test_ChangeCode_TransactionRecord_ExChangePresent_member(self):
        """測試會員模式下是否可以兌換禮物並且寫入收禮紀錄"""
        self.test_driver.loginV2()
        self.test_driver.memberSelect("訂單")
        present_code, order_no = self.test_driver.memberSendRecord()
        self.test_driver.orderNo(present_code=present_code,mode='presentChange')
        self.assertIsNotNone(present_code)

    def test_ChangeCode_TransactionRecord_ExChangePresent_agentMember(self):
        """測試代理會員模式下是否可以兌換禮物並且寫入收禮紀錄"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.memberSelect("訂單")
        present_code, order_no = self.test_driver.memberSendRecord()
        self.test_driver.orderNo(present_code=present_code,mode='presentChange')
        self.assertIsNotNone(present_code)

    @unittest.skipIf(env['env'] == 'prod','正式站跳過')
    def test_ChangeCode_PromoteCode_guest(self):
        """測試訪客模式下輸入推廣碼兌換彈窗"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.orderNo(present_code=env['agent_introduction'],mode='noAlter')
        self.api = gpg_api(token='agentToken')
        nickname=self.api.apiGetData(method='get',api_url=FontAPI.member_memberInfo.value)['Data']['NickName'][4:]
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__view")]/div[1]/div[2]/p').text
        self.assertEqual(res,f'立即領取{nickname}送你的大禮包！')

    # @unittest.skipIf(env['env'] == 'prod','正式站跳過')
    # def test_ChangeCode_PromoteCode_agm(self):
    #     """測試會員模式下輸入推廣碼是否能夠掛線註冊成功"""
    #     self.test_driver.loginV2(identity='guest',passredis=True)
    #     self.test_driver.orderNo(present_code=env['agent_introduction'],mode='noAlter')
    #     self.test_driver.loginV2(phone='',validcode='',passredis=True,guestRegister=True)
    #     self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//button[contains(@class,"bg-redBtn")]'))

    # @unittest.skipIf(env['env'] == 'prod','正式站跳過')
    # def test_ChangeCode_PromoteCode_jkf(self):
    #     """測試會員模式下輸入jkf是否能夠掛線註冊成功"""
    #     self.test_driver.loginV2(identity='guest',passredis=True)
    #     self.test_driver.orderNo(present_code='jkf',mode='noAlter')
    #     self.test_driver.loginV2(phone='',validcode='',passredis=True,guestRegister=True)
    #     self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//button[contains(@class,"bg-redBtn")]'))

    def test_ChangeCode_PromoteCode_24hr_agm(self):
        """測試會員24小時後是否可以換線_agm"""
        self.test_driver.loginV2()
        self.test_driver.orderNo(present_code=env['agent_introduction'],mode='noAlter')
        time.sleep(5)
        self.assertEqual(self.test_driver.getAlertMessage(), '好可惜! 您沒抽中禮包，下次再接再厲吧!!')

    def test_ChangeCode_PromoteCode_24hr_jkf(self):
        """測試會員24小時後是否可以換線_jkf"""
        self.test_driver.loginV2()
        self.test_driver.orderNo(present_code='jkf',mode='noAlter')
        self.assertEqual(self.test_driver.getAlertMessage(), '好可惜! 您沒抽中禮包，下次再接再厲吧!!')

    def test_ChangeCode_PromoteCode_agent(self):
        """測試代理會員是否可以換限兌換"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.orderNo(present_code=env['agent_introduction'],mode='noAlter')
        self.assertEqual(self.test_driver.getAlertMessage(), '好可惜! 您沒抽中禮包，下次再接再厲吧!!')

    def test_ChangeCode_PromoteCode_mgm(self):
        """測試會員是否可以使用MGM掛線"""
        self.test_driver.loginV2()
        self.test_driver.orderNo(present_code=env['member_introduction'],mode='noAlter')
        self.assertEqual(self.test_driver.getAlertMessage(), '序號無效，請確認輸入正確的字元')

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())