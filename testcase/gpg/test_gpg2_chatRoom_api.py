import time
from testcase.gpg2_chromeset import gpg_api,progressNotify,FontAPI
import unittest
from testcase.HTMLTestReportCN import HTMLTestRunner
import logging
import inspect
class Test_ChatRoom_api(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
        # time.sleep(2)
    @classmethod
    def setUpClass(cls):
        progressNotify(message='聊天室API測試開始')
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='聊天室API測試完成')
    def test_SendChat_member_api(self):
        """測試會員模式下是否可以聊天"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='memberToken')
        get_friend = [i for i in
                      self.api.apiGetData(method='get', api_url=FontAPI.friend_friendList.value).get('Data') if
                      i.get('FriendID') not in []].pop()
        get_chat_group = self.api.apiGetData(method='get', payload={"FriendID": get_friend.get('FriendID')},
                                             api_url=FontAPI.chat_chatGroup.value)
        res = self.api.apiGetData(method='post', data={"GroupID": get_chat_group.get('GroupID'), "Content": "c8763"},
                                  api_url=FontAPI.chat_sendChatText.value)
        self.assertEqual(res['Status']['Message'], 'Success')

    def test_SendChat_memberAgent_api(self):
        """測試代理會員模式下是否可以聊天"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        self.api = gpg_api(token='agentToken')
        get_friend = [i for i in
                      self.api.apiGetData(method='get', api_url=FontAPI.friend_friendList.value).get('Data') if
                      i.get('FriendID') not in [-998, -999]].pop()
        get_chat_group = self.api.apiGetData(method='get', payload={"FriendID": get_friend.get('FriendID')},
                                             api_url=FontAPI.chat_chatGroup.value)
        res = self.api.apiGetData(method='post', data={"GroupID": get_chat_group.get('GroupID'), "Content": "c8763"},
                                  api_url=FontAPI.chat_sendChatText.value)
        self.assertEqual(res['Status']['Message'], 'Success')
        
    def test_RecommendList_guest_api(self):
        """測試訪客模式下是否可以查詢推薦好友"""
        self.api = gpg_api(token='guestToken')
        res = self.api.apiGetData(method='get', payload={},api_url=FontAPI.friend_recommendList.value)
        self.assertEqual(res, '')
    def test_RecommendList_member_api(self):
        """測試會員模式下是否可以查詢推薦好友"""
        self.api = gpg_api(token='memberToken')
        res = self.api.apiGetData(method='get', payload={},api_url=FontAPI.friend_recommendList.value)
        self.assertEqual(res['Status']['Message'], 'Success')
    def test_RecommendList_agentMember_api(self):
        """測試代理會員模式下是否可以查詢推薦好友"""
        self.api = gpg_api(token='agentToken')
        res = self.api.apiGetData(method='get', payload={},api_url=FontAPI.friend_recommendList.value)
        self.assertEqual(res['Status']['Message'], 'Success')
        

if __name__ == '__main__':
    unittest.main(testRunner = HTMLTestRunner())
    