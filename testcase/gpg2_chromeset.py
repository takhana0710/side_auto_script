from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 座標點擊
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random
import re
import requests
import logging
import json
from enum import Enum
import sys
import os
from env import sys_parameter
import uuid
from testcase.gcp.excel import mail
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--site", type=str)
args = vars(ap.parse_args())
env = sys_parameter(args['site'])

class TransferDict(Enum):  # 錢包建構
    gpg_gold = 1
    VASlot_gold = 220101
    VABattle_gold = 220103
    gpg_silver = 2
    VASlot_silver = 220102
    VABattle_silver = 220104
    IFUN_gold = 90601
    # MK_gold = 131101
    # MK_silver=131102
    crowdplay_gold=31601

class AdIdLevel(Enum):
    admin_company = 1
    a_agent = 2
    b_agent = 3
    c_agent = 4
    agm = 11
    member = 12

def clean_resource():  # 預先砍 區別整個類別砍
    """砍進程"""
    os.system('taskkill /im chromedriver.exe /F')  # 砍進程
    os.system('taskkill /im chrome.exe /F')


def progressNotify(message):
    """通知進度條打slack到我的帳號"""
    hook = 'https://hooks.slack.com/services/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'
    requests.post(hook, json={'text': message}, headers={'Content-Type': 'application/json'})


class gpg_api:
    
    def __init__(self, **kwargs):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'accept': 'application/json, text/plain, */*'
        }
        # if kwargs.get('token') in ['guestToken', 'memberToken', 'agentToken']:  # ＡＰＩ採取 token 直撈 redis
        #     self.token = r.get(kwargs.get('token'))
        # else:
        #     self.token = kwargs.get('token')
        self.token = kwargs.get('token')
        self.headers['authorization'] = 'Bearer %s' % self.token
    
    def apiGetData(self, **kwargs):
        """
        :param kwargs:
        method:request method
        api_url:api_url
        data:post json
        payload: get url payload
        :return:
        """
        method = kwargs.get('method')
        apiUrl = kwargs.get('api_url')
        data = kwargs.get('data')
        payload = kwargs.get('payload')
        logging.info('testcase parameter:' + str(kwargs))
        try:
            if method == 'get':
                res = requests.get(apiUrl, data=data, params=payload, headers=self.headers)
                logging.info('response statuscode:' + str(res.status_code))
                logging.info('response text:' + str(res.text))
            else:
                # print(apiUrl+'\t'+str(data)+'\t'+str(self.headers))
                res = requests.post(apiUrl, json=data, headers=self.headers)
                print(res.status_code)
                print(res.text)
                logging.info('response statuscode:' + str(res.status_code))
                logging.info('response text:' + str(res.text))
            return res.json()
        except:
            # print(apiUrl + '\t' + data + '\t' + self.headers)
            if method == 'get':
                res = requests.get(apiUrl, data=data, params=payload, headers=self.headers)
                logging.info('response statuscode:' + str(res.status_code))
                logging.info('response text:' + str(res.text))
            else:
                res = requests.post(apiUrl, json=data, params=payload, headers=self.headers)
                logging.info('response statuscode' + str(res.status_code))
                logging.info('response text:' + str(res.text))
            return res.text
    
    # def cleanRedis(self, **kwargs):
    #     r.delete('%sToken' % kwargs.get('auth'))
    #     r.delete('%sRefresh' % kwargs.get('auth'))

def nickname_fun():
        res = str(uuid.uuid4())[:8]
        return res

