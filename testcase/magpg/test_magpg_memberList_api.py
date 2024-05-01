import unittest
from testcase.gpg2_chromeset import env, ma_api, BackAPI
import inspect
import logging

class Test_MemberList_api(unittest.TestCase):
    """測試會員列表"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_MemberList_API(self):
        """測試總代理的會員列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'IsGuest': False, },
                             api_url=BackAPI.member_memberList.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_MemberList_API(self):
        """測試A代理的會員列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'IsGuest': False, },
                             api_url=BackAPI.member_memberList.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_MemberList_API(self):
        """測試B代理的會員列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'IsGuest': False, },
                             api_url=BackAPI.member_memberList.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_MemberList_API(self):
        """測試C代理的會員列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'IsFuzzySearch': True,
                                      'Skip': 0,
                                      'Show': 50,
                                      'Field': 'CreateTime',
                                      'OrderType': 'desc',
                                      'IsGuest': False, },
                             api_url=BackAPI.member_memberList.value)
        self.assertEqual('Success', res['Status']['Message'])


    ############################遊戲帳號查看#######################################
    def test_GPG_GameAccounts(self):
        """測試總代理的遊戲帳號否正常成功"""
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'MemberID':1},
                             api_url=BackAPI.infos_gameAccounts.value)
        self.assertEqual('Success', res['Status']['Message'])


    def test_A_Agent_GameAccounts(self):
        """測試總代理的遊戲帳號否正常成功"""
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'MemberID':1},
                             api_url=BackAPI.infos_gameAccounts.value)
        self.assertEqual('', res)


    def test_B_Agent_GameAccounts(self):
        """測試總代理的遊戲帳號否正常成功"""
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'MemberID':1},
                             api_url=BackAPI.infos_gameAccounts.value)
        self.assertEqual('', res)


    def test_C_Agent_GameAccounts(self):
        """測試總代理的遊戲帳號否正常成功"""
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'MemberID':1},
                             api_url=BackAPI.infos_gameAccounts.value)
        self.assertEqual('', res)
