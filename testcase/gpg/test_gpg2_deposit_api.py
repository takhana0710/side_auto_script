import unittest
from testcase.gpg2_chromeset import driver_eng, clean_resource, progressNotify, gpg_api, FontAPI,env
from testcase.gpg_minipet_sp import get_mail
import asyncio
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner


class Test_Deposit_api(unittest.TestCase):
    """測試禮包API派發與內容"""

    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        # pass
        self.test_driver.exit()

    @classmethod
    def setUpClass(cls):
        progressNotify(message='儲值API測試開始')

    @classmethod
    def tearDownClass(cls):
        progressNotify(message='儲值API測試完成')

    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_BuyPackage_api(self):
        """測試API_BuyPackage"""
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='post', api_url=FontAPI.electronicMall_buyPackage.value,
                            data={"PackageID": 10127, "UniformInvoiceInfo": {
                                "DonateMark": 0, "CarrierType": "3J0002", "CarrierId": "/H2PL7A5",
                                "BuyerEmailAddress": "huahung@ceis.tw"}, "Quantity": "1"})
        self.assertEqual(res['Status']['Message'],'派發禮包成功')

    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_BuyPackage_api_canBasic(self):
        """測試API_礦寵開工禮包"""
        member = '+  2'
        self.test_driver.loginV2(passredis=True,register=True,phone=member)
        self.api = gpg_api(token=self.test_driver.token)
        self.api.apiGetData(method='post', api_url=FontAPI.electronicMall_buyPackage.value,data={"PackageID":20012,"UniformInvoiceInfo":{"DonateMark":1,"NPOBAN":"919"},"Quantity":1})
        data = asyncio.get_event_loop().run_until_complete(get_mail(token=self.test_driver.mini))
        self.assertEqual(bool(data['data']['list'][0]['title']=='礦寵開工禮包-罐頭') and bool(data['data']['list'][0]['gId']==13000),True) # 礦寵開工禮包

    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_BuyPackage_api_canHighest(self):
        """測試API_超營養大禮包"""
        member = '+  1'
        self.test_driver.loginV2(passredis=True,register=True,phone=member)
        self.api = gpg_api(token=self.test_driver.token)
        self.api.apiGetData(method='post', api_url=FontAPI.electronicMall_buyPackage.value,data={"PackageID":30013,"UniformInvoiceInfo":{"DonateMark":1,"NPOBAN":"919"},"Quantity":1})
        data = asyncio.get_event_loop().run_until_complete(get_mail(token=self.test_driver.mini))
        # print(data)
        self.assertEqual(bool(data['data']['list'][0]['title']=='超營養升級大補包-高級神奇罐頭') and bool(data['data']['list'][0]['gId']==13002),True) # 超營養大禮包

    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_BuyPackage_api_rich1(self):
        """測試API_富豪沙灘派對"""
        member = '+  3'
        self.test_driver.loginV2(passredis=True, register=True, phone=member)
        self.api = gpg_api(token=self.test_driver.token)
        self.api.apiGetData(method='post', api_url=FontAPI.electronicMall_buyPackage.value,
                            data={"PackageID":30704,"UniformInvoiceInfo":{"DonateMark":1,"NPOBAN":"919"},"Quantity":1})
        data = asyncio.get_event_loop().run_until_complete(get_mail(token=self.test_driver.mini))
        self.assertEqual
        (bool(data['data']['list'][0]['title'] == '富豪沙灘派對-艷陽沙灘' and data['data']['list'][0]['gId'] == 41001) and
        (bool(data['data']['list'][1]['title'] == '富豪沙灘派對-艷陽沙灘' and data['data']['list'][1]['gId'] == 32015)) and
        (bool(data['data']['list'][2]['title'] == '富豪沙灘派對-艷陽沙灘' and data['data']['list'][2]['gId'] == 2017)) and
        (bool(data['data']['list'][3]['title'] == '富豪沙灘派對-艷陽沙灘' and data['data']['list'][3]['gId'] == 23002)) and
        (bool(data['data']['list'][4]['title'] == '富豪沙灘派對-艷陽沙灘' and data['data']['list'][4]['gId'] == 1002)) ,True)  # 富豪禮包

    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_BuyPackage_api_rich2(self):
        """測試API_好野櫻花季"""
        member = '+  4'
        self.test_driver.loginV2(passredis=True, register=True, phone=member)
        self.api = gpg_api(token=self.test_driver.token)
        self.api.apiGetData(method='post', api_url=FontAPI.electronicMall_buyPackage.value,data={"PackageID":30701,"UniformInvoiceInfo":{"DonateMark":1,"NPOBAN":"919"},"Quantity":1})
        data = asyncio.get_event_loop().run_until_complete(get_mail(token=self.test_driver.mini))
        self.assertEqual
        (bool(data['data']['list'][0]['title'] == '好野櫻花季-黑糖' and data['data']['list'][0]['gId'] == 2026) and
        (bool(data['data']['list'][1]['title'] == '好野櫻花季-黑糖' and data['data']['list'][1]['gId'] == 41000)) and
        (bool(data['data']['list'][2]['title'] == '好野櫻花季-黑糖' and data['data']['list'][2]['gId'] == 32014)) and
        (bool(data['data']['list'][3]['title'] == '好野櫻花季-黑糖' and data['data']['list'][3]['gId'] == 2017)) and
        (bool(data['data']['list'][4]['title'] == '好野櫻花季-黑糖' and data['data']['list'][4]['gId'] == 23005)) ,True)
    # def test_BuyPackage_api_event(self):
    #     """測試API_新春兔給樂"""
    #     member = '+  6'
    #     self.test_driver.loginV2(passredis=True, register=True, phone=member)
    #     self.api = gpg_api(token=self.test_driver.token)
    #     self.api.apiGetData(method='post', api_url=FontAPI.electronicMall_buyPackage.value,data={"PackageID":31016,"UniformInvoiceInfo":{"DonateMark":1,"NPOBAN":"919"},"Quantity":1})
    #     data = asyncio.get_event_loop().run_until_complete(get_mail(token=self.test_driver.mini))
    #     self.assertEqual
    #     (bool(data['data']['list'][0]['title'] == '兔給樂紅包-咻咻衝天炮' and data['data']['list'][0]['gId'] == 10063) and
    #     (bool(data['data']['list'][1]['title'] == '兔給樂紅包-咻咻衝天炮' and data['data']['list'][1]['gId'] == 32029)) and
    #     (bool(data['data']['list'][2]['title'] == '兔給樂紅包-咻咻衝天炮' and data['data']['list'][2]['gId'] == 10006)) ,True)
    """
    2022/12/23 備註:
      api端以使用restful+礦寵websocket測試禮包之派發與內容
      實體物品商城後續進行api端測試
    """


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
