import unittest
from testcase.gpg2_chromeset import env, ma_api,BackAPI
import logging
import inspect

class Test_Index(unittest.TestCase):
    """測試首頁"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_TokenMenu_API(self):
        """測試總代理的權限選單是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.token_menu.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_TokenMenu_API(self):
        """測試A代理的權限選單是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.token_menu.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_TokenMenu_API(self):
        """測試B代理的權限選單是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.token_menu.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_TokenMenu_API(self):
        """測試C代理的權限選單是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.token_menu.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_GPG_AdvertisersData_API(self):
        """測試總代理的代理資料是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.home_AdvertisersData.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_AdvertisersData_API(self):
        """測試A代理的代理資料是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.home_AdvertisersData.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_AdvertisersData_API(self):
        """測試B代理的代理資料是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.home_AdvertisersData.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_AdvertisersData_API(self):
        """測試C代理的代理資料是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.home_AdvertisersData.value)
        self.assertEqual('Success', res['Status']['Message'])