class driver_eng:
    def __init__(self, **kwargs):  # 共模
        kwargs.setdefault('url',env['font_url'])
        kwargs.setdefault('ua_platform','desktop')
        if kwargs.get('url') != None:
            url = kwargs.get('url')
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
        options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        options.add_experimental_option("excludeSwitches",['enable-automation'])
        options.add_experimental_option("excludeSwitches", ['enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-software-rasterizer')
        if kwargs.get('ua_platform') == 'phone':
            options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 14 Pro Max"})
        # options.add_argument("--auto-open-devtools-for-tabs") # 開發者模式
        # prefs = {'download.default_directory': os.getenv('OS_LOG_PATH'),'intl.accept_languages': 'zh_TW'}
        # options.add_experimental_option('prefs',prefs)
        # capabilities = DesiredCapabilities.CHROME
        # capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        options.add_argument('--start-maximized')
        options.add_argument('--mute-audio')
        if sys.platform == 'linux':
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=options)
            self.driver.set_window_size(800,600)
        else:
            self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)
        # self.per_time = json.loads(self.driver.execute_script('return JSON.stringify(window.performance.timing)')))
        # self.per_getEntries = json.loads(self.driver.execute_script('return JSON.stringify(window.performance.getEntries())'))
        self.wait = WebDriverWait(self.driver, 10, 0.5)
    
    def view_source(self, **kwargs):  # 查看code
        if kwargs.get('url'):
            self.driver.get(kwargs.get('url'))
            with open('{filename}.html'.format(filename=kwargs.get('filename')), 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
                f.close()
        else:
            with open('{filename}.html'.format(filename=kwargs.get('filename')), 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
                f.close()
    
    def reload(self):  # 重新刷新頁面
        self.driver.execute_script("location.reload(true);")
        self.closeDaily()
    
    def asideBarSelect(self, **kwargs):
        """選擇側邊主選單"""
        res_text, res = self.asideBar()
        res = list(filter(lambda i: i.find_element(By.XPATH, './div/span').text == kwargs.get('fun_text'), res)).pop()
        self.driver.execute_script("arguments[0].click();", res)
        self.driver.implicitly_wait(10)
        # [i.find_element(By.XPATH, './div') for i in res[:5] if
        #  i.find_element(By.XPATH, './div/span').text == fun_text].pop().click()
    
    def changeLanguage(self):
        """切換語系"""
        self.driver.implicitly_wait(1)
        if self.driver.find_elements(By.XPATH, '//div[contains(@class,"menu__member")]/div'):
            self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH, '//div[contains(@class,"menu__member")]/div'))
        else:
            self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH, '//div[contains(@class,"menu__member")]/img'))
        self.driver.find_element(By.XPATH,'//span[text()="設定" or text()="Settings" or text()="オプション"]').click()
        self.driver.find_element(By.XPATH,'//div[text()="語系設定" or (text()="Language Settings" or text()="言語設定")]').click()
        res = gpg_api().apiGetData(method='get',api_url=FontAPI.token_locale.value)
        self.driver.find_element(By.XPATH,f'//div[text()="{res["Data"][0]["LocaleName_zhTW"]}"]').click()
        self.driver.find_element(By.XPATH,'//div[contains(@class,"gift__close-bg")]').click()

    def loginV2(self,**kwargs):
        kwargs.setdefault('send_site','')
        kwargs.setdefault('identity', 'member')
        kwargs.setdefault('member_account', env['member_account'])
        kwargs.setdefault('agent_account', env['agent_account'])
        kwargs.setdefault('agent_password', env['agent_password'])
        kwargs.setdefault('nickname', nickname_fun())
        kwargs.setdefault('valid_code', '')
        agent_account = kwargs.get('agent_account')
        agent_password = kwargs.get('agent_password')
        member_account = kwargs.get('member_account')
        loading_first = self.driver.page_source
        identity = kwargs.get('identity')
        valid_code=kwargs.get('valid_code')
        if re.compile('<div class=".*?z-mask">',re.S).findall(loading_first) == []:
            self.memberSelect(fun_text='會員中心')
        self.driver.implicitly_wait(10)
        if identity=='agent':
            get_element = self.driver.find_element(By.XPATH, '//div[contains(@class,"drawer__view")]/div[1]/div[1]')
            [get_element.click() for _ in range(20)]
            self.driver.find_element(By.XPATH, '//div[contains(@class,"other__type__option")]').click()
            self.driver.find_element(By.XPATH, '//input[@type="account"]').send_keys(agent_account)
            self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(agent_password)
            self.driver.find_element(By.XPATH, '//button[text()="登入"]').click()
            if self.driver.find_elements(By.XPATH,'//p[text()="請洽客服人員。"]') !=[]:
                return False # 先中止後續的動作
        else:
            if re.compile('\+886+[0-9]{9}|[0-9]{10}', re.S).findall(member_account) != []:
                acc_type={'text':'手機','type':'phone','input_path':'//input[@class="vti__input"]'}
            else:
                acc_type = {'text': '信箱', 'type': 'email','input_path': '//input[contains(@class,"validate__email__input")]'}
            self.driver.implicitly_wait(10)
            if identity=='guest':
                try:
                    self.driver.find_element(By.XPATH,'//div[contains(@class,"main__type__option")]/span[text()="訪客"]').click()
                    self.driver.find_element(By.XPATH,'//button[text()="開始遊戲"]').click()

                    return True
                except:
                    self.memberSelect(fun_text='訪客資料')
                    self.driver.find_element(By.XPATH,f'//div[contains(@class,"edit__button") and text()="{acc_type["text"]}驗證"]').click()
            else:
                self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH,f'//div[contains(@class,"main__type__option")]/span[text()="{acc_type["text"]}"]'))
            self.driver.find_element(By.XPATH, acc_type['input_path']).send_keys(member_account)
            self.driver.find_element(By.XPATH,'//button[contains(@class,"validate__send__OTP")]').click()
            # if env['env'] == 'prod':
            backend_api = ma_api()
            time.sleep(10)
            if backend_api.token == None:
                return 'backendLoginError'
            if acc_type['type']=='email':
                # if env['env'] == 'prod':
                res = backend_api.apiGetData(method='get',api_url=BackAPI.infos_emailVerifications.value)
                if res['Data']==[]:
                    pass
                else:
                    email_code=list(filter(lambda x:x.get('Email')==member_account,res['Data']))
                    valid_code=email_code[0]['Code']
            else:
                # if env['env'] == 'prod':
                res = backend_api.apiGetData(method='get',api_url=BackAPI.infos_smsVerifications.value)
                if res['Data']==[]:
                    pass
                else:
                    phone_code=list(filter(lambda x:x.get('Phone')==member_account,res['Data']))
                    valid_code=phone_code[0]['Code']
            self.driver.find_element(By.XPATH,'//input[contains(@class,"validate__input__box")]').send_keys(valid_code)
            self.driver.find_element(By.XPATH,'//button[contains(@class,"validate__handle") and text()="下一步"]').click()
            time.sleep(10)
            self.getToken()
        # count = 0
        # self.closeDaily()
        # if identity=='agent' or check_click==False:
        #     time.sleep(10)
        #     return True
        # self.editNickName(is_register=True,name=nickname_fun())
        # time.sleep(2)
        # button_text = re.compile('<button class="bg-purpleBtn.*?">(.*?)</button>',re.S).findall(self.driver.page_source)
        # self.driver.find_element(By.XPATH, f'//button[contains(@class,"bg-purpleBtn") and text()="{button_text.pop()}"]').click()
    
    def getToken(self):
        self.closeDaily(refresh=True)
        self.token, self.refresh, self.mini = eval(self.driver.execute_script('return localStorage.getItem("userToken")'))
        return self.token

    # def redisCommon(self,**kwargs):
    #     identity=kwargs.get('identity')
    #     method = kwargs.get('method')
    #     if method == 'get':
    #         token = '\"' + r.get(f'{identity}Token') + '\"'
    #         refresh = '\"' + r.get(f'{identity}Refresh') + '\"'
    #         js = f"""localStorage.setItem("userToken",\'[{token},{refresh}]\')"""
    #         self.token = r.get(f'{identity}Token')
    #         self.driver.execute_script(js)
    #     else:
    #         r.set(f'{identity}Token', self.token)
    #         r.set(f'{identity}Refresh', self.refresh)
    #         r.set(f'{identity}Mining', self.mini)  # 新增礦寵

    def api_parser(self,**kwargs):#第一版本
        api_list = kwargs.get('api_list')
        
        # print(api_list)
        for i in api_list:
            # try:
                if i['method']=="Network.responseReceived" and i['params']['type']=='Image':
                    if i['params']['response']['staus'] != 200:
                        url=i['params']['response']['url']
                        progressNotify(message=f'安安機器人發現這個地方掉圖在幫忙看個{url}')
            # except:
            #     pass
        # res=list(map(lambda x:self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': x['params']['requestId']}),api_list))
        # with open('body.json','w',encoding='utf-8')as f:
        #     f.write(str(res))
        #     f.close()
        
    # def cleanRedis(self):
    #     """清redis"""
    #     r.flushdb()
    
    def closeDaily(self, **kwargs):
        """關閉每日彈窗 or 活動彈窗"""
        refresh = kwargs.get('refresh')
        if refresh == True:
            self.driver.execute_script("location.reload(true);")
            return None
        try:
            self.driver.find_element(By.XPATH,'//div[contains(@class,"signin__button__item") and text()="簽到"]').click()
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,'//div[contains(@class,"signin__button__item") and text()="已領取"]'))
        except:
            pass
        if self.driver.find_elements(By.XPATH,'//div[contains(@class,"event__mask")]') != []:
            ActionChains(self.driver).click(self.driver.find_element(By.XPATH, '//div[contains(@class,"event__view")]')).perform()
            ActionChains(self.driver).click(self.driver.find_element(By.XPATH, '//button[contains(@class,"seven__button")]')).perform()
        pass

    def gameList(self, type=None):
        """遊戲列表"""
        # self.driver.find_element(By.XPATH, '//ul[contains(@class,aside__list)]/li[2]').click()
        self.asideBarSelect(fun_text='遊戲')
        # self.driver.implicitly_wait(10)
        if type == 'slot':
            self.driver.find_element(By.XPATH, '//div[text()="拉霸"]').click()
        if type == 'battle':
            self.driver.find_element(By.XPATH, '//div[text()="對戰"]').click()
        if type == 'chess':
            self.driver.find_element(By.XPATH, '//div[text()="棋牌"]').click()
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH,'//div[contains(@class,"game__list__wrap")]/div[contains(@class,"game__list")]/div')

    def gameDetail(self, i):
        """遊戲詳細頁"""
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//div[contains(@class,"game__list__wrap")]/div/div[{index}]'.format(index=i)).click()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
                                                                                     '//div[contains(@class,"game-detail__play") and text()="立即遊玩"]'))
        coin_list = self.driver.find_element(By.XPATH, '//div[contains(@class,"game-pop__coin__list")]/div')
        return coin_list
    
    def choiceCoin(self, **kwargs):
        """送禮選擇硬幣"""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text()="送禮"]')))
        self.driver.find_element(By.XPATH, '//div[text()="送禮"]').click()
        self.driver.find_element(By.XPATH, '//input[contains(@class,"verify__input")]').send_keys('123456')
        # count = 0 # 迴圈計數器
        while self.driver.find_elements(By.XPATH, '//button[contains(@class,"validate__button") and text()="下一步"]') != []:
            try:
                self.driver.find_element(By.XPATH, '//button[contains(@class,"validate__button") and text()="下一步"]').click()
            except:
                pass
        if kwargs.get('coin') == 'sliver':
            try:
                self.driver.find_element(By.XPATH, '//div[contains(@class,"pick-coin__text") and text()="銀幣"]').click()
            except:
                self.driver.save_screenshot(filename=f'test_reports/choiceCoin{str(uuid.uuid4())}.png')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//button[contains(@class,"bg-purpleBtn")]').click()

    def sendPresent(self):
        """送禮"""
        # try:
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"packing__submit") and text()="完成"]')))
        self.driver.find_element(By.XPATH, '//button[contains(@class,"packing__submit") and text()="完成"]').click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"gift-success__button")]')))
        self.driver.find_element(By.XPATH, '//div[contains(@class,"gift-success__button")]').click()
        # except:
        #     self.driver.find_element(By.XPATH, '//div[contains(@class,"gift__close")]').click()
        #
    
    def recordList(self, **kwargs):
        """訂單選擇"""
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,f"//div[@class='swiper-wrapper']/div/span[text()=\"{kwargs.get('text')}\"]"))
    
    def memberSendRecord(self):
        """兌換贈禮"""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"menu__member")]')))
        self.memberSelect(fun_text='訂單')
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"record__container")]')))
        self.recordList(text='贈禮記錄')
        self.driver.implicitly_wait(10)
        while True:
            i = random.choice(range(len(self.driver.find_elements(By.XPATH, '//tbody/tr'))))
            if self.driver.find_element(By.XPATH, f'//tbody/tr[{i}]/td[4]/div/div/div[2]').text != '已完成':
                break
        if self.driver.find_element(By.XPATH, f'//tbody/tr[{i}]/td[4]/div/div/div[2]').text == '保管中':
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(By.XPATH, f'//tbody/tr[{i}]/td[3]/div/div'))
            self.driver.find_element(By.XPATH, '//div[text()="保管序號並查看"]').click()
            time.sleep(1)
        self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH, f'//tbody/tr[{i}]/td[3]/div/div'))
        present_code = re.sub('禮包序號', "", self.driver.find_element(By.XPATH, '//div[contains(@class,"context")]').text)
        order_no = self.driver.find_element(By.XPATH, f'//tbody/tr[{i}]/td[1]/div/div/div[2]').text
        # print(present_code, order_no)
        return present_code, order_no
    
    def orderNo(self, **kwargs):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//ul[contains(@class,"aside__list")]')))
        self.asideBarSelect(fun_text='序號')
        # while True:
        #     try:
        self.driver.find_element(By.XPATH, '//input[contains(@class,"serial__input")]').send_keys(kwargs.get('present_code'))
        self.driver.find_element(By.XPATH, '//button[contains(@class,"serial__button")]').click()
        #     break
        # except:
        #     self.asideBarSelect(fun_text='序號')
        self.driver.implicitly_wait(10)
        """多加參數判斷後續彈窗行為,禮物兌換 or 註冊掛線, 沒有彈窗,Default 禮物兌換確定"""
        if kwargs.get('mode') == 'presentChange':
            self.driver.find_element(By.XPATH, '//a[@href="/center/record?type=receive"]').click()
        elif kwargs.get('mode') == 'PromoteCode':
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH, '//button[text()="開始遊戲"]').click()
        elif kwargs.get('mode') == 'noAlter':  # 沒有彈窗
            # time.sleep(0.3)
            pass
        else:
            self.driver.find_element(By.XPATH, '//div[contains(@class,"serial__btn") and text()="確定"]').click()
    
    def depositType(self,**kwargs):
        deposit_type=kwargs.get('type')
        self.driver.find_element(By.XPATH,f'//div[@class="swiper-wrapper"]/div[contains(@class,"swiper-slide")]/div[text()="{deposit_type}"]').click()
        res_packageItem = self.driver.find_elements(By.XPATH,'//div[contains(@class,"deposit__package__list")]/div[contains(@class,"package__item")]')
        return res_packageItem
    

    
    def depositPayWay(self,**kwargs):
        package = kwargs.get('package')
        pay_way = kwargs.get('pay_way')
        info = kwargs.get('info')
        count = kwargs.get('count')
        package.click()
        if count != None:
            self.driver.find_element(By.XPATH, '//input[contains(@class,"deposit-total__input")]').clear()
            self.driver.find_element(By.XPATH, '//input[contains(@class,"deposit-total__input")]').send_keys(count)
            self.driver.find_element(By.XPATH, '//div[contains(@class,"deposit-total__less")]').click()
            self.driver.find_element(By.XPATH, '//div[contains(@class,"deposit-total__add")]').click()
            count = self.driver.find_element(By.XPATH, '//input[contains(@class,"deposit-total__input")]').get_attribute('value')
        self.driver.find_element(By.XPATH,f'//div[contains(@class,"deposit__list")]/div[contains(@class,"deposit__item")]/div[@class="label" and text()="{pay_way}"]').click()
        if pay_way == '載具類型':
            self.driver.find_element(By.XPATH,'//div[text()="E-mail"]/following-sibling::input').send_keys(info['email'])
            if info.get('nature')!=None:
                self.driver.find_element(By.XPATH, '//div[text()="自然人憑證"]/following-sibling::div/input').send_keys(info['nature'])
            else:
                self.driver.find_element(By.XPATH,'//div[text()="手機條碼"]/following-sibling::div/input').send_keys(info['cellphoneCode'])
        elif pay_way == '統一編號':
            self.driver.find_element(By.XPATH, '//div[text()="抬頭"]/following-sibling::input').send_keys(info['companyName'])
            self.driver.find_element(By.XPATH, '//div[text()="統一編號"]/following-sibling::input').send_keys(info['companyCode'])
        else: # 捐贈
            if info.get('donateCode')!=None:
                self.driver.find_element(By.XPATH, '//div[contains(@class,"deposit__item")][2]/div/following-sibling::input').send_keys(info['donateCode'])
        self.driver.find_element(By.XPATH,'//div[text()="購買"]').click()
        return count
    
    def depositFinishWay(self,**kwargs):
        way = kwargs.get('way')
        if way == 'record':
            self.driver.find_element(By.XPATH,'//button[text()="查看訂單記錄"]').click()
        elif way=='deposit':
            self.driver.find_element(By.XPATH,'//button[text()="退回商城"]').click()
        elif way=='mini':
            self.driver.find_element(By.XPATH, '//button[text()="開啟神遊礦寵"]').click()
        else:
            self.driver.get(env['font_url'])
    
    
    def editNickName(self, **kwargs):
        name=kwargs.get('name')
        is_register=kwargs.get('is_register')
        if is_register==True:
            self.driver.find_element(By.XPATH, '//input[@placeholder="告訴我你的名字吧！"]').send_keys(name)
            self.driver.find_element(By.XPATH,'//button[contains(@class,"bg-purpleBtn") and text()="下一步"]').click()
            return True
        self.driver.find_element(By.XPATH, '//div[contains(@class,"edit__button") and text()="修改暱稱"]').click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="請輸入2~16個字元"]')))
        self.driver.find_element(By.XPATH, '//input[@placeholder="請輸入2~16個字元"]').clear()
        self.driver.find_element(By.XPATH, '//input[@placeholder="請輸入2~16個字元"]').send_keys(name)
        self.driver.find_element(By.XPATH, '//button[text()="送出修改"]').click()
    
    def asideBar(self):
        res = self.driver.find_elements(By.XPATH, '//div[contains(@class,"aside__container")]/ul/li')
        res_text = [i.find_element(By.XPATH, './div/span').text for i in res]
        return res_text, res
    
    def twitter(self):
        self.driver.find_element(By.XPATH, '//div[@class="swiper-wrapper"]/div[3]/span[text()="GPG動態"]').click()
        self.driver.implicitly_wait(20)
        res = self.driver.find_element(By.XPATH, '//div[@class="twitter__container"]/div[contains(@class,"twitter-timeline")]/iframe')
        return res
    
    def gameRank(self):
        self.driver.find_element(By.XPATH, '//div[@class="swiper-wrapper"]/div[2]/span[text()="排行榜"]').click()
        self.driver.implicitly_wait(10)
    
    def memberSelect(self, fun_text):
        """會員選單"""
        self.driver.implicitly_wait(1)
        if self.driver.find_elements(By.XPATH, '//div[contains(@class,"menu__member")]/div'):
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(By.XPATH, '//div[contains(@class,"menu__member")]/div'))
        else:
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(By.XPATH, '//div[contains(@class,"menu__member")]/img'))
        self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH, '//span[text()="%s"]' % fun_text))
        self.driver.implicitly_wait(10)
        # try:
        #     self.driver.execute_script("arguments[0].click();",self.driver.find_element(By.XPATH, '//div[contains(@class,"menu__member")]/div'))
        # except:
        #     self.driver.implicitly_wait(4)
    
    def chatRoom(self):
        """聊天室路徑"""
        self.driver.find_element(By.XPATH, '//div[contains(@class,"menu__message")]/img').click()
    
    # def friendList(self):
    #     """聊天室好友列表"""
    #     self.driver.find_element(By.XPATH, '//div[contains(@class,"menu__list")]/div[text()="好友"]').click()
    
    def Addfriend(self):
        """聊天室加入好友"""
        self.driver.find_element(By.XPATH, '//div[contains(@class,"swiper-slide")]/span[text()="加入好友"]').click()
    
    def transfer(self):
        """轉帳錢包路徑"""
        count = 0
        while True:
            try:
                self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,'//div[contains(@class,"menu__balance__icon-bg")]'))
                self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"balance__container")]')))
                self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.XPATH,'//div[contains(@class,"balance__transfer__icon")]'))
                break
            except:
                count+=1
                if count>3:
                    break
                pass
    
    def transferPacket(self, start=None, to=None):
        """轉帳錢包"""
        # self.driver.find_element(By.XPATH,'//div[@class="wallet-action__container"]/div[1]').click()
        if start != None:
            self.driver.find_element(By.XPATH,
                                     '//div[contains(@class,"wallet-action__tips")]/div[contains(@class,"select__wrap")]/div[contains(@class,"switch__container")]/label/i').click()
            self.driver.find_element(By.XPATH, '//div[contains(@class,"switch__item") and text()="%s"]' % start).click()
            time.sleep(1)
        if to != None:
            self.driver.find_element(By.XPATH,
                                     '//img[contains(@class,"wallet-action__move")]/following-sibling::div[contains(@class,"select__wrap")]/div[contains(@class,"switch__container")]/label[contains(@class,"switch__display")]/i').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//div[contains(@class,"switch__item") and text()="%s"]' % to).click()
        else:
            pass
        self.driver.find_element(By.XPATH, '//input[@inputmode="numeric"]').send_keys('1')
        self.driver.find_element(By.XPATH, '//div[text()="確認轉帳"]').click()
        self.driver.find_element(By.XPATH, '//div[contains(@class,"wallet__close")]/div').click()
    
    def service(self):
        """客服"""
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//span[text()="客服"]').click()
    
    def article(self):
        for i in ['//span[text()="合作夥伴"]', '//span[text()="使用條款"]', '//span[text()="關於GPG"]']:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, i)))
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, i))
            self.driver.find_element(By.XPATH, '//img[contains(@class,"article__close")]').click()
    
    def transferRecord(self):
        """轉移紀錄"""
    
    def mining(self):
        """礦機icon"""
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//div[contains(@class,"shortcut__wrap")]/div[contains(@class,"shortcut__container")]').click()
        # time.sleep(10)
    
    def exit(self):
        """砍進程"""
        self.driver.quit()
        os.system('taskkill /im chromedriver.exe /F')  # 砍進程
        os.system('taskkill /im chrome.exe /F')
    
    def playGame(self, **kwargs):
        """玩遊戲"""
        self.loginV2(phone=kwargs.get('account'), passredis=True)  # 第三個是礦寵token
        self.closeDaily()
        self.asideBarSelect(fun_text='遊戲')
        return self.gameList('slot')
    
    def miniver2(self, **kwargs):
        self.loginV2(identity='agent')  # 第三個是礦寵token
        self.closeDaily()
        self.driver.find_element(By.XPATH,'//div[contains(@class,"shortcut__wrap")]').click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    def signIn(self, **kwargs):
        """簽到"""
        self.memberSelect(fun_text="簽到")
        self.driver.find_element(By.XPATH,
                                 '//div[contains(@class,"menu__item")]/span[text()="%s"]' % kwargs.get('func')).click()
        fun_button = self.driver.find_elements(By.XPATH,
                                               '//div[contains(@class,"signin__button__constainer")]/div')  # 包含關閉和簽到
        self.driver.implicitly_wait(10)
        return fun_button
    
    def getAlertMessage(self):
        """取得彈跳錯誤訊息"""
        count = 0
        while True:
            res = re.compile('<span class="new-content__text">(.*?)</span>', re.S).findall(self.driver.page_source)
            if len(res) == 1:
                break
            count += 1
            if count >= 3:
                break
        return res.pop()
    
    def logout(self,**kwargs):
        kwargs.setdefault('set_option', '登出')
        self.memberSelect(fun_text='設定')
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, f'//div[text()="{kwargs.get("set_option")}"]'))
        time.sleep(1)
    
    def version(self):
        ver = self.driver.find_element(By.XPATH, '//div[contains(@class,"footer__copyright")]/span').text
        return ver


