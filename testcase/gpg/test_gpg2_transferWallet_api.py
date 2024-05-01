import unittest
from testcase.gpg2_chromeset import gpg_api, progressNotify,TransferDict,FontAPI,env
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
import inspect
import logging

"""
轉帳錢包-單元測試
規格文件整理
幣別：金幣＆銀幣 default:金幣
轉出：default:主錢包
轉入：default:  
轉帳額度：超過主錢包額度必須直接填入，手機版鎖定數字鍵盤，限定整數
確認轉帳：點擊後，若額度>轉出方錢包，則跳轉帳錯誤（ＡＰＩ測試）
  單筆轉帳上限為一億元
  無轉帳上限
轉帳紀錄
"""


# class Test_transferWallet_api(unittest.TestCase):
#     def setUp(self):
#         # self.test_driver = driver_eng()
#         warnings.simplefilter('ignore', ResourceWarning)
#
#     def tearDown(self):
#         pass
#         # time.sleep(2)
#
#     @classmethod
#     def setUpClass(cls):
#         progressNotify(message='轉帳錢包ＡＰＩ測試開始')
#
#     @classmethod
#     def tearDownClass(cls):
#         progressNotify(message='轉帳錢包ＡＰＩ測試完成')
#
#     def memberInfo(self, **kwargs):
#         identity = kwargs.get('identity')
#         if identity == None:
#             identity = 'member'
#         self.api = gpg_api(token=f'{identity}Token')
#         res = self.api.apiGetData(method='get', payload={'CheckProviderMember': True, 'UpdateFromProvider': True},
#                                   api_url=FontAPI.wallet_search.value).get('Data')
#         gold = list(filter(lambda x: x.get('WalletPointTypeID') == TransferDict.gpg_gold.value, res)).pop().get(
#             'Balance')
#         silver = list(filter(lambda x: x.get('WalletPointTypeID') == TransferDict.gpg_silver.value, res)).pop().get(
#             'Balance')
#         return gold, silver
#
#     def test_transferWallet_transferApitest_gold_guest_M2Vs(self):
#         """測試訪客模式下測試API轉帳到  是否可以成功(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_member_M2Vs(self):
#         """測試會員模式下測試API轉帳到  是否可以成功(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_agentMember_M2Vs(self):
#         """測試代理會員模式下測試API轉帳到  是否可以成功(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_guest_M2Vs(self):
#         """測試訪客模式下測試API轉帳到  是否可以成功(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_silver.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _silver.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_member_M2Vs(self):
#         """測試會員模式下測試API轉帳到  是否可以成功(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_agentMember_M2Vs(self):
#         """測試代理會員模式下測試API轉帳到  是否可以成功(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_enoughNo_guest_M2Vs(self):
#         """測試訪客模式下測試API轉帳到  是否(金幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': gold + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_gold_enoughNo_member_M2Vs(self):
#         """測試會員模式下測試API轉帳到  是否(金幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo()
#         self.api.apiGetData(method='post',
#                             data={'CheckProviderMember': True, 'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                   'Point': gold - 1000, 'ToWalletPointTypeID': TransferDict.  _gold.value},
#                             api_url=FontAPI.wallet_transfer.value)
#         gold, silver = self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': gold + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.api.apiGetData(method='post', data={"PointTypeID": 1}, api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_gold_enoughNo_agentMember_M2Vs(self):
#         """測試代理會員模式下測試API轉帳到  是否(金幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo(identity='agent')
#         self.api.apiGetData(method='post',
#                             data={'CheckProviderMember': True, 'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                   'Point': gold - 1000, 'ToWalletPointTypeID': TransferDict.  _gold.value},
#                             api_url=FontAPI.wallet_transfer.value)
#         gold, silver = self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': gold + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.api.apiGetData(method='post', data={"PointTypeID": 1}, api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_silver_enoughNo_guest_M2Vs(self):
#         """測試訪客模式下測試API是否(銀幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': silver + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_silver_enoughNo_member_M2Vs(self):
#         """測試會員模式下測試API是否(銀幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo()
#         self.api.apiGetData(method='post',
#                             data={'CheckProviderMember': True, 'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                   'Point': silver - 1000, 'ToWalletPointTypeID': TransferDict.  _silver.value},
#                             api_url=FontAPI.wallet_transfer.value)
#         gold, silver = self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': silver + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.api.apiGetData(method='post', data={"PointTypeID": 2}, api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_silver_enoughNo_agentMember_M2Vs(self):
#         """測試代理會員模式下測試API轉帳到  是否(銀幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo(identity='agent')
#         self.api.apiGetData(method='post',
#                             data={'CheckProviderMember': True, 'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                   'Point': silver - 1000, 'ToWalletPointTypeID': TransferDict.  _silver.value},
#                             api_url=FontAPI.wallet_transfer.value)
#         gold, silver = self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': silver + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.api.apiGetData(method='post', data={"PointTypeID": 2}, api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_gold_guest_M2Vb(self):
#         """測試訪客模式下測試API轉帳到VA對戰是否可以成功(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_member_M2Vb(self):
#         """測試會員模式下測試API轉帳到VA對戰是否可以成功(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_agentMember_M2Vb(self):
#         """測試代理會員模式下測試API轉帳到VA對戰是否可以成功(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_guest_M2Vb(self):
#         """測試訪客模式下測試API轉帳到VA對戰是否可以成功(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_silver.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _silver.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_member_M2Vb(self):
#         """測試會員模式下測試API轉帳到VA對戰是否可以成功(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_agentMember_M2Vb(self):
#         """測試代理會員模式下測試API轉帳到VA對戰是否可以成功(銀幣)"""
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_enoughNo_guest_M2Vb(self):
#         """測試訪客模式下測試API轉帳到VA對戰是否(金幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': gold + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_gold_enoughNo_member_M2Vb(self):
#         """測試會員模式下測試API轉帳到VA對戰是否(金幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': gold + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_gold_enoughNo_agentMember_M2Vb(self):
#         """測試代理會員模式下測試API轉帳到VA對戰是否(金幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': gold + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_silver_enoughNo_guest_M2Vb(self):
#         """測試訪客模式下測試API轉帳到VA對戰是否(銀幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': silver + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_silver_enoughNo_member_M2Vb(self):
#         """測試會員模式下測試API轉帳到VA對戰是否(銀幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': silver + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_transferApitest_silver_enoughNo_agentMember_M2Vb(self):
#         """測試代理會員模式下測試API是否(銀幣)餘額不足"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         gold, silver = self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': silver + 1000,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 錢包餘額不足!')
#
#     def test_transferWallet_ErrorTransfer_syntaxError_guest(self):
#         """測試訪客模式下轉帳金額非數字"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 'syntaxError',
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          'The JSON value could not be converted to System.Decimal. Path: $.Point | LineNumber: 0 | BytePositionInLine: 80.')
#
#     def test_transferWallet_ErrorTransfer_syntaxError_member(self):
#         """測試會員模式下轉帳金額非數字"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 'syntaxError',
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          'The JSON value could not be converted to System.Decimal. Path: $.Point | LineNumber: 0 | BytePositionInLine: 80.')
#
#     def test_transferWallet_ErrorTransfer_syntaxError_agentMember(self):
#         """測試代理會員模式下轉帳金額非數字"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 'syntaxError',
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          'The JSON value could not be converted to System.Decimal. Path: $.Point | LineNumber: 0 | BytePositionInLine: 80.')
#
#     def test_transferWallet_ErrorTransfer_guest(self):
#         """測試訪客模式下轉帳金幣帳戶轉銀幣帳戶"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 不同幣別不可轉換!')
#
#     def test_transferWallet_ErrorTransfer_member(self):
#         """測試會員模式下轉帳金幣帳戶轉銀幣帳戶"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 不同幣別不可轉換!')
#
#     def test_transferWallet_ErrorTransfer_agentMember(self):
#         """測試代理會員模式下轉帳金幣帳戶轉銀幣帳戶"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 不同幣別不可轉換!')
#
#     @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
#     def test_transferWallet_gold_  Max(self):
#         """測試  轉帳上限1億元(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': 10000000012,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! VA 電子轉帳上限1億點')
#
#     @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
#     def test_transferWallet_silver_  Max(self):
#         """測試  轉帳上限1億元(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': 10000000012,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! VA 電子轉帳上限1億點')
#
#     def test_transferWallet_gold_transferNegativeNumber_M2Vb_guest(self):
#         """測試訪客模式下  轉帳輸入負數(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error! InPoker.ChangePoints (Gold) Error. Message:補扣點失敗!原因：點數不能為負的。")
#
#     def test_transferWallet_silver_transferNegativeNumber_M2Vb_guest(self):
#         """測試訪客模式下  轉帳輸入負數(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error! InPoker.ChangePoints (Silver) Error. Message:補扣點失敗!原因：點數不能為負的。")
#
#     def test_transferWallet_gold_transferNegativeNumber_M2Vb_member(self):
#         """測試會員模式下  轉帳輸入負數(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error! InPoker.ChangePoints (Gold) Error. Message:補扣點失敗!原因：點數不能為負的。")
#
#     def test_transferWallet_silver_transferNegativeNumber_M2Vb_member(self):  # question
#         """測試會員模式下  轉帳輸入負數(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error! InPoker.ChangePoints (Silver) Error. Message:補扣點失敗!原因：點數不能為負的。")
#
#     def test_transferWallet_gold_transferNegativeNumber_M2Vb_agentMember(self):
#         """測試代理會員模式下  轉帳輸入負數(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error! InPoker.ChangePoints (Gold) Error. Message:補扣點失敗!原因：點數不能為負的。")
#
#     def test_transferWallet_silver_transferNegativeNumber_M2Vb_agentMember(self):
#         """測試代理會員模式下  轉帳輸入負數(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error! InPoker.ChangePoints (Silver) Error. Message:補扣點失敗!原因：點數不能為負的。")
#
#     def test_transferWallet_gold_transferNegativeNumber_M2Vs_guest(self):
#         """測試訪客模式下  轉帳輸入負數(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error!   .TransferWallet (Gold) Error. VaApi.DepositCurrency returns null.")
#
#     def test_transferWallet_silver_transferNegativeNumber_M2Vs_guest(self):
#         """測試訪客模式下  轉帳輸入負數(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error!   .TransferWallet (Silver) Error. VaApi.DepositCurrency returns null.")
#
#     def test_transferWallet_gold_transferNegativeNumber_M2Vs_member(self):
#         """測試會員模式下  轉帳輸入負數(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error!   .TransferWallet (Gold) Error. VaApi.DepositCurrency returns null.")
#
#     def test_transferWallet_silver_transferNegativeNumber_M2Vs_member(self):
#         """測試會員模式下  轉帳輸入負數(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error!   .TransferWallet (Silver) Error. VaApi.DepositCurrency returns null.")
#
#     def test_transferWallet_gold_transferNegativeNumber_M2Vs_agentMember(self):
#         """測試代理會員模式下  轉帳輸入負數(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_gold.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _gold.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error!   .TransferWallet (Gold) Error. VaApi.DepositCurrency returns null.")
#
#     def test_transferWallet_silver_transferNegativeNumber_M2Vs_agentMember(self):
#         """測試代理會員模式下  轉帳輸入負數(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={'CheckProviderMember': True,
#                                                        'FromWalletPointTypeID': TransferDict.gpg_silver.value,
#                                                        'Point': -1,
#                                                        'ToWalletPointTypeID': TransferDict.  _silver.value},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'],
#                          "Send GameConnect-'TransferWallet' api error!   .TransferWallet (Silver) Error. VaApi.DepositCurrency returns null.")
#
#     def test_transferWallet_gold_TransferBack_guest(self):
#         """測試訪客模式下一鍵轉回(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 1},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "Success")
#
#     def test_transferWallet_silver_TransferBack_guest(self):
#         """測試訪客模式下一鍵轉回(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 2},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "Success")
#
#     def test_transferWallet_gold_TransferBack_member(self):
#         """測試會員模式下一鍵轉回(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 1},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "Success")
#
#     def test_transferWallet_silver_TransferBack_member(self):
#         """測試會員模式下一鍵轉回(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 2},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "Success")
#
#     def test_transferWallet_gold_TransferBack_agentMember(self):
#         """測試代理會員模式下一鍵轉回(金幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 1},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "Success")
#
#     def test_transferWallet_silver_TransferBack_agentMember(self):
#         """測試代理會員模式下一鍵轉回(銀幣)"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 2},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "Success")
#
#     def test_transferWallet_ErrorCoinType_TransferBack_guest(self):
#         """測試訪客模式下輸入不存在的幣種一鍵取回"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 3},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "無效的幣別")
#
#     def test_transferWallet_ErrorCoinType_TransferBack_member(self):
#         """測試會員模式下輸入不存在的幣種一鍵取回"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 3},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "無效的幣別")
#
#     def test_transferWallet_ErrorCoinType_TransferBack_agentMember(self):
#         """測試代理會員模式下輸入不存在的幣種一鍵取回"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"PointTypeID": 3},
#                                   api_url=FontAPI.wallet_transferBack.value)
#         self.assertEqual(res['Status']['Message'], "無效的幣別")
#
#     def test_transferWallet_transferApitest_gold_guest_M2  (self):
#         """測試訪客模式下輸入主錢包轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_member_M2  (self):
#         """測試會員模式下輸入主錢包轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_agentMember_M2  (self):
#         """測試代理會員模式下輸入主錢包轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_Error_guest_M2  (self):
#         """測試訪客模式下錯誤錢包轉換  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_silver.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 不同幣別不可轉換!')
#
#     def test_transferWallet_transferApitest_Error_member_M2  (self):
#         """測試會員模式下錯誤錢包轉換  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_silver.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 不同幣別不可轉換!')
#
#     def test_transferWallet_transferApitest_Error_agentMember_M2  (self):
#         """測試代理會員模式下錯誤錢包轉換"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_silver.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], '錢包轉換失敗! 不同幣別不可轉換!')
#
#     def test_transferWallet_transferApitest_gold_guest_Vs2  (self):
#         """測試訪客模式下Va電子轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_member_Vs2  (self):
#         """測試會員模式下Va電子轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_agentMember_Vs2  (self):
#         """測試代理會員模式下Va電子轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_guest_Vb2  (self):
#         """測試訪客模式下Va對戰轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_member_Vb2  (self):
#         """測試會員模式下Va對戰轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_agentMember_Vb2  (self):
#         """測試代理會員模式下Va對戰轉  """
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.  _gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_guest_M2MK(self):
#         """測試訪客模式下金幣主錢包轉MK"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.MK_gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_guest_M2MK(self):
#         """測試訪客模式下銀幣主錢包轉MK"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='guest')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_silver.value,
#                                                        "ToWalletPointTypeID": TransferDict.MK_silver.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_member_M2MK(self):
#         """測試會員模式下金幣主錢包轉MK"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.MK_gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_member_M2MK(self):
#         """測試會員模式下銀幣主錢包轉MK"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo()
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_silver.value,
#                                                        "ToWalletPointTypeID": TransferDict.MK_silver.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_gold_agentMember_M2MK(self):
#         """測試代理模式下金幣主錢包轉MK"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_gold.value,
#                                                        "ToWalletPointTypeID": TransferDict.MK_gold.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')
#
#     def test_transferWallet_transferApitest_silver_agentMember_M2MK(self):
#         """測試代理模式下銀幣主錢包轉MK"""
#         logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
#         self.memberInfo(identity='agent')
#         res = self.api.apiGetData(method='post', data={"FromWalletPointTypeID": TransferDict.gpg_silver.value,
#                                                        "ToWalletPointTypeID": TransferDict.MK_silver.value,
#                                                        "Point": 1, "CheckProviderMember": True},
#                                   api_url=FontAPI.wallet_transfer.value)
#         self.assertEqual(res['Status']['Message'], 'Success')

# if __name__ == '__main__':
#     unittest.main(testRunner=HTMLTestRunner())
