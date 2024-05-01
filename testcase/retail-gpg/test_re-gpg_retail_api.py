import unittest
from testcase.gpg2_chromeset import BackAPI,ma_api
import logging
import inspect
class Test_Retail(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_retail_onSiteOrderList(self):
        """測試兌換紀錄API是否是存活"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = ma_api(account=' ',password=' ')
        res = self.api.apiGetData(method='get',
                             payload={'Skip': 0,'Show': 10,'Field':'OrderCreateTime',
                                      'OrderType':'desc','IsFuzzySearch':True},
                             api_url=BackAPI.coupon_onSiteOrderList.value)
        self.assertEqual('Success', res['Status']['Message'])
        
    def test_retail_storeMenu(self):
        """測試端點核銷資訊API是否是存活"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = ma_api(account=' ', password=' ')
        res = self.api.apiGetData(method='get',
                                  payload={},
                                  api_url=BackAPI.coupon_order_storeMenu.value)
        self.assertEqual('Success', res['Status']['Message'])
        
    def test_retail_OnsiteReport(self):
        """測試兌換總匯表API是否是存活"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = ma_api(account=' ', password=' ')
        res = self.api.apiGetData(method='get',
                                  payload={'IsFuzzySearch': True,'Skip': 0,'Show': 10,'Field': 'VoucherId','OrderType': 'desc'},
                                  api_url=BackAPI.coupon_order_onSiteReport.value)
        self.assertEqual('Success', res['Status']['Message'])
    def test_retail_onSiteOrderList_field_(self):
        """測試欄位"""
        