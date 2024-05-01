import random
import time
import unittest
from testcase.gpg2_chromeset import env, ma_api, BackAPI
from enum import Enum
import logging
import inspect


class Test_GameList(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_GPG_GameList_API(self):
        """測試總代理的遊戲列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'Skip': 0,
                                      'Show': 50,
                                      'Field': 'FrontSort',
                                      'OrderType': 'asc',
                                      'GameProviderID': 1},
                             api_url=BackAPI.game_gameList.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_GameList_API(self):
        """測試A代理的遊戲列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'Skip': 0,
                                      'Show': 50,
                                      'Field': 'FrontSort',
                                      'OrderType': 'asc',
                                      'GameProviderID': 1},
                             api_url=BackAPI.game_gameList.value)
        self.assertEqual('', res)

    def test_B_Agent_GameList_API(self):
        """測試B代理的遊戲列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'Skip': 0,
                                      'Show': 50,
                                      'Field': 'FrontSort',
                                      'OrderType': 'asc',
                                      'GameProviderID': 1},
                             api_url=BackAPI.game_gameList.value)
        self.assertEqual('', res)

    def test_C_Agent_GameList_API(self):
        """測試C代理的遊戲列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'Skip': 0,
                                      'Show': 50,
                                      'Field': 'FrontSort',
                                      'OrderType': 'asc',
                                      'GameProviderID': 1},
                             api_url=BackAPI.game_gameList.value)
        self.assertEqual('', res)

    def test_GPG_Status_API(self):
        """測試總代理的遊戲商狀態是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             api_url=BackAPI.game_provider_vaSlot_status.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_Status_API(self):
        """測試A代理的遊戲商狀態是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.game_provider_ifun_status.value)
        self.assertEqual('', res)

    def test_B_Agent_Status_API(self):
        """測試B代理的遊戲商狀態是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.game_provider_vaBattle_status.value)
        self.assertEqual('', res)

    def test_C_Agent_Status_API(self):
        """測試C代理的遊戲商狀態是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             api_url=BackAPI.game_provider_vaSlot_status.value)
        self.assertEqual('', res)

    def test_GPG_EditGame_API(self):
        """測試總代理的編輯功能是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'FrontSort': 3,
                                 'GameID': 3,
                                 'GameProviderGameID': "323",
                                 'GameProviderID': 1,
                                 'GameTypeID': 1,
                                 'GoldState': True,
                                 'SilverState': True,
                                 'TraditionalChinese': "貔貅財寶庫EX PLUS"
                             },
                             api_url=BackAPI.game_editGame.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_EditGame_API(self):
        """測試A代理的編輯功能是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'FrontSort': 3,
                                 'GameID': 3,
                                 'GameProviderGameID': "323",
                                 'GameProviderID': 1,
                                 'GameTypeID': 1,
                                 'GoldState': True,
                                 'SilverState': True,
                                 'TraditionalChinese': "貔貅財寶庫EX PLUS"
                             },
                             api_url=BackAPI.game_editGame.value)
        self.assertEqual('', res)

    def test_B_Agent_EditGame_API(self):
        """測試B代理的編輯功能是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'FrontSort': 3,
                                 'GameID': 3,
                                 'GameProviderGameID': "323",
                                 'GameProviderID': 1,
                                 'GameTypeID': 1,
                                 'GoldState': True,
                                 'SilverState': True,
                                 'TraditionalChinese': "貔貅財寶庫EX PLUS"
                             },
                             api_url=BackAPI.game_editGame.value)
        self.assertEqual('', res)

    def test_C_Agent_EditGame_API(self):
        """測試C代理的編輯功能是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'FrontSort': 3,
                                 'GameID': 3,
                                 'GameProviderGameID': "323",
                                 'GameProviderID': 1,
                                 'GameTypeID': 1,
                                 'GoldState': True,
                                 'SilverState': True,
                                 'TraditionalChinese': "貔貅財寶庫EX PLUS"
                             },
                             api_url=BackAPI.game_editGame.value)
        self.assertEqual('', res)

    def test_GPG_GameStatus_Close_API(self):
        """測試總代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'GameID': 3,
                                 'MaintenanceStatus': 1,
                             },
                             api_url=BackAPI.game_um_status.value)
        self.assertEqual('Success', res['Status']['Message'])
        self.test_GPG_GameStatus_Open_API()

    def test_A_Agent_GameStatus_Close_API(self):
        """測試A代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameID': 3,
                                 'MaintenanceStatus': 1,
                             },
                             api_url=BackAPI.game_um_status.value)
        self.assertEqual('', res)

    def test_B_Agent_GameStatus_Close_API(self):
        """測試B代理的維護設定是否正常成功"""
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameID': 3,
                                 'MaintenanceStatus': 1,
                             },
                             api_url=BackAPI.game_um_status.value)
        self.assertEqual('', res)

    def test_C_Agent_GameStatus_Close_API(self):
        """測試C代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameID': 3,
                                 'MaintenanceStatus': 1,
                             },
                             api_url=BackAPI.game_um_status.value)
        self.assertEqual('', res)

    def test_GPG_GameStatus_Open_API(self):
        """測試總代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'GameID': 3,
                                 'MaintenanceStatus': 0,
                             },
                             api_url=BackAPI.game_um_status.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_GameStatus_Open_API(self):
        """測試A代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameID': 3,
                                 'MaintenanceStatus': 0,
                             },
                             api_url=BackAPI.game_um_status.value)
        self.assertEqual('', res)

    def test_B_Agent_GameStatus_Open_API(self):
        """測試B代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameID': 3,
                                 'MaintenanceStatus': 0,
                             },
                             api_url=BackAPI.game_um_status.value)
        self.assertEqual('', res)

    def test_C_Agent_GameStatus_Open_API(self):
        """測試C代理的維護設定是否正常成功"""
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameID': 3,
                                 'MaintenanceStatus': 0,
                             },
                             api_url=BackAPI.game_um_status.value)
        self.assertEqual('', res)

    def test_GPG_AllGameStatus_Close_API(self):
        """測試總代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'GameProviderID': 1,
                                 'MaintenanceStatus': 1,
                             },
                             api_url=BackAPI.game_Provider_Um_Status.value)
        self.assertEqual('Success', res['Status']['Message'])
        time.sleep(2)
        self.test_GPG_AllGameStatus_Open_API()  # 請使用後記得打開

    def test_A_Agent_AllGameStatus_Close_API(self):
        """測試A代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameProviderID': 1,
                                 'MaintenanceStatus': 1,
                             },
                             api_url=BackAPI.game_Provider_Um_Status.value)
        self.assertEqual('', res)

    def test_B_Agent_AllGameStatus_Close_API(self):
        """測試B代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameProviderID': 1,
                                 'MaintenanceStatus': 1,
                             },
                             api_url=BackAPI.game_Provider_Um_Status.value)
        self.assertEqual('', res)

    def test_C_Agent_AllGameStatus_Close_API(self):
        """測試C代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameProviderID': 1,
                                 'MaintenanceStatus': 1,
                             },
                             api_url=BackAPI.game_Provider_Um_Status.value)
        self.assertEqual('', res)

    def test_GPG_AllGameStatus_Open_API(self):
        """測試總代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post',
                             data={
                                 'GameProviderID': 1,
                                 'MaintenanceStatus': 0,
                             },
                             api_url=BackAPI.game_Provider_Um_Status.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_Agent_AllGameStatus_Open_API(self):
        """測試A代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameProviderID': 1,
                                 'MaintenanceStatus': 0,
                             },
                             api_url=BackAPI.game_Provider_Um_Status.value)
        self.assertEqual('', res)

    def test_B_Agent_AllGameStatus_Open_API(self):
        """測試B代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameProviderID': 1,
                                 'MaintenanceStatus': 0,
                             },
                             api_url=BackAPI.game_Provider_Um_Status.value)
        self.assertEqual('', res)

    def test_C_Agent_AllGameStatus_Open_API(self):
        """測試C代理的維護設定是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',
                             data={
                                 'GameProviderID': 1,
                                 'MaintenanceStatus': 0,
                             },
                             api_url=BackAPI.game_Provider_Um_Status.value)
        self.assertEqual('', res)