class FontAPI(Enum):  # 前台ＡＰＩ
    font_api = env['font_api']
    token_locale=f'{font_api}Token/Locale'
    activity_normal_signInMonthList = f'{font_api}Activity/Normal/SignInMonthList'
    member_memberInfo = f'{font_api}Member/MemberInfo'
    chat_chatRoomList = f'{font_api}Chat/ChatRoomList'
    friend_friendList = f'{font_api}Friend/FriendList'
    friend_recommendList = f'{font_api}Friend/RecommendList'
    member_memberWallet = f'{font_api}Member/MemberWallet'
    wallet_search = f'{font_api}Wallet/Search'
    game_homeBanner = f'{font_api}Game/HomeBanner'
    game_homeHotGame = f'{font_api}Game/HomeHotGame'
    game_gameList = f'{font_api}Game/GameList'
    game_leaderboard = f'{font_api}Game/Leaderboard'
    activity_noviceSignIn7thList = f'{font_api}Activity/NoviceSignIn7thList'
    activity_noviceSignIn7th = f'{font_api}Activity/NoviceSignIn7th'
    electronicMall_packageList = f'{font_api}ElectronicMall/PackageList'
    member_phoneAvailability = f'{font_api}Member/PhoneAvailability'
    transaction_sendTransactionPasswordVerify = f'{font_api}Transaction/SendTransactionPasswordVerify'
    mining_getPetInfo=f'{font_api}Mining/GetPetInfo'
    member_nickName = f'{font_api}Member/AddNickname'
    member_OrderDel = f'{font_api}Member/OrderDel'
    game_gameLink = f'{font_api}Game/GameLink'
    member_updateMemberStatus = f'{font_api}Member/UpdateMemberStatus'
    wallet_transferRecord = f'{font_api}Wallet/TransferRecord'
    wallet_transfer = f'{font_api}Wallet/Transfer'
    transaction_checkTransactionPasswordVerify = f'{font_api}Transaction/CheckTransactionPasswordVerify'
    transaction_verifyPassword = f'{font_api}Transaction/VerifyPassword'
    transaction_estimateFee = f'{font_api}Transaction/EstimateFee'
    transaction_submitRewardPoint = f'{font_api}Transaction/SubmitRewardPoint'
    transaction_discloseSerialNo = f'{font_api}Transaction/discloseSerialNo'
    chat_initUnReadCount = f'{font_api}Chat/InitUnReadCount'
    chat_sendChatText = f'{font_api}Chat/SendChatText'
    electronicMall_buyPackage = f'{font_api}ElectronicMall/BuyPackage'
    member_updateAvatarFrame = f'{font_api}Member/UpdateAvatarFrame'
    member_certifiedPhone = f'{font_api}Member/CertifiedPhone'
    member_acceptPromotion = f'{font_api}Member/AcceptPromotion'
    friend_searchFriend = f'{font_api}Friend/SearchFriend'
    friend_friendAdd = f'{font_api}Friend/FriendAdd'
    chat_chatRoomText = f'{font_api}Chat/ChatRoomText'
    chat_chatGroup = f'{font_api}Chat/ChatGroup'
    transaction_setTransactionPassword = f'{font_api}Transaction/SetTransactionPassword'
    transaction_transactionRecord = f'{font_api}Transaction/TransactionRecord'
    game_recommendGame = f'{font_api}Game/RecommendGame'
    game_gameInfo = f'{font_api}Game/GameInfo'
    member_avatarFrameRepository = f'{font_api}Member/AvatarFrameRepository'
    member_avatarRepository = f'{font_api}Member/AvatarRepository'
    member_orderList = f'{font_api}Member/OrderList'
    wallet_transferBack = f'{font_api}wallet/TransferBack'
    activity_redDot = f'{font_api}Activity/RedDot'
    franchisee_createFranchisee = f'{font_api}Franchisee/CreateFranchisee'
    game_rankingByPoints=f'{font_api}Game/RankingByPoints'
    member_contributionRanking_BetCache=f'{font_api}Member/ContributionRanking/BetCache'
    member_contributionRanking_TotalWalletPoint=f'{font_api}Member/ContributionRanking/TotalWalletPoint'
    

