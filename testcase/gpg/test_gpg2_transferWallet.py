# import unittest
# from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify
# import warnings
# from testcase.HTMLTestReportCN import HTMLTestRunner
# from selenium.webdriver.common.by import By
# """
# 轉帳錢包-單元測試
# 規格文件整理
# 幣別：金幣＆銀幣 default:金幣
# 轉出：default:主錢包
# 轉入：default:VASlot
# 轉帳額度：超過主錢包額度必須直接填入，手機版鎖定數字鍵盤，限定整數
# 確認轉帳：點擊後，若額度>轉出方錢包，則跳轉帳錯誤（ＡＰＩ測試）
# VASlot單筆轉帳上限為一億元
# VABattle無轉帳上限
# 轉帳紀錄
#
#  """
#   2023/1/1 預計可能重構
#  """
# class Test_transferWallet(unittest.TestCase):
#     def setUp(self):
#         clean_resource()  # 開始砍進程
#         self.test_driver = driver_eng()
#         warnings.simplefilter('ignore', ResourceWarning)
#
#     def tearDown(self):
#         self.test_driver.exit()
#
#     @classmethod
#     def setUpClass(cls):
#         progressNotify(message='轉帳錢包測試開始')
#
#     @classmethod
#     def tearDownClass(cls):
#         progressNotify(message='轉帳錢包測試完成')
#
#     def test_transferWallet_guest(self):
#         """測試訪客模式下是否轉帳成功"""
#         self.test_driver.loginV2(identity='guest')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket()
#
#     def test_transferWallet_member(self):
#         """測試會員模式下是否轉帳成功"""
#         self.test_driver.loginV2()
#         self.test_driver.transfer()
#         self.test_driver.transferPacket()
#
#     def test_transferWallet_agentMember(self):
#         """測試代理會員模式下是否轉帳成功"""
#         self.test_driver.loginV2(identity='agent')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket()
#
#     def test_transferWallet_M2Vb_guest(self):
#         """測試訪客模式下是否主錢包轉  """
#         self.test_driver.loginV2(identity='guest')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
#     def test_transferWallet_M2Vb_member(self):
#         """測試會員模式下是否主錢包轉  """
#         self.test_driver.loginV2()
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
#     def test_transferWallet_M2Vb_agentMember(self):
#         """測試代理會員模式下是否主錢包轉  """
#         self.test_driver.loginV2(identity='agent')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
#     def test_transferWallet_Vb2Vs_guest(self):
#         """測試訪客模式下是否   轉  """
#         self.test_driver.loginV2(identity='guest')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='  ', to='  ')
#
#     def test_transferWallet_Vb2Vs_member(self):
#         """測試會員模式下是否  戰轉  """
#         self.test_driver.loginV2()
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='  ', to='  ')
#
#     def test_transferWallet_Vb2Vs_agentMember(self):
#         """測試代理會員模式下是否  戰轉  """
#         self.test_driver.loginV2(identity='agent')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='  ', to='  ')
#
#     def test_transferWallet_Vb2M_guest(self):
#         """測試訪客模式下是否  轉主錢包"""
#         self.test_driver.loginV2(identity='guest')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='  ', to='主錢包')
#
#     def test_transferWallet_Vb2M_member(self):
#         """測試會員模式下是否  轉主錢包"""
#         self.test_driver.loginV2()
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='  ', to='主錢包')
#
#     def test_transferWallet_Vb2M_agentMember(self):
#         """測試代理會員模式下是否  轉主錢包"""
#         self.test_driver.loginV2(identity='agent')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='  ', to='主錢包')
#
#     def test_transferWallet_intoGame_guest(self):# 後續 code review
#         """測試訪客模式下當餘額不足時進入遊戲是否跳出錢包視窗"""
#         self.test_driver.loginV2(identity='guest')
#         i, game_list = enumerate(self.test_driver.gameList(type='battle'), start=1).__next__()
#         self.test_driver.gameDetail(i)
#         self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game-pop__wrap")]'))
#
#     def test_transferWallet_intoGame_member(self):# 後續 code review
#         """測試會員模式下當餘額不足時進入遊戲是否跳出錢包視窗"""
#         self.test_driver.loginV2()
#         i, game_list = enumerate(self.test_driver.gameList(type='battle'), start=1).__next__()
#         self.test_driver.gameDetail(i).click()
#         self.assertIsNotNone(
#             self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"wallet__container")]'))
#
#     def test_transferWallet_intoGame_agentMember(self): # 後續 code review
#         """測試代理會員模式下當餘額不足時進入遊戲是否跳出錢包視窗"""
#         self.test_driver.loginV2(identity='agent')
#         i, game_list = enumerate(self.test_driver.gameList(type='battle'), start=1).__next__()
#         self.test_driver.gameDetail(i).click()
#         self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"wallet__container")]'))
#
#     def test_transferWallet_M2  _guest(self):
#         """測試訪客模式下是否主錢包轉  """
#         self.test_driver.loginV2(identity='guest')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
#     def test_transferWallet_M2  _member(self):
#         """測試會員模式下是否主錢包轉  """
#         self.test_driver.loginV2()
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
#     def test_transferWallet_M2  _agentMember(self):
#         """測試代理會員模式下是否主錢包轉  """
#         self.test_driver.loginV2(identity='agent')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
#     def test_transferWallet_M2  _guest(self):
#         """測試訪客模式下是否主錢包轉  """
#         self.test_driver.loginV2(identity='guest')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
#     def test_transferWallet_M2  _member(self):
#         """測試會員模式下是否主錢包轉  """
#         self.test_driver.loginV2()
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
#     def test_transferWallet_M2  _agentMember(self):
#         """測試代理會員模式下是否主錢包轉  """
#         self.test_driver.loginV2(identity='agent')
#         self.test_driver.transfer()
#         self.test_driver.transferPacket(start='主錢包', to='  ')
#
# if __name__ == '__main__':
#     unittest.main(testRunner = HTMLTestRunner())