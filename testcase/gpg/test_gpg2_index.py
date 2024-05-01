import unittest
from testcase.gpg2_chromeset import driver_eng,clean_resource,progressNotify
from selenium.webdriver.common.by import By
import time
import warnings
from testcase.HTMLTestReportCN import HTMLTestRunner
class Test_IndexPage(unittest.TestCase):
    def setUp(self):
        clean_resource()  # 開始砍進程
        self.test_driver = driver_eng()
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        self.test_driver.exit()
        
    @classmethod
    def setUpClass(cls):
        progressNotify(message='首頁測試開始')
        
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='首頁測試完成')
        
    def test_twitter_guest(self):
        """測試訪客模式下twitter是否有貼文＋入口按鈕"""
        self.test_driver.loginV2(identity='guest')
        res = self.test_driver.twitter()
        self.assertIsNotNone(res)

    def test_twitter_member(self):
        """測試會員模式下twitter是否有貼文＋入口按鈕"""
        self.test_driver.loginV2()
        res = self.test_driver.twitter()
        self.assertIsNotNone(res)

    def test_twitter_agentMember(self):
        """測試代理會員模式下twitter是否有貼文＋入口按鈕"""
        self.test_driver.loginV2(identity='agent')
        res = self.test_driver.twitter()
        self.assertIsNotNone(res)


    def test_gameList_guest(self):
        """測試訪客模式下熱門遊戲清單"""
        self.test_driver.loginV2(identity='guest')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__list")]')
        self.assertIsNotNone(res)

    def test_gameList_member(self):
        """測試會員模式下熱門遊戲清單"""
        self.test_driver.loginV2()
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__list")]')
        self.assertIsNotNone(res)

    def test_gameList_agentMember(self):
        """測試代理會員模式下熱門遊戲清單"""
        self.test_driver.loginV2(identity='agent')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__list")]')
        self.assertIsNotNone(res)

    def test_footer_guest(self):
        """測試訪客模式下 footer"""
        self.test_driver.loginV2(identity='guest')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"footer__container")]')
        self.assertIsNotNone(res)

    def test_footer_member(self):
        """測試會員模式下 footer"""
        self.test_driver.loginV2()
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"footer__container")]')
        self.assertIsNotNone(res)

    def test_footer_agentMember(self):
        """測試代理會員模式下 footer"""
        self.test_driver.loginV2(identity='agent')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"footer__container")]')
        self.assertIsNotNone(res)

    def test_gameRecommend_guest(self):
        """測試訪客模式下遊戲推薦"""
        self.test_driver.loginV2(identity='guest')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"latest__wrap")]')
        self.assertIsNotNone(res)

    def test_gameRecommend_member(self):
        """測試會員模式下遊戲推薦"""
        self.test_driver.loginV2()
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"latest__wrap")]')
        self.assertIsNotNone(res)

    def test_gameRecommend_agentMember(self):
        """測試代理會員模式下遊戲推薦"""
        self.test_driver.loginV2(identity='agent')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"latest__wrap")]')
        self.assertIsNotNone(res)

    def test_asideList_guest(self):
        """測試訪客模式下功能選單"""
        self.test_driver.loginV2(identity='guest')
        res,_ = self.test_driver.asideBar()
        self.assertEqual(['最新消息', '首頁', '遊戲', '商城', '序號', '門市據點', '', ''], res)

    def test_asideList_member(self):
        """測試會員模式下功能選單"""
        self.test_driver.loginV2()
        res,_ = self.test_driver.asideBar()
        self.assertEqual(['最新消息', '首頁', '遊戲', '商城', '序號', '門市據點', '', ''], res)

    def test_asideList_agentMember(self):
        """測試代理會員模式下功能選單"""
        self.test_driver.loginV2(identity='agent')
        res,_ = self.test_driver.asideBar()
        self.assertEqual(['最新消息', '首頁', '遊戲', '商城', '序號', '門市據點', '', ''], res)

    def test_logo_guest(self):
        """測試訪客模式下logo"""
        self.test_driver.loginV2(identity='guest')
        res = self.test_driver.driver.find_element(By.XPATH,'//img[@class="logo__img"]')
        self.assertIsNotNone(res)

    def test_logo_member(self):
        """測試會員模式下logo"""
        self.test_driver.loginV2()
        res = self.test_driver.driver.find_element(By.XPATH,'//img[@class="logo__img"]')
        self.assertIsNotNone(res)

    def test_logo_agentMember(self):
        """測試代理會員模式下logo"""
        self.test_driver.loginV2(identity='agent')
        res = self.test_driver.driver.find_element(By.XPATH,'//img[@class="logo__img"]')
        self.assertIsNotNone(res)

    def test_newGame_guest(self):
        """測試訪客模式下是否有新遊戲"""
        self.test_driver.loginV2(identity='guest')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__short__wrap")]')
        self.assertIsNotNone(res)

    def test_newGame_member(self):
        """測試會員模式下是否有新遊戲"""
        self.test_driver.loginV2()
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__short__wrap")]')
        self.assertIsNotNone(res)

    def test_newGame_agentMember(self):
        """測試代理會員模式下是否有新遊戲"""
        self.test_driver.loginV2(identity='agent')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"game__short__wrap")]')
        self.assertIsNotNone(res)

    def test_menuTool_guest(self):
        """測試訪客模式下是否會員功能bar"""
        self.test_driver.loginV2(identity='guest')
        res = self.test_driver.driver.find_elements(By.XPATH,'//div[contains(@class,"header__container")]/div[contains(@class,"menu__user")]/div')
        self.assertEqual(4 , len(res))

    def test_menuTool_member(self):
        """測試會員模式下是否成功有會員功能bar"""
        self.test_driver.loginV2()
        res = self.test_driver.driver.find_elements(By.XPATH,'//div[contains(@class,"header__container")]/div[contains(@class,"menu__user")]/div')
        self.assertEqual(4, len(res))

    def test_menuTool_agentMember(self):
        """測試代理會員模式下是否成功有會員功能bar"""
        self.test_driver.loginV2(identity='agent')
        res = self.test_driver.driver.find_elements(By.XPATH,'//div[contains(@class,"header__container")]/div[contains(@class,"menu__user")]/div')
        self.assertEqual(4, len(res))

    def test_miningIcon_guest(self):
        """測試訪客模式下點擊礦機"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.mining()
        res=self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__view")]')
        self.assertIsNotNone(res)

    def test_miningIcon_noLogin(self):
        """測試未登入模式下點擊礦機"""
        self.test_driver.mining()
        res=self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"drawer__block")]')
        self.assertIsNotNone(res)

    def test_miningIcon_member(self):
        """測試會員模式下點擊礦機"""
        self.test_driver.loginV2()
        self.test_driver.mining()
        # self.test_driver.driver.switch_to.window(self.test_driver.driver.window_handles[1])
        # res=self.test_driver.driver.find_element(By.XPATH,'//canvas[@id="GameCanvas"]')
        # self.assertIsNotNone(res)
    def test_miningIcon_agentMember(self):
        """測試代理會員模式下點擊礦機"""
        self.test_driver.loginV2(identity='agent')
        self.test_driver.mining()
        # self.test_driver.driver.switch_to.window(self.test_driver.driver.window_handles[1])
        # res=self.test_driver.driver.find_element(By.XPATH,'//canvas[@id="GameCanvas"]')
        # self.assertIsNotNone(res)
    
    def test_memberSelect_Sound(self):
        """測試訪客是否有音效設定"""
        self.test_driver.logout(set_option='音效設定')
        res = self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"pop-view__container")]')
        self.assertIsNotNone(res)
    # def test_SignIn_member(self):
    #     """測試會員模式下簽到月簽"""
    #     self.test_driver.loginV2()
    #     res = self.test_driver.signIn(func='月簽到')
    #     try:
    #         list(filter(lambda x:x.text == "簽到",res)).pop().click()
    #         self.test_driver.reload()
    #         res = self.test_driver.signIn(func='月簽到')
    #         self.assertIsNotNone(list(filter(lambda x: x.text == "已領取", res)).pop())
    #     except:
    #         self.assertIsNotNone(list(filter(lambda x: x.text == "已領取", res)).pop())
    #
    # def test_SignIn_agentMember(self):
    #     """測試代理會員模式下簽到月簽"""
    #     self.test_driver.loginV2(identity='agent')
    #     res = self.test_driver.signIn(func='月簽到')
    #     try:
    #         list(filter(lambda x:x.text == "簽到",res)).pop().click()
    #         self.test_driver.reload()
    #         res = self.test_driver.signIn(func='月簽到')
    #         self.assertIsNotNone(list(filter(lambda x: x.text == "已領取", res)).pop())
    #     except:
    #         self.assertIsNotNone(list(filter(lambda x: x.text == "已領取", res)).pop())
    
    # def test_SignInClose_member(self):
    #     """測試會員模式下關閉月簽"""
    #     self.test_driver.loginV2()
    #     res = self.test_driver.signIn(func="月簽到")
    #     list(filter(lambda x:x.text == "關閉",res)).pop().click()
    #     # res = re.compile('<div class="event__mask .*?"></div>',re.M).findall(self.test_driver.driver.page_source)
    #     self.assertEqual(self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"event__mask")]').is_displayed(),False)
    #
    # def test_SignInClose_agentMember(self):
    #     """測試代理會員模式下關閉月簽"""
    #     self.test_driver.loginV2(identity='agent')
    #     res = self.test_driver.signIn(func="月簽到")
    #     list(filter(lambda x:x.text == "關閉",res)).pop().click()
    #     # res=re.compile('<div class="event__mask .*?"></div>',re.M).findall(self.test_driver.driver.page_source)# 優化之後在嘗試改寫
    #     self.assertEqual(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"event__mask")]').is_displayed(),False)
    
    def test_gameRank_guest(self):
        """測試訪客模式下是否有遊戲排行榜"""
        self.test_driver.loginV2(identity='guest')
        self.test_driver.gameRank()
        self.assertIsNotNone(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"rank__container")]/div[contains(@class,"game__wrap")]'))

if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())