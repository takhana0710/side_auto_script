import unittest
from testcase.gpg2_chromeset import ma_api, BackAPI
import logging
import inspect
from script.utils import TimeSelect
time_select=TimeSelect()
class Test_presentActivityList_api(unittest.TestCase):
    """兌換券管理"""
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01_GPG_ActivityGet(self):
        """測試總代理的活動列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_activityGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_02_GPG_ActivityAdd(self):
        """測試總代理的新增活動是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post', data={"ActivityName": "  ",
                                                  "StartTime": time_select.MonthStart(),
                                                  "EndTime": time_select.MonthEnd()},
                             api_url=BackAPI.voucher_activityAdd.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_03_GPG_ActivityEdit(self):
        """測試總代理的編輯活動是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = list(filter(lambda x:x.get('ActivityName')=='  ',api.apiGetData(method='get', api_url=BackAPI.voucher_activityGet.value)['Data'])).pop()
        del res['ActivityConditions']
        res['ActivityName']='  Edit'
        res = api.apiGetData(method='post', data=res,api_url=BackAPI.voucher_activityEdit.value)
        self.assertEqual('Success', res['Status']['Message'])
        
    def test_04_GPG_ActivityDel(self):
        """測試總代理的刪除活動是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = list(filter(lambda x:x.get('ActivityName')=='  Edit',api.apiGetData(method='get', api_url=BackAPI.voucher_activityGet.value)['Data'])).pop()
        res = api.apiGetData(method='post',data={"ActivityID":res['ActivityID']},api_url=BackAPI.voucher_activityDel.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_05_GPG_VoucherGet(self):
        """測試總代理的取得兌換券是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',payload={'Skip': 0,'Show': 50,
                                                   'Field': 'VoucherName','OrderType': 'desc',
                                                   'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_voucherGet.value)
        self.assertEqual('Success', res['Status']['Message'])
        
    def test_06_GPG_VoucherAdd(self):
        """測試總代理新增兌換券是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        package = api.apiGetData(method='get',
                             payload={'Skip': 0,'Show': 50,'Field': 'PackageName',
                                      'OrderType': 'desc','IsEnable': 1,
                                      'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_packageGet.value)['Data'].pop()
        activity = api.apiGetData(method='get',payload={'Skip': 0,'Show': 50,
                                                   'Field': 'VoucherName','OrderType': 'desc',
                                                   'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_activityGet.value)['Data'].pop()
        res = api.apiGetData(method='post',data={"VoucherName":'  ',
                                                 "PackageID":package['PackageID'],
                                                 "ActivityID":activity['ActivityID'],"Amount":"2",
                                                 "StartTime": time_select.MonthStart(),
                                                 "EndTime": time_select.MonthEnd()},
                             api_url=BackAPI.voucher_voucherAdd.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_07_GPG_packageExchangeSend(self):
        """測試總代理指定兌換是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        voucher = api.apiGetData(method='get',api_url=BackAPI.voucher_voucherGet.value, payload={'Skip': 0, 'Show': 50,
                                                    'Field': 'VoucherName',
                                                    'OrderType': 'desc',
                                                    'VoucherName': "  ",
                                                    'IsFuzzySearch': True})['Data'].pop()
        agent = api.apiGetData(method='get', api_url=BackAPI.member_advertisersList.value,
                               payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0, 'Show': 99999,
                                        'Field': 'CreateTime', 'OrderType': 'desc', 'NickName': 'QAminiag20'})['Data'].pop()
        member = api.apiGetData(method='post', api_url=BackAPI.infos_memberInfo.value,
                               data={'NickNameLike': '  '})['Data'].pop()
        res = api.apiGetData(method='post',data={"VoucherID":voucher['VoucherID'],"Amount":1,"SenderID":agent['MemberID']
            ,"ReceiverID":[member['MemberID']]},
                             api_url=BackAPI. voucher_packageExchangeSend.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_08_GPG_VoucherEdit(self):
        """測試總代理編輯兌換券是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',api_url=BackAPI.voucher_voucherGet.value, payload={'Skip': 0, 'Show': 50,
                                                    'Field': 'VoucherName',
                                                    'OrderType': 'desc',
                                                    'VoucherName': "  ",
                                                    'IsFuzzySearch': True})['Data'].pop()
        res = api.apiGetData(method='post',
                             data={"VoucherID":res['VoucherID'],"VoucherName":"  Edit","PackageID":res['PackageID'],
                                   "ActivityID":res['ActivityID'],"Amount":"13",
                                   "StartTime": time_select.MonthStart(),
                                   "EndTime": time_select.MonthEnd()},
                             api_url=BackAPI.voucher_voucherEdit.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_09_GPG_VoucherDel(self):
        """測試總代理刪除兌換券是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',api_url=BackAPI.voucher_voucherGet.value, payload={'Skip': 0, 'Show': 50,
                                                    'Field': 'VoucherName',
                                                    'OrderType': 'desc',
                                                    'VoucherName': "  Edit",
                                                    'IsFuzzySearch': True})['Data'].pop()
        res = api.apiGetData(method='post',data={"VoucherID":res['VoucherID']},
                             api_url=BackAPI.voucher_voucherDel.value)
        self.assertEqual('Success', res['Status']['Message'])