import unittest
from testcase.gpg2_chromeset import driver_eng,ma_api,gpg_api, progressNotify,AdIdLevel,FontAPI,BackAPI,env,clean_resource
import warnings
from selenium.webdriver.common.by import By
import sys
import re
import time
from script.utils import TimeSelect
sys.path.append('../..')
time_select = TimeSelect()
class Test_RegisterFunction(unittest.TestCase):
    """註冊總邏輯"""
    def setUp(self):
        clean_resource()
        warnings.simplefilter('ignore', ResourceWarning)
        self.test_driver = driver_eng()

    def tearDown(self):
        pass
        # self.test_driver.exit()
    @classmethod
    def setUpClass(cls):
        progressNotify(message='註冊總測試開始')
    @classmethod
    def tearDownClass(cls):
        progressNotify(message='註冊總邏輯測試結束')
    @unittest.skipIf(env['env'] == 'prod','正式站跳過')
    def test_00_delete(self):
        """測試註冊的前置刪除作業"""
        self.api=ma_api()
        member = list()
        res =list(map(lambda x:self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc','IsGuest': False, 'PhoneNumber': x})['Data'],
                      ['  ','  ','  ','  ']))
        for i in res:
            member.extend(i)
        list(map(lambda x:self.api.apiGetData(method='post', api_url=BackAPI.member_disable.value, data={"MemberId": x.get('MemberID')}),member))
        res = list(map(lambda x: x.get('MemberID') , self.api.apiGetData(method='get', api_url=BackAPI.member_advertisersList.value,payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0, 'Show': 50,'PhoneNumber':'  ','Field': 'CreateTime', 'OrderType': 'desc'})['Data']))
        [self.api.apiGetData(method='post', api_url=BackAPI.member_disable.value,data={"MemberId": i}) for i in res]
        
    @unittest.skipIf(env['env'] == 'prod','正式站跳過')
    def test_10_agm_way_serialNoRegister(self):
        """測試AGM會員是否可以透過輸入序號方式掛線"""
        member = '  0'
        self.api=ma_api(account=env['agent_account'],password=env['agent_password'])
        self.test_driver.loginV2(member_account=member)
        time.sleep(10)
        # self.test_driver.orderNo(present_code=env['agent_introduction'],mode='PromoteCode')
        # res = self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc','IsGuest': False, 'PhoneNumber': member})['Data'].pop()
        # self.assertEqual(res['PhoneNumber'],member)
        
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_11_agm_way_promoteRegister(self):
        """測試AGM會員是否可以透過點擊網址註冊方式掛線"""
        member = '  1'
        self.api=ma_api(account=env['agent_account'],password=env['agent_password'])
        self.test_driver.driver.get(url=f'{env["font_url"]}?promote={env["agent_introduction"]}')
        self.test_driver.loginV2(member_account=member)
        res = self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc','IsGuest': False, 'PhoneNumber': member})['Data'].pop()
        self.assertEqual(res['PhoneNumber'],member)

    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_12_agm_way_guestPromoteRegister(self):
        """測試AGM會員是否可以訪客點擊網址註冊方式掛線"""
        member = '  2'
        self.api=ma_api(account=env['agent_account'],password=env['agent_password'])
        self.test_driver.loginV2(identity='guest')
        self.test_driver.driver.get(url=f'{env["font_url"]}?promote={env["agent_introduction"]}')
        self.test_driver.loginV2(member_account=member)
        res = self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc','IsGuest': False, 'PhoneNumber': member})['Data'].pop()
        self.assertEqual(res['PhoneNumber'],member)

    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_13_agm_way_memberPromoteRegister(self):
        """測試AGM會員是否可以會員點擊網址註冊方式掛線"""
        member = '  3'
        self.api=ma_api(account=env['agent_account'],password=env['agent_password'])
        self.test_driver.loginV2(member_account=member)
        self.test_driver.driver.get(url=f'{env["font_url"]}?promote={env["agent_introduction"]}')
        res = self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc', 'IsGuest': False, 'PhoneNumber': member})['Data'].pop()
        self.assertEqual(res['PhoneNumber'], member)

    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_20_mgm_way_IntroductionRegister(self):
        """測試MGM會員是否可以會員點擊網址註冊方式掛線"""
        member = '  4'
        self.api=ma_api()
        self.test_driver.driver.get(url=f'{env["font_url"]}?introduction={env["member_introduction"]}')
        self.test_driver.loginV2(member_account=member)
        res = self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc','IsGuest': False, 'PhoneNumber': member})['Data'].pop()
        self.assertEqual(res['IntroducePhoneNumber'],env['member_account'])
        
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_21_mgm_way_guestIntroductionRegister(self):
        """測試MGM會員是否可以訪客點擊網址註冊方式掛線"""
        member = '  5'
        self.api = ma_api()
        self.test_driver.loginV2(identity='guest')
        self.test_driver.driver.get(url=f'{env["font_url"]}?introduction={env["member_introduction"]}')
        self.test_driver.loginV2(member_account=member)
        res = self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc','IsGuest': False, 'PhoneNumber': member})['Data'].pop()
        self.assertEqual(res['IntroducePhoneNumber'],env['member_account'])
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_30_A_agent_Register(self):
        """測試代理推廣頁註冊A代理"""
        self.api = ma_api()
        self.gpg_api=gpg_api()
        phone = '  4'
        res = self.api.apiGetData(api_url=BackAPI.member_inviteFranchisee.value, method='post',data={"Greeting": "歡迎成為GPG的廣告加盟商！GPG廣告加盟商後台網址: https://manage-gpg.ceis.tw"})['Data']['Url']
        token = re.compile(r"  /\?token=(.*)", re.S).findall(res).pop()
        account = 'A' + str(int(time.time()))
        self.gpg_api.apiGetData(method='post',api_url=FontAPI.franchisee_createFranchisee.value,data={"Token": token, "NickName": account,"Account": account,"Password": account})
        self.test_driver.loginV2(identity='agent',agent_account=account,agent_password=account)
        self.test_driver.loginV2(member_account=phone)
        self.test_driver.closeDaily()
        self.test_driver.memberSelect('會員中心')
        level = re.compile('Lv\.([0-9]+)', re.S).findall(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"info-vip__label")]').text).pop()
        self.assertEqual(level, '13')
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_31_B_agent_Register(self):
        """測試代理推廣頁註冊B代理"""
        self.api = ma_api(account='QAminiag20',password='QAminiag20')
        self.gpg_api = gpg_api()
        res = self.api.apiGetData(api_url=BackAPI.member_inviteFranchisee.value,method='post',
                           data={"Greeting": "歡迎成為GPG的廣告加盟商！GPG廣告加盟商後台網址: https://manage-gpg.ceis.tw"})['Data']['Url']
        token = re.compile("  /\?token=(.*)", re.S).findall(res).pop()
        account='B' + str(int(time.time()))
        phone = '  5'
        self.gpg_api.apiGetData(method='post',api_url=FontAPI.franchisee_createFranchisee.value,data={"Token": token, "NickName": account,
                                        "Account": account,
                                        "Password": account})
        self.test_driver.loginV2(identity='agent', passredis=True, agent_account=account, agent_password=account)
        self.test_driver.loginV2(member_account=phone)
        self.test_driver.closeDaily()
        self.test_driver.memberSelect('會員中心')
        level = re.compile('Lv\.([0-9]+)', re.S).findall(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"info-vip__label")]').text).pop()
        self.assertEqual(level, '11')
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_32_C_agent_Register(self):
        """測試代理推廣頁註冊C代理"""
        self.api = ma_api(account='  ',password='  ')
        self.gpg_api = gpg_api()
        res = self.api.apiGetData(api_url=BackAPI.member_inviteFranchisee.value, method='post',
                                 data={"Greeting": "歡迎成為GPG的廣告加盟商！GPG廣告加盟商後台網址: https://manage-gpg.ceis.tw"})['Data']['Url']
        token = re.compile("  /\?token=(.*)", re.S).findall(res).pop()
        account = 'C' + str(int(time.time()))
        phone = '  6'
        self.gpg_api.apiGetData(method='post',api_url=FontAPI.franchisee_createFranchisee.value,data={"Token": token, "NickName": account,"Account": account,"Password": account})
        self.test_driver.loginV2(identity='agent',agent_account=account, agent_password=account)
        self.test_driver.loginV2(member_account=phone)
        self.test_driver.closeDaily()
        self.test_driver.memberSelect('會員中心')
        level = re.compile('Lv\.([0-9]+)', re.S).findall(self.test_driver.driver.find_element(By.XPATH,'//div[contains(@class,"info-vip__label")]').text).pop()
        self.assertEqual(level, '5')
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_33_A_agent_member_20Can(self):
        """測試A代理註冊滿5個會增送20個罐頭"""
        self.api = ma_api()
        res = self.api.apiGetData(method='get',api_url=BackAPI.dataReport_promoteReport.value,payload={'StatusID':2,'IsFuzzySearch': True, 'Skip': 0,'Show': 50,'Field': 'CreateTime','OrderType': 'desc','AdID': AdIdLevel.a_agent.value})['Data']
        a_agent=list(filter(lambda x: re.compile('[A][0-9]{10}', re.S).findall(x['MemberAccount']),res)).pop()
        member_list = ['  0','  1','  2','  3','  4']
        for i in member_list:
            self.test_driver.driver.get(url=f'{env["font_url"]}?promote={a_agent["PromoteCode"]}')
            self.test_driver.loginV2(member_account=i)
            self.test_driver.logout()
        self.test_driver.loginV2(identity='agent',passredis=True,account=a_agent['MemberAccount'], password=a_agent['MemberAccount'])
        self.gpg_api = gpg_api(token=self.test_driver.token)
        package_res = list(filter(lambda x:x.get('PackageName')=='註冊推廣禮包',self.gpg_api.apiGetData(method='get', payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},api_url=FontAPI.member_orderList.value)['Data'])).pop()
        self.assertEqual(bool((package_res['ItemData']['CanName']=='罐頭') and (package_res['ItemData']['CanQuantity']==20)),True)
        res = list(map(lambda i: i.get('MemberID'),self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc', 'IsGuest': False, 'PhoneNumber': '  '})['Data']))
        res.append(a_agent['MemberID'])
        [self.api.apiGetData(method='post', api_url=BackAPI.member_disable.value, data={"MemberId": i}) for i in res]
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_34_B_agent_member_20Can(self):
        """測試B代理註冊滿5個會增送20個罐頭"""
        self.api = ma_api()
        res = self.api.apiGetData(method='get',api_url=BackAPI.dataReport_promoteReport.value,payload={'StatusID':2,'IsFuzzySearch': True, 'Skip': 0,'Show': 50,'Field': 'CreateTime','OrderType': 'desc','AdID': AdIdLevel.b_agent.value})['Data']
        b_agent=list(filter(lambda x: re.compile('[B][0-9]{10}', re.S).findall(x['MemberAccount']),res)).pop()
        member_list = ['  0','  1','  2','  3','  4']
        for i in member_list:
            self.test_driver.driver.get(url=f'{env["font_url"]}?promote={b_agent["PromoteCode"]}')
            self.test_driver.loginV2(member_account=i)
            self.test_driver.logout()
        self.test_driver.loginV2(identity='agent',passredis=True,account=b_agent['MemberAccount'], password=b_agent['MemberAccount'])
        self.gpg_api = gpg_api(token=self.test_driver.token)
        package_res = list(filter(lambda x:x.get('PackageName')=='註冊推廣禮包',self.gpg_api.apiGetData(method='get', payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},api_url=FontAPI.member_orderList.value)['Data'])).pop()
        self.assertEqual(bool((package_res['ItemData']['CanName']=='罐頭') and (package_res['ItemData']['CanQuantity']==20)),True)
        res = list(map(lambda i: i.get('MemberID'),self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc', 'IsGuest': False, 'PhoneNumber': '  '})['Data']))
        res.append(b_agent['MemberID'])
        [self.api.apiGetData(method='post', api_url=BackAPI.member_disable.value, data={"MemberId": i}) for i in res]
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_35_C_agent_member_20Can(self):
        """測試C代理註冊滿5個會增送20個罐頭"""
        self.api = ma_api()
        res = self.api.apiGetData(method='get',api_url=BackAPI.dataReport_promoteReport.value,payload={'StatusID':2,'IsFuzzySearch': True, 'Skip': 0,'Show': 50,'Field': 'CreateTime','OrderType': 'desc','AdID': AdIdLevel.c_agent.value})['Data']
        c_agent=list(filter(lambda x: re.compile('[C][0-9]{10}', re.S).findall(x['MemberAccount']),res)).pop()
        member_list = ['  0','  1','  2','  3','  4']
        for i in member_list:
            self.test_driver.driver.get(url=f'{env["font_url"]}?promote={c_agent["PromoteCode"]}')
            self.test_driver.loginV2(member_account=i)
            self.test_driver.logout()
        self.test_driver.loginV2(identity='agent',passredis=True,account=c_agent['MemberAccount'], password=c_agent['MemberAccount'])
        self.gpg_api = gpg_api(token=self.test_driver.token)
        package_res = list(filter(lambda x:x.get('PackageName')=='註冊推廣禮包',self.gpg_api.apiGetData(method='get', payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},api_url=FontAPI.member_orderList.value)['Data'])).pop()
        self.assertEqual(bool((package_res['ItemData']['CanName']=='罐頭') and (package_res['ItemData']['CanQuantity']==20)),True)
        res = list(map(lambda i: i.get('MemberID'),self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc', 'IsGuest': False, 'PhoneNumber': '  '})['Data']))
        res.append(c_agent['MemberID'])
        [self.api.apiGetData(method='post', api_url=BackAPI.member_disable.value, data={"MemberId": i}) for i in res]
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_36_mgm_member_20Can(self):
        """測試會員註冊滿5個會增送20個罐頭"""
        self.api=ma_api()
        member = '  6'
        self.test_driver.loginV2(member_account=member)
        self.gpg_api = gpg_api(token=self.test_driver.token)
        member_info = self.gpg_api.apiGetData(method='get',api_url=FontAPI.member_memberInfo.value)['Data']
        self.test_driver.logout()
        member_list = ['  0','  1','  2','  3','  4']
        for i in member_list:
            self.test_driver.driver.get(url=f'{env["font_url"]}?introduction={member_info["IntroduceCode"]}')
            self.test_driver.loginV2(member_account=i)
            self.test_driver.logout()
        package_res = list(filter(lambda x:x.get('PackageName')=='註冊推廣禮包',self.gpg_api.apiGetData(method='get', payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},api_url=FontAPI.member_orderList.value)['Data'])).pop()
        self.assertEqual(bool((package_res['ItemData']['CanName']=='罐頭') and (package_res['ItemData']['CanQuantity']==20)),True)
        res = list(map(lambda i: i.get('MemberID'),self.api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50, 'Field': 'CreateTime',"OrderType": 'desc', 'IsGuest': False, 'PhoneNumber': '  '})['Data']))
        res.append(member_info['MemberID'])
        [self.api.apiGetData(method='post', api_url=BackAPI.member_disable.value, data={"MemberId": i}) for i in res]
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_40_agm_bonusPresent(self):
        """測試agm回贈禮"""
        self.gpg_api = gpg_api(token='agentToken')
        res = self.gpg_api.apiGetData(method='get',payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},api_url=FontAPI.member_orderList.value)['Data'][0]
        self.assertEqual(bool((res['PackageName'] == "邀請互贈禮包(A)") and (res['ItemData']['CanQuantity']==3)),True)
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_50_agm_newPresent(self):
        """測試agm新手禮"""
        member = '  3'
        self.test_driver.loginV2(member_account=member)
        self.gpg_api = gpg_api(token=self.test_driver.token)
        res = self.gpg_api.apiGetData(method='get',payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},api_url=FontAPI.member_orderList.value)['Data'][0]
        self.assertEqual(bool((res['PackageName'] == "高雄鳳山元宇宙概念店額外禮包") and (res['GoldPoint'] == 688) and (res['SilverPoint'] == 30000) and (res['ItemData']['CanQuantity'] == 1)), True)
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_60_mgm_bonusPresent(self):
        """測試mgm回贈禮"""
        self.gpg_api = gpg_api(token='memberToken')
        res = self.gpg_api.apiGetData(method='get',payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},api_url=FontAPI.member_orderList.value)['Data'][0]
        self.assertEqual(bool((res['PackageName'] == "邀請互贈禮包(M)") and (res['GoldPoint'] == 1000) and (res['SilverPoint'] == 30000) and (res['ItemData']['CanQuantity']==3)),True)
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_70_mgm_newPresent(self):
        """測試mgm新手禮"""
        member = '  5'
        self.test_driver.loginV2(member_account=member)
        self.gpg_api = gpg_api(token=self.test_driver.token)
        res = self.gpg_api.apiGetData(method='get',payload={'StartDate': time_select.MonthStart(), 'EndDate': time_select.MonthEnd()},api_url=FontAPI.member_orderList.value)['Data'][0]
        self.assertEqual(bool((res['PackageName'] == "邀請專屬額外禮包(M)") and (res['GoldPoint'] == 688) and (res['SilverPoint'] == 30000) and (res['ItemData']['CanQuantity'] == 1)), True)
        
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_80_ChangeRole_memberToAgent(self):
        phone = '  0'
        self.ma_api = ma_api()
        member = self.ma_api.apiGetData(method='get', api_url=BackAPI.member_memberList.value,payload={'IsFuzzySearch': True, 'Skip': 0, 'Show': 50,'Field': 'CreateTime', "OrderType": 'desc','IsGuest': False,'PhoneNumber': phone})['Data'].pop()
        member_info = list(filter(lambda x:x.get('TargetAdId')==AdIdLevel.c_agent.value,self.ma_api.apiGetData(method='get', api_url=BackAPI.member_roleChangeDetail.value,payload={'MemberId': member['MemberID']})['Data']['ChangeType'])).pop()
        ac_pw ='CC' + str(int(time.time()))
        self.ma_api.apiGetData(method='post', api_url=BackAPI.member_roleChange.value,data={"MemberId": member['MemberID'],"TargetAdId": member_info['TargetAdId'],"UpMemberId": member_info['UpperId'],"Account": ac_pw,"Password": ac_pw})
        advertisers = self.ma_api.apiGetData(method='get', api_url=BackAPI.member_advertisersList.value,payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0,'Show': 50, 'PhoneNumber': phone, 'Field': 'CreateTime','OrderType': 'desc'})['Data'].pop()
        self.assertEqual(advertisers['AdId'], AdIdLevel.c_agent.value)
        
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_91_ChangeRole_NewAgentLevel(self):
        """C代理等級是否正確"""
        phone = '  0'
        self.ma_api = ma_api()
        member = self.ma_api.apiGetData(method='get', api_url=BackAPI.member_advertisersList.value,payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0, 'Show': 50,'PhoneNumber': phone, 'Field': 'CreateTime', 'OrderType': 'desc'})['Data'].pop()
        self.test_driver.loginV2(identity='agent', agent_account=member['MemberAccount'], agent_password=member['MemberAccount'])
        self.test_driver.memberSelect('會員中心')
        level = re.compile('Lv\.([0-9]+)', re.S).findall(self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"info-vip__label")]').text).pop()
        self.assertEqual(level, '5')
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_92_memberTo_C_agent(self):
        """C轉B是否成功"""
        phone = '  0'
        self.ma_api = ma_api()
        member = self.ma_api.apiGetData(method='get', api_url=BackAPI.member_advertisersList.value,payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0,'Show': 50, 'PhoneNumber': phone , 'Field': 'CreateTime','OrderType': 'desc'})['Data'].pop()
        member_info = list(filter(lambda x:x.get('TargetAdId')==AdIdLevel.b_agent.value,self.ma_api.apiGetData(method='get', api_url=BackAPI.member_roleChangeDetail.value,payload={'MemberId': member['MemberID']})['Data']['ChangeType'])).pop()
        self.ma_api.apiGetData(method='post', api_url=BackAPI.member_roleChange.value,data={"MemberId": member['MemberID'],"TargetAdId": member_info['TargetAdId'],"UpMemberId": member_info['UpperId']})
        self.test_driver.loginV2(identity='agent', account=member['MemberAccount'], password=member['MemberAccount'], passredis=True)
        self.test_driver.memberSelect('會員中心')
        level = re.compile('Lv\.([0-9]+)', re.S).findall(self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"info-vip__label")]').text).pop()
        self.assertEqual(level, '11')
    @unittest.skipIf(env['env'] == 'prod', '正式站跳過')
    def test_93_memberTo_C_agent(self):
        """B代理轉會員"""
        phone = '  0'
        self.ma_api = ma_api()
        member = self.ma_api.apiGetData(method='get', api_url=BackAPI.member_advertisersList.value,
                                     payload={'IsFuzzySearch': True, 'SearchDescents': False, 'Skip': 0,
                                              'Show': 50, 'PhoneNumber': phone, 'Field': 'CreateTime',
                                              'OrderType': 'desc'})['Data'].pop()
        member_info = list(filter(lambda x: x.get('TargetAdId') == AdIdLevel.member.value,
                                  self.ma_api.apiGetData(method='get', api_url=BackAPI.member_roleChangeDetail.value,
                                                      payload={'MemberId': member['MemberID']})['Data']['ChangeType'])).pop()
        self.ma_api.apiGetData(method='post', api_url=BackAPI.member_roleChange.value,
                            data={"MemberId": member['MemberID'], "TargetAdId": member_info['TargetAdId'],
                                  "UpMemberId": member_info['UpperId']})
        self.test_driver.loginV2(member_account=phone)
        self.test_driver.memberSelect('會員中心')
        level = re.compile('Lv\.([0-9]+)', re.S).findall(self.test_driver.driver.find_element(By.XPATH, '//div[contains(@class,"info-vip__label")]').text).pop()
        self.assertEqual(level, '0')
