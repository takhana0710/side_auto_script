import random
import unittest
from testcase.gpg2_chromeset import env, ma_api, BackAPI
from script.utils import TimeSelect
import logging
import inspect
time_select=TimeSelect()
class Test_CustomerServiceChangeRecord(unittest.TestCase):
    """測試補購點紀錄查詢API"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_CustomerServiceChangeRecord_API(self):
        """測試總代理的補扣點紀錄查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.member_customerServiceChangeRecord.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_CustomerServiceChangeRecord_API(self):
        """測試A代理的補扣點紀錄查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.member_customerServiceChangeRecord.value)
        self.assertEqual('', res)

    def test_B_Agent_CustomerServiceChangeRecord_API(self):
        """測試B代理的補扣點紀錄查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.member_customerServiceChangeRecord.value)
        self.assertEqual('', res)

    def test_C_Agent_CustomerServiceChangeRecord_API(self):
        """測試C代理的補扣點紀錄查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'sDate': time_select.MonthStart(),
                                      'eDate': time_select.MonthEnd(),
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.member_customerServiceChangeRecord.value)
        self.assertEqual('', res)

    def test_GPG_CustomerServiceChange_API_goldPlus(self):
        """測試總代理的補扣點新增是否正常成功-金幣加點"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'MemberID': 1,
                                 'Note': "測試API加點--->幣別:金幣 , 金錢：1",
                                 'Point': "1",
                                 'PointTypeID': 1,
                             },
                             api_url=BackAPI.member_customerServiceChange.value)
        self.assertEqual('Success', res['Status']['Message'])
        
    def test_GPG_CustomerServiceChange_API_goldSub(self):
        """測試總代理的補扣點新增是否正常成功-金幣扣點"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'MemberID': 1,
                                 'Note': "測試API扣點--->幣別:金幣 , 金錢：1",
                                 'Point': "-1",
                                 'PointTypeID': 1,
                             },
                             api_url=BackAPI.member_customerServiceChange.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_GPG_CustomerServiceChange_API_sliverPlus(self):
        """測試總代理的補扣點新增是否正常成功-銀幣加點"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'MemberID': 1,
                                 'Note': "測試API加點--->幣別:銀幣 , 金錢：1",
                                 'Point': "1",
                                 'PointTypeID': 2,
                             },
                             api_url=BackAPI.member_customerServiceChange.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_GPG_CustomerServiceChange_API_sliverSub(self):
        """測試總代理的補扣點新增是否正常成功-銀幣扣點"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'MemberID': 1,
                                 'Note': "測試API扣點--->幣別:銀幣 , 金錢：1",
                                 'Point': "-1",
                                 'PointTypeID': 2,
                             },
                             api_url=BackAPI.member_customerServiceChange.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_CustomerServiceChange_API(self):
        """測試A代理的補扣點新增是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'MemberID': 1,
                                 'Note': "測試API加點--->幣別:金幣 , 金錢：1",
                                 'Point': "1",
                                 'PointTypeID': 1,
                             },
                             api_url=BackAPI.member_customerServiceChange.value)
        self.assertEqual('', res)

    def test_B_Agent_CustomerServiceChange_API(self):
        """測試B代理的補扣點新增是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'MemberID': 1,
                                 'Note': "測試API加點--->幣別:金幣 , 金錢：1",
                                 'Point': "1",
                                 'PointTypeID': 1,
                             },
                             api_url=BackAPI.member_customerServiceChange.value)
        self.assertEqual('', res)

    def test_C_Agent_CustomerServiceChange_API(self):
        """測試C代理的補扣點新增是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'MemberID': 1,
                                 'Note': "測試API加點--->幣別:金幣 , 金錢：1",
                                 'Point': "1",
                                 'PointTypeID': 1,
                             },
                             api_url=BackAPI.member_customerServiceChange.value)
        self.assertEqual('', res)

    def test_GPG_MemberInfoID_API(self):
        """測試總代理的會員查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={'MemberId': 1},
                             api_url=BackAPI.infos_memberInfo.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_MemberInfoID_API(self):
        """測試A代理的會員查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'MemberId': 1},
                             api_url=BackAPI.infos_memberInfo.value)
        self.assertEqual('', res)

    def test_B_Agent_MemberInfoID_API(self):
        """測試B代理的會員查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'MemberId': 1},
                             api_url=BackAPI.infos_memberInfo.value)
        self.assertEqual('', res)

    def test_C_Agent_MemberInfoID_API(self):
        """測試C代理的會員查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'MemberId': 1},
                             api_url=BackAPI.infos_memberInfo.value)
        self.assertEqual('', res)

    def test_GPG_MemberInfoLikeName_API(self):
        """測試總代理的會員查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={'NickNameLike': "GPG"},
                             api_url=BackAPI.infos_memberInfo.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_MemberInfoLikeName_API(self):
        """測試A代理的會員查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'MemberId': 1},
                             api_url=BackAPI.infos_memberInfo.value)
        self.assertEqual('', res)

    def test_B_Agent_MemberInfoLikeName_API(self):
        """測試B代理的會員查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'NickNameLike': "GPG"},
                             api_url=BackAPI.infos_memberInfo.value)
        self.assertEqual('', res)

    def test_C_Agent_MemberInfoLikeName_API(self):
        """測試C代理的會員查詢是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'NickNameLike': "GPG"},
                             api_url=BackAPI.infos_memberInfo.value)
        self.assertEqual('', res)
