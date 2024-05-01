import unittest
from testcase.gpg2_chromeset import env, ma_api,BackAPI
import logging
import inspect

class Test_AdvertisersList_api(unittest.TestCase):
    """廣告商加盟列表"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GPG_AdvertisersList_API(self):
        """測試總代理的廣告商加盟列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0, 'Show': 50,
                                      'Field': 'CreateTime', 'OrderType': 'desc'},
                             api_url=BackAPI.member_advertisersList.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_AdvertisersList_API(self):
        """測試A代理的廣告商加盟列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0, 'Show': 50,
                                      'Field': 'CreateTime', 'OrderType': 'desc'},
                             api_url=BackAPI.member_advertisersList.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_AdvertisersList_API(self):
        """測試B代理的廣告商加盟列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0, 'Show': 50,
                                      'Field': 'CreateTime', 'OrderType': 'desc'},
                             api_url=BackAPI.member_advertisersList.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_AdvertisersList_API(self):
        """測試C代理的廣告商加盟列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0, 'Show': 50,
                                      'Field': 'CreateTime', 'OrderType': 'desc'},
                             api_url=BackAPI.member_advertisersList.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_GPG_AdvertisersInfo_API(self):
        """測試總代理的廣告商加盟商資訊是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             api_url=BackAPI.member_advertisersInfo.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_AdvertisersInfo_API(self):
        """測試A代理的廣告商加盟商資訊是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.member_advertisersInfo.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_AdvertisersInfo_API(self):
        """測試B代理的廣告商加盟商資訊是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.member_advertisersInfo.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_AdvertisersInfo_API(self):
        """測試C代理的廣告商加盟商資訊是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.member_advertisersInfo.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_GPG_AdvertisersPath_API(self):
        """測試總代理的廣告商加盟商路徑是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             api_url=BackAPI.member_advertisersPath.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_AdvertisersPath_API(self):
        """測試A代理的廣告商加盟商路徑是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.member_advertisersPath.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_AdvertisersPath_API(self):
        """測試B代理的廣告商加盟商路徑是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.member_advertisersPath.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_AdvertisersPath_API(self):
        """測試C代理的廣告商加盟商路徑是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.member_advertisersPath.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_GPG_InviteFranchisee_API(self):
        """測試總代理的產生加盟註冊連結是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={"Greeting": "歡迎成為GPG的廣告加盟商！GPG廣告加盟商後台網址: https://manage-gpg.ceis.tw"},
                             api_url=BackAPI.member_inviteFranchisee.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_InviteFranchisee_API(self):
        """測試A代理的的產生加盟註冊連結是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={"Greeting": "歡迎成為GPG的廣告加盟商！GPG廣告加盟商後台網址: https://manage-gpg.ceis.tw"},
                             api_url=BackAPI.member_inviteFranchisee.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_Agent_InviteFranchisee_API(self):
        """測試B代理的的產生加盟註冊連結是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={"Greeting": "歡迎成為GPG的廣告加盟商！GPG廣告加盟商後台網址: https://manage-gpg.ceis.tw"},
                             api_url=BackAPI.member_inviteFranchisee.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_Agent_InviteFranchisee_API(self):
        """測試C代理的的產生加盟註冊連結是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={"Greeting": "歡迎成為GPG的廣告加盟商！GPG廣告加盟商後台網址: https://manage-gpg.ceis.tw"},
                             api_url=BackAPI.member_inviteFranchisee.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_GPG_GameAccounts_API(self):
        """測試總代理的查看會員遊戲帳號是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             data={"MemberID": 1},  # 寫死直接查詢ＧＰＧ的帳號
                             api_url=BackAPI.infos_gameAccounts.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_GameAccounts_API(self):
        """測試A代理的查看會員遊戲帳號是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             data={"MemberID": 1},  # 寫死直接查詢ＧＰＧ的帳號
                             api_url=BackAPI.infos_gameAccounts.value)
        self.assertEqual('', res)

    def test_B_Agent_GameAccounts_API(self):
        """測試B代理的查看會員遊戲帳號是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             data={"MemberID": 1},  # 寫死直接查詢ＧＰＧ的帳號
                             api_url=BackAPI.infos_gameAccounts.value)
        self.assertEqual('', res)

    def test_C_Agent_GameAccounts_API(self):
        """測試C代理的查看會員遊戲帳號是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             data={"MemberID": 1},  # 寫死直接查詢ＧＰＧ的帳號
                             api_url=BackAPI.infos_gameAccounts.value)
        self.assertEqual('', res)