"""
此為整理所有註冊邏輯
1.會員可以透過序號輸入，一進來掛連結，訪客完成掛連結，事後註冊完成之後再掛連結(兩個禮拜)皆可成為AGM
2.會員可以一進來掛連結，訪客完成掛連結皆可成為MGM
3.當一個代理或者會員有成功推廣會員數達5個人會送神奇罐頭 20個
4.AGM(丟連結)會回贈 神奇罐頭 3個
5.AGM(被邀請)會贈與 金幣688 銀幣30,000 神奇罐頭 1
6.MGM(丟連結)會回贈 金幣1,000 銀幣 30,000 神奇罐頭 3個
7.MGM(被邀請)會贈與 金幣688 銀幣30,000 神奇罐頭 1個
8.代理層級在後台發出各自的推廣註冊頁發展註冊下線
9.相關換線流程
10.會不定期有代理推廣連結會有特殊礦寵禮包,目前測試站設定921的預設推廣連結為 礦寵-咪塔 922 推廣連結 為 礦寵-黑糖
11.929 939 928 三位為模擬實體核銷的紅菓咖啡帳號可進行實體兌換回歸測試不能刪除也不能改密碼
12.新增Email欄位註冊
備註:由代理推廣5位代理沒有拿到20個罐頭屬正常
 """
