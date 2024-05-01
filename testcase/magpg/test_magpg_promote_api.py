import unittest
from testcase.gpg2_chromeset import ma_api, BackAPI
import logging
import inspect

class Test_Promote_api(unittest.TestCase):
    """推廣連結管理"""
    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_GPG_PromoteReport_API(self):
        """測試總代理的推廣連結管理是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'StatusID': 2,
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_promoteReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_PromoteReport_API(self):
        """測試A代理的推廣連結管理是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'StatusID': 2,
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc' },
                             api_url=BackAPI.dataReport_promoteReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_PromoteReport_API(self):
        """測試B代理的推廣連結管理是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'StatusID': 2,
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc' },
                             api_url=BackAPI.dataReport_promoteReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_PromoteReport_API(self):
        """測試C代理的推廣連結管理是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'StatusID': 2,
                                      'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc', },
                             api_url=BackAPI.dataReport_promoteReport.value)
        self.assertEqual('Success', res['Status']['Message'])

    def GPG_NewCode_API(self, MemberID):
        """測試總代理的推廣連結新增頁面是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             api_url=BackAPI.promote_newCode.value)
        self.assertEqual('Success', res['Status']['Message'])
        self.GPG_Add_API(MemberID, res['Data'])

    def A_Agent_NewCode_API(self, MemberID):
        """測試A代理的推廣連結新增頁面是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.promote_newCode.value)
        self.assertEqual('Success', res['Status']['Message'])
        self.A_Agent_Add_API(MemberID, res['Data'])

    def B_Agent_NewCode_API(self, MemberID):
        """測試B代理的推廣連結新增頁面是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.promote_newCode.value)
        self.assertEqual('Success', res['Status']['Message'])
        self.B_Agent_Add_API(MemberID, res['Data'])

    def C_Agent_NewCode_API(self, MemberID):
        """測試C代理的推廣連結新增頁面是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.promote_newCode.value)
        self.assertEqual('Success', res['Status']['Message'])
        self.C_Agent_Add_API(MemberID, res['Data'])

    def GPG_Add_API(self, MemberID, promoteCode):
        """測試總代理的推廣連結是否新增正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={'MemberID': MemberID,
                                   'Note': "",
                                   'PromoteCode': promoteCode},
                             api_url=BackAPI.promote_add.value)
        self.assertEqual('Success', res['Status']['Message'])

    def A_Agent_Add_API(self, MemberID, promoteCode):
        """測試A代理的推廣連結是否新增正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'MemberID': MemberID,
                                   'Note': "",
                                   'PromoteCode': promoteCode},
                             api_url=BackAPI.promote_add.value)
        self.assertEqual('Success', res['Status']['Message'])

    def B_Agent_Add_API(self, MemberID, promoteCode):
        """測試B代理的推廣連結是否新增正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'MemberID': MemberID,
                                   'Note': "",
                                   'PromoteCode': promoteCode},
                             api_url=BackAPI.promote_add.value)
        self.assertEqual('Success', res['Status']['Message'])

    def C_Agent_Add_API(self, MemberID, promoteCode):
        """測試C代理的推廣連結是否新增正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'MemberID': MemberID,
                                   'Note': "",
                                   'PromoteCode': promoteCode},
                             api_url=BackAPI.promote_add.value)
        self.assertEqual('Success', res['Status']['Message'])

    def GPG_Delete_API(self, PromoteID):
        """測試總代理的推廣連結刪除是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={'PromoteID': PromoteID},
                             api_url=BackAPI.promote_delete.value)
        self.assertEqual('Success', res['Status']['Message'])

    def A_Agent_Delete_API(self, PromoteID):
        """測試A代理的推廣連結刪除是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'PromoteID': PromoteID},
                             api_url=BackAPI.promote_delete.value)
        self.assertEqual('Success', res['Status']['Message'])

    def B_Agent_Delete_API(self, PromoteID):
        """測試B代理的推廣連結刪除是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'PromoteID': PromoteID},
                             api_url=BackAPI.promote_delete.value)
        self.assertEqual('Success', res['Status']['Message'])

    def C_Agent_Delete_API(self, PromoteID):
        """測試C代理的推廣連結刪除是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={'PromoteID': PromoteID},
                             api_url=BackAPI.promote_delete.value)
        self.assertEqual('Success', res['Status']['Message'])
