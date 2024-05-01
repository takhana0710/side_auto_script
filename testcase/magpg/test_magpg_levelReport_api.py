import unittest
from testcase.gpg2_chromeset import env, ma_api,BackAPI
import logging
import inspect
from script.utils import TimeSelect
time_select = TimeSelect()
class Test_LevelReport(unittest.TestCase):
    """測試等級趨勢報表"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_adLvResetGet_API(self):
        """測試總代理的等級重置列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.dataReport_adLvResetGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_adLvResetGet_API(self):
        """測試A代理的權限選單是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag20', password='QAminiag20')
        res = api.apiGetData(method='get', api_url=BackAPI.dataReport_adLvResetGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_adLvResetGet_API(self):
        """測試B代理的權限選單是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag21', password='QAminiag21')
        res = api.apiGetData(method='get', api_url=BackAPI.dataReport_adLvResetGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_adLvResetGet_API(self):
        """測試C代理的權限選單是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag22', password='QAminiag22')
        res = api.apiGetData(method='get', api_url=BackAPI.dataReport_adLvResetGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_GPG_AdLvReport_API(self):
        """測試總代理的代理資料是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', payload={'sDate':time_select.MonthStart(),'eDate':time_select.MonthEnd()},api_url=BackAPI.dataReport_adLvReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_AdLvReport_API(self):
        """測試A代理的代理資料是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag20', password='QAminiag20')
        res = api.apiGetData(method='get', payload={'sDate':time_select.MonthStart(),'eDate':time_select.MonthEnd()},api_url=BackAPI.dataReport_adLvReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_AdLvReport_API(self):
        """測試B代理的代理資料是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag21', password='QAminiag21')
        res = api.apiGetData(method='get', payload={'sDate':time_select.MonthStart(),'eDate':time_select.MonthEnd()},api_url=BackAPI.dataReport_adLvReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_AdLvReport_API(self):
        """測試C代理的代理資料是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag22', password='QAminiag22')
        res = api.apiGetData(method='get', payload={'sDate':time_select.MonthStart(),'eDate':time_select.MonthEnd()},api_url=BackAPI.dataReport_adLvReport.value)
        self.assertEqual('Success', res['Status']['Message'])
        
    def test_GPG_AdLvResetAdd_API(self):
        """測試總代理等級重置是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',data={'Note':''}, api_url=BackAPI.dataReport_adLvResetAdd.value)
        self.assertEqual('Success', res['Status']['Message'])
    def test_A_Agent_AdLvResetAdd_API(self):
        """測試A代理等級重置是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag20', password='QAminiag20')
        res = api.apiGetData(method='post',data={'Note':''}, api_url=BackAPI.dataReport_adLvResetAdd.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_AdLvResetAdd_API(self):
        """測試B代理等級重置是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag21', password='QAminiag21')
        res = api.apiGetData(method='post',data={'Note':''}, api_url=BackAPI.dataReport_adLvResetAdd.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_AdLvResetAdd_API(self):
        """測試C代理等級重置是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='QAminiag22', password='QAminiag22')
        res = api.apiGetData(method='post',data={'Note':''}, api_url=BackAPI.dataReport_adLvResetAdd.value)
        self.assertEqual('Success', res['Status']['Message'])