import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

"""主要是快速打一輪ＡＰＩ進行快速測試與驗證"""

url = ''
hook = 'https://hooks.slack.com/services/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'
date = datetime.datetime.now()
token = []
GroupId=1239
PackageId = 10061
class GPGAPICheck:
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'authorization': 'Bearer %s' % self.access_token
        }

    def FriendList(self):
        api = "Friend/FriendList"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-好友列表有誤'}, headers={'Content-Type': 'application/json'})

    def ChatRoomList(self):
        api = "Chat/ChatRoomList"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-聊天室列表有誤'}, headers={'Content-Type': 'application/json'})

    def MemberWallet(self):
        api = "Member/MemberWallet"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-會員錢包有誤'}, headers={'Content-Type': 'application/json'})

    def MemberInfo(self):
        api = "Member/MemberInfo"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-會員資訊有誤'}, headers={'Content-Type': 'application/json'})

    def AvatarFrameRepository(self):
        api = "Member/AvatarFrameRepository"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-頭像框列表'}, headers={'Content-Type': 'application/json'})

    def OrderList(self):
        startDate = date.replace(day=1).strftime('%Y/%m/%d')
        api = 'Member/OrderList'
        if requests.get(url + api, headers=self.headers,
                        params={'StartDate': startDate, 'EndDate': date.strftime('%Y/%m/%d')}).json()['Status'][
            'Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-訂單紀錄有誤'}, headers={'Content-Type': 'application/json'})

    def TransactionRecord(self):
        api = 'Transaction/TransactionRecord'
        startDate = date.replace(day=1).strftime('%Y-%m-%dT%H:%M:%S+08:00')
        skip = 0
        show = 10
        if requests.get(url + api, headers=self.headers,
                        params={'StartDate': startDate, 'EndDate': date.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
                                'Skip': skip, 'Show': show}).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-贈禮紀錄有誤'}, headers={'Content-Type': 'application/json'})

    def HomeBanner(self):
        api = "Game/HomeBanner"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-首頁banner有誤'}, headers={'Content-Type': 'application/json'})

    def HomeHotGame(self):
        api = "Game/HomeHotGame"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-熱門遊戲有誤'}, headers={'Content-Type': 'application/json'})

    def NoviceSignIn7thList(self):
        api = "Activity/NoviceSignIn7thList"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-每日簽到列表有誤'}, headers={'Content-Type': 'application/json'})

    def SignIn9MonthList(self):
        api = "Activity/Normal/SignIn9MonthList"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-九月簽到列表有誤'}, headers={'Content-Type': 'application/json'})

    def SignIn9Month(self):
        api = "Activity/Normal/SignIn9Month"
        result=requests.post(url + api, headers=self.headers).json()
        if result['Status']['Code'] != '0' and result['Status']['Code'] != '4001':
            print(result)
            requests.post(hook, json={'text': '回歸測試-九月簽到有誤'}, headers={'Content-Type': 'application/json'})

    def ChatRoomText(self):
        api = 'Chat/ChatRoomText'
        if requests.get(url + api, headers=self.headers, params={'GroupID': GroupId, 'Skip': 0, 'Show': 1000}).json()[
            'Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-聊天列表有誤'}, headers={'Content-Type': 'application/json'})

    def SendChatText(self):
        api = 'Chat/SendChatText'
        if requests.post(url + api, headers=self.headers, json={"GroupID": GroupId, "Content": "automationtest"}).json()[
            'Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-傳送聊天訊息有誤'}, headers={'Content-Type': 'application/json'})

    def GameList(self):
        api = "Game/GameList"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-遊戲列表有誤'}, headers={'Content-Type': 'application/json'})

    def GameInfo(self):
        api = 'Game/GameInfo'
        if requests.get(url + api, headers=self.headers, params={'GameID': 12}).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-遊戲訊息有誤'}, headers={'Content-Type': 'application/json'})

    def RecommendGame(self):
        api = "game/RecommendGame"
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-推薦遊戲有誤'}, headers={'Content-Type': 'application/json'})

    # def UpdateMemberStatus(self):
    #     """有問題"""
    #     api='Member/UpdateMemberStatus'
    #     print(requests.post(url + api, headers=self.headers).text)

    def PackageList1(self):
        api = 'ElectronicMall/PackageList'
        if requests.get(url + api, headers=self.headers, params={'PaymentType': 1}).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-禮包列表有誤'}, headers={'Content-Type': 'application/json'})

    def PackageList2(self):
        api = 'ElectronicMall/PackageList'
        if requests.get(url + api, headers=self.headers, params={'PaymentType': 2}).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-禮包列表有誤'}, headers={'Content-Type': 'application/json'})

    def PackageList3(self):
        api = 'ElectronicMall/PackageList'
        if requests.get(url + api, headers=self.headers, params={'PaymentType': 3}).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-禮包列表有誤'}, headers={'Content-Type': 'application/json'})

    def BuyPackage(self):
        api = 'ElectronicMall/BuyPackage'
        if requests.post(url + api, headers=self.headers,
                         json={"PackageID":PackageId,"UniformInvoiceInfo":{"DonateMark":1,"NPOBAN":"919"}}).json()[
            'Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-購買禮包有誤'}, headers={'Content-Type': 'application/json'})

    def NickName(self):
        api = 'Member/NickName'
        if requests.post(url + api, headers=self.headers, json={"Nickname": str(time.time())}).json()['Status'][
            'Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-修改暱稱有誤'}, headers={'Content-Type': 'application/json'})

    def UpdateAvatar(self):
        api = 'Member/UpdateAvatar'
        if requests.post(url + api, headers=self.headers,
                         json={"AvatarID": ""}).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-更新頭像有誤'}, headers={'Content-Type': 'application/json'})

    def AvatarRepository(self):
        api = 'Member/AvatarRepository'
        if requests.get(url + api, headers=self.headers).json()['Status']['Code'] != '0':
            requests.post(hook, json={'text': '回歸測試-頭像列表有誤'}, headers={'Content-Type': 'application/json'})


# GPGAPICheck(token[0],token[1]).UpdateMemberStatus()
# """執行全部的method"""
x = GPGAPICheck(token[0], token[1])

public_method_names = [method for method in dir(x) if callable(getattr(x, method)) if not method.startswith('_')]
print(public_method_names)
for i in public_method_names:
    getattr(x, i)()