class ma_api:
    def __init__(self, **kwargs):
        kwargs.setdefault('account',env['back_account'])
        kwargs.setdefault('password',env['back_password'])
        kwargs.setdefault('url',BackAPI.token_signIn.value)
        account = kwargs.get('account')
        password = kwargs.get('password')
        # print(account,password)
        url = kwargs.get('url')
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }
        data = {'Account': account, 'Password': password}
        response = requests.post(url, json=data, headers=self.headers).json()
        self.token = response['access_token']
    
    def apiGetData(self, **kwargs):
        """
        :param kwargs:
        method:request method
        api_url:api_url
        data:post json
        payload: get url payload
        :return:
        """
        method = kwargs.get('method')
        apiUrl = kwargs.get('api_url')
        data = kwargs.get('data')
        payload = kwargs.get('payload')
        self.headers['authorization'] = 'Bearer %s' % self.token
        logging.info('testcase parameter:' + str(kwargs))
        try:
            if method == 'get':
                res = requests.get(apiUrl, data=data, params=payload, headers=self.headers)
                print(res.status_code)
                logging.info('response statuscode:' + str(res.status_code))
                logging.info('response text:' + res.text)
            else:
                # print(apiUrl+'\t'+str(data)+'\t'+str(self.headers))
                res = requests.post(apiUrl, json=data, headers=self.headers)
                logging.info('response statuscode:' + str(res.status_code))
                logging.info('response text:' + res.text)
            print(res.json())
            return res.json()
        except:
            # print(apiUrl + '\t' + data + '\t' + self.headers)
            if method == 'get':
                res = requests.get(apiUrl, data=data, params=payload, headers=self.headers)
                logging.info('response statuscode:' + str(res.status_code))
                logging.info('response text:' + res.text)
            else:
                res = requests.post(apiUrl, data=data, params=payload, headers=self.headers)
                logging.info('response statuscode', str(res.status_code))
                logging.info('response text:', res.text)
            return res.text
    
    def uploadFile(self, **kwargs):
        logging.info('testcase parameter:' + str(kwargs))
        self.headers['authorization'] = 'Bearer %s' % self.token
        api_url = kwargs.get('api_url')
        res = requests.post(url=api_url, data=kwargs.get('data'), files=kwargs.get('file'), headers=self.headers)
        logging.info('response statuscode:' + str(res.status_code))
        logging.info('response text:' + res.text)
        try:
            return res.json()
        except:
            return res.text


class ma_driver_eng:
    def __init__(self):  # 共模
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')
        options.add_argument('--no-sandbox')
        caps = {
            'browserName': 'chrome',
            'version': '',
            'platform': 'ANY',
            'goog:loggingPrefs': {'performance': 'ALL'},  # 记录性能日志
            'goog:chromeOptions': {'extensions': [], 'args': ['--headless']}  # 无界面模式
        }
        options.add_experimental_option('prefs', {'intl.accept_languages': 'zh_TW'})  # 強制改瀏覽器的語系
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-urlfetcher-cert-requests')
        self.driver = webdriver.Chrome(options=options, desired_capabilities=caps)
        self.driver.get(env['back_url'])
        # print(self.driver.execute_script('return JSON.stringify(window.performance.timing)'))
        # print(self.driver.execute_script('return JSON.stringify(window.performance.getEntries())'))
        self.wait = WebDriverWait(self.driver, 10, 0.5)
    
    def login(self):
        """後台登入"""
        self.driver.find_element(By.XPATH, '//input[@placeholder="請輸入帳號"]').send_keys('GenesisPerfectGame')
        self.driver.find_element(By.XPATH, '//input[@placeholder="請輸入密碼"]').send_keys('123456')
        self.driver.find_element(By.XPATH, '//span[text()="送出"]').click()
        self.driver.implicitly_wait(10)
    
    def side_select(self, **kwargs):
        """側邊選單"""
        self.driver.find_element(By.XPATH,
                                 f'//div[@class="el-submenu__title"]/span[text()="{kwargs.get("text")}"]').click()
    
    def func_select(self, **kwargs):
        """功能列表"""
        self.driver.find_element(By.XPATH, f'//ul[@role="menu"]/li[text()="{kwargs.get("text")}"]').click()
    
    def fuzzy_search(self, **kwargs):
        """模糊搜尋"""
        status = self.driver.find_element(By.XPATH,
                                          f'//label[text()="{kwargs.get("text")}"]/following-sibling::div/label')
        if 'el-checkbox is-checked' == status.get_attribute('class'):
            if kwargs.get('setting') == 'cancel':
                status.click()
        else:
            if kwargs.get('setting') == 'submit':
                status.click()
    
    def mining_report(self):
        """礦機報表"""
    
    def scroll_select(self, **kwargs):
        """下拉選單"""
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 f'//label[text()="{kwargs.get("label_text")}"]/following-sibling::div').click()
        time.sleep(2)
        res = self.driver.find_elements(By.XPATH, '//ul[contains(@class,"el-scrollbar__view")]/li')
        list(filter(lambda x: x.find_element(By.XPATH, './span').text == kwargs.get('text'), res)).pop().click()
    
    def search_button(self):
        """搜尋按鈕點擊"""
        self.driver.find_element(By.XPATH, '//button[contains(@class,"el-button")]/span[text()="搜尋"]').click()
        time.sleep(3)
    
    def input_text(self, **kwargs):
        """輸入資料"""
        self.driver.find_element(By.XPATH,
                                 f'//label[text()="{kwargs.get("label_text")}"]/following-sibling::div/div/input').send_keys(
            kwargs.get('text'))
    
    def clean(self):
        """清除條件"""
        self.driver.find_element(By.XPATH, '//span[text()="清除條件"]').click()
    
    def input_date(self, *args, **kwargs):
        """輸入日期"""
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 f'//label[text()="{kwargs.get("label_text")}"]/following-sibling::div').click()
        for i in args:
            self.driver.find_element(By.XPATH,
                                     f'//div[@class="el-picker-panel__body"]/div/span[{args.index(i) + 1}]/div/input').clear()
            self.driver.find_element(By.XPATH,
                                     f'//div[@class="el-picker-panel__body"]/div/span[{args.index(i) + 1}]/div/input').send_keys(
                i)
        self.driver.find_element(By.XPATH,
                                 '//div[@class="el-picker-panel__footer"]/button[2]/span[text()="OK"]').click()
    
    def getAlertMessage(self):
        """取得彈跳錯誤訊息"""
        count = 0
        while True:
            res = re.compile('<p class="el-message__content">(.*?)</p>', re.S).findall(self.driver.page_source)
            if len(res) == 1:
                break
            count += 1
            if count >= 3:
                break
        return res.pop()
    
    def view_source(self, **kwargs):  # 查看code
        if kwargs.get('url'):
            self.driver.get(kwargs.get('url'))
            with open('{filename}.html'.format(filename=kwargs.get('filename')), 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
                f.close()
        else:
            with open('{filename}.html'.format(filename=kwargs.get('filename')), 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
                f.close()


class BackAPI(Enum):  # 後台ＡＰＩ
    Back_api = env['back_api']
    home_AdvertisersData = f'{Back_api}Home/AdvertisersData'
    token_menu = f'{Back_api}Token/Menu'
    token_signIn=f'{Back_api}Token/SignIn'
    """廣告加盟商管理"""
    promote_newCode = f'{Back_api}Promote/NewCode'
    promote_add = f'{Back_api}Promote/Add'
    promote_delete = f'{Back_api}Promote/Delete'
    """會員管理"""
    member_advertisersList = f'{Back_api}Member/AdvertisersList'
    member_advertisersInfo = f'{Back_api}Member/AdvertisersInfo'
    member_advertisersPath = f'{Back_api}Member/AdvertisersPath'
    member_inviteFranchisee = f'{Back_api}Member/InviteFranchisee'
    member_memberList = f'{Back_api}Member/MemberList'
    infos_gameAccounts = f'{Back_api}Infos/GameAccounts'
    member_customerServiceChangeRecord = f'{Back_api}Member/CustomerServiceChangeRecord'
    member_customerServiceChange = f'{Back_api}Member/CustomerServiceChange'
    infos_memberInfo = f'{Back_api}Infos/MemberInfo'
    member_disable = f'{Back_api}Member/Disable'
    infos_smsVerifications = f'{Back_api}Infos/SmsVerifications'
    infos_emailVerifications = f'{Back_api}Infos/EmailVerifications'
    member_roleChangeDetail=f'{Back_api}Member/Roles/Change/Detail'
    member_roleChange=f'{Back_api}Member/Roles/Change'
    """遊戲管理"""
    game_gameList = f'{Back_api}Game/GameList'
    game_provider_vaSlot_status = f'{Back_api}Game/Provider/1/Um/Status'
    game_provider_vaBattle_status = f'{Back_api}Game/Provider/3/Um/Status'
    game_provider_ifun_status = f'{Back_api}Game/Provider/4/Um/Status'
    game_editGame = f'{Back_api}Game/EditGame'
    game_um_status = f'{Back_api}Game/Um/Status'  # 單一遊戲進維護
    game_Provider_Um_Status = f'{Back_api}Game/Provider/Um/Status'  # 全遊戲維護
    """報表管理"""
    dataReport_walletChangeReport = f'{Back_api}DataReport/WalletChangeReport'
    dataReport_memberDepositReport = f'{Back_api}DataReport/MemberDepositReport'
    dataReport_depositReport = f'{Back_api}DataReport/DepositReport'
    dataReport_transactionRecord = f'{Back_api}DataReport/TransactionRecord'
    dataReport_miningReceipts = f'{Back_api}DataReport/MiningReceipts'
    dataReport_adLvResetGet = f'{Back_api}DataReport/AdLvResetGet'
    dataReport_adLvReport = f'{Back_api}DataReport/AdLvReport'
    dataReport_adLvResetAdd = f'{Back_api}DataReport/AdLvResetAdd'
    dataReport_promoteReport = f'{Back_api}DataReport/PromoteReport'
    dataReport_adLvResetMod = f'{Back_api}DataReport/AdLvResetMod'
    """贈品管理"""
    voucher_itemGet = f'{Back_api}Voucher/ItemGet'
    voucher_itemAdd = f'{Back_api}Voucher/ItemAdd'
    voucher_itemDel = f'{Back_api}Voucher/ItemDel'
    voucher_itemEdit = f'{Back_api}Voucher/ItemEdit'
    voucher_itemTypeGet = f'{Back_api}Voucher/ItemTypeGet'
    voucher_itemTypeAdd = f'{Back_api}Voucher/ItemTypeAdd'
    voucher_itemTypeEdit = f'{Back_api}Voucher/ItemTypeEdit'
    voucher_itemPhotoDel = f'{Back_api}Voucher/ItemPhotoDel'
    """禮包產品組合"""
    voucher_packageItemGet = f'{Back_api}Voucher/PackageItemGet'
    voucher_packageGet = f'{Back_api}Voucher/PackageGet'
    voucher_packageAdd = f'{Back_api}Voucher/PackageAdd'
    voucher_packageDel = f'{Back_api}Voucher/PackageDel'
    voucher_packageEdit = f'{Back_api}Voucher/PackageEdit'
    voucher_packagePhotoDel = f'{Back_api}Voucher/PackagePhotoDel'
    """兌換券管理"""
    voucher_voucherGet = f'{Back_api}Voucher/VoucherGet'
    voucher_voucherAdd = f'{Back_api}Voucher/VoucherAdd'
    voucher_voucherEdit = f'{Back_api}Voucher/VoucherEdit'
    voucher_voucherDel = f'{Back_api}Voucher/VoucherDel'
    voucher_activityGet = f'{Back_api}Voucher/ActivityGet'
    voucher_activityAdd = f'{Back_api}Voucher/ActivityAdd'
    voucher_activityEdit = f'{Back_api}Voucher/ActivityEdit'
    voucher_activityDel = f'{Back_api}Voucher/ActivityDel'
    voucher_packageExchangeSend = f'{Back_api}Voucher/PackageExchangeSend'
    voucher_packageExchangeGet=f'{Back_api}Voucher/PackageExchangeGet'
    """發送清單"""
    voucher_voucherSendGet = f'{Back_api}Voucher/VoucherSendGet'
    """領取清單"""
    voucher_voucherReceiveGet = f'{Back_api}Voucher/VoucherReceiveGet'
    """實體核銷券功能"""
    coupon_order_onSiteRedeemCheck=f"{Back_api}Coupon/Order/OnSiteRedeemCheck"
    coupon_onSiteOrderList=f'{Back_api}Coupon/OnSiteOrderList'
    coupon_order_storeMenu=f'{Back_api}Coupon/Order/StoreMenu'
    coupon_order_onSiteReport=f'{Back_api}Coupon/Order/OnSiteReport'

class PlayAPI_ids(Enum): # gpgoAuth建構
    play_api_ids=env['play_api_ids']
    connect_token=f'{play_api_ids}connect/token'
    token_adLogin=f'{play_api_ids}Token/AdLogin'

class PlayAPI(Enum): # gpg oAuth建構
    play_api=env['play_api']
    mining_pool_public=f'{play_api}Mining/pool/public'
    singleWallet_search=f'{play_api}SingleWallet/Search'
    mining_pool_blindbox=f'{play_api}mining/pool/blindbox'
    activity_drawlots=f'{play_api}Activity/Drawlots'
    chat_recommendFriends=f'{play_api}Chat/RecommendFriends'
    friend_friendAdd=f'{play_api}Friend/FriendAdd'
    chat_sendMessage=f'{play_api}Chat/SendMessage'
    coupon_addOrder=f'{play_api}Coupon/AddOrder'
    member_myInfo=f'{play_api}Member/MyInfo'
    member_nickname=f'{play_api}Member/Nickname'
    mining_pool_public_idv=f'{play_api}Mining/pool/public/idv'
    mining_pool_personal=f'{play_api}Mining/pool/personal'
    singleWallet_transfer=f'{play_api}SingleWallet/Transfer'
    transaction_exchange=f'{play_api}Transaction/Exchange'
    voucher_mkItem=f'{play_api}Voucher/MKItem'




