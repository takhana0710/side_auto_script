from testcase.gpg2_chromeset import TransferDict,gpg_api,driver_eng,FontAPI,env
import datetime
import time
import requests
driver = driver_eng()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  # 座標點擊
action = ActionChains(driver.driver)
def gameList():
    res = requests.get(FontAPI.game_gameList.value,params={'Locale': 'zh-TW'}).json()['Data']
    return list(filter(lambda x:x['GameName']=="勇敢吧！外星人！",res))
# def checkImageLog():
#     logs_row = driver.driver.get_log('performance')
#     logs = [json.loads(lr["message"])["message"] for lr in logs_row]
#     for i in logs:
#         if i['method']=="Network.responseReceived" and i['params']['type']=='Image':
#             if re.compile('https://img\.godplay\.app/',re.S).findall(i['params']['response']['url']) !=[] and i['params']['response']['status'] != 200:
#                 url=i['params']['response']['url']
#                 progressNotify(msg=f'安安機器人發現這個地方掉圖在幫忙看個{url}')

def progressNotify(msg):
    hook='https://hooks.slack.com/services/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' # gpg_game
    # hook = 'https://hooks.slack.com/services/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' # CEIS_QA
    requests.post(hook, json={"text":msg}, headers={'Content-Type': 'application/json'})


def play_game(member,game):
    res = driver.loginV2(member_account=member)
    if res == 'backendLoginError':
        progressNotify(msg='後臺登入失敗哦~~~')
    api = gpg_api(token=driver.token)
    for i in game:
        while True:
            res = api.apiGetData(method='get', api_url=FontAPI.wallet_search.value,payload={'CheckProviderMember': True, 'UpdateFromProvider': True, 'Locale': 'zh-TW'})
            if res['Status']['Code'] == '0':
                wallet_list = res['Data']
                coda = list(filter(lambda x: x.get('WalletPointTypeID') == TransferDict.VABattle_gold.value, wallet_list))
                if coda[0]["Balance"] < 5000:
                    api.apiGetData(method='post', api_url=FontAPI.wallet_transfer.value,data={'CheckProviderMember': True, 'FromWalletPointTypeID': 1, 'Point': 1000,'ToWalletPointTypeID': TransferDict.VABattle_gold.value})
                else:
                    break
            else:
                time.sleep(3)
        try:
            game_link = requests.get(url=FontAPI.game_gameLink.value,headers={"Authorization":"Bearer "+ driver.token},params={"Platform": "web","PointTypeID": 1,
            "GameID": i['GameID'],
            "GameProvider": i['Vendor']['GameProvider'],
            "GameProviderGameID": i['Vendor']['GameProviderGameID'],
            "ReturnUrl": f'https://godplay.app/game/detail/{i["GameID"]}',
            "Locale": "zh-TW"}).json()
        except:
            print(i['GameID'])
            continue
        driver.driver.execute_script("window.open('');")
        driver.driver.switch_to.window(driver.driver.window_handles[1])
        driver.driver.get(game_link["Url"])
        size = driver.driver.get_window_size()
        time.sleep(5)
        width = size['width'] / 2
        height = size['height'] * 0.53
        action.move_by_offset(width, height).click().perform()
        action.move_by_offset(-width, -height).click().perform()
        height = size['height'] * 0.45
        action.move_by_offset(width, height).click().perform()
        action.move_by_offset(-width, -height).click().perform()
        count = 0
        while True:
           driver.driver.find_element(By.XPATH, '//canvas[@id="GameCanvas"]').send_keys(Keys.SPACE)
           time.sleep(5)
           if count > 500:
               break
           count+=1
        driver.driver.close()
        driver.driver.switch_to.window(driver.driver.window_handles[0])
    driver.logout()
    time.sleep(5)

def apitest():
    api = gpg_api(token=driver.token)
    # driver.exit()
    res = api.apiGetData(method='get',api_url=FontAPI.wallet_search.value,payload={'Locale': 'zh-TW', 'CheckProviderMember': True, 'UpdateFromProvider': True})
    time.sleep(2)
    sliver = api.apiGetData(method='post',api_url=FontAPI.wallet_transferBack.value,data={"PointTypeID": 2})
    time.sleep(2)
    gold = api.apiGetData(method='post',api_url=FontAPI.wallet_transferBack.value,data={"PointTypeID": 1})
    time.sleep(2)
    try:
        if gold['Status']['Code'] != "0":
            progressNotify('gold' + str(gold))
        if sliver['Status']['Code'] != "0":
            progressNotify('sliver' + str(sliver))
    except:
        progressNotify('sliver' + sliver)
        progressNotify('gold' + gold)
        progressNotify('getWallet' + res)
    for i in [TransferDict.VASlot_gold.value, TransferDict.IFUN_gold.value, TransferDict.VABattle_gold.value]:
        res_transfer=api.apiGetData(method='post',api_url=FontAPI.wallet_transfer.value,data={'CheckProviderMember': True, 'FromWalletPointTypeID': 1, 'Point': 10000,'ToWalletPointTypeID': i})
        time.sleep(2)
        try:
            if res_transfer['Status']['Code'] != "0":
                progressNotify('res_transfer_gold' + str(res_transfer))
        except:
            progressNotify('res_transfer_gold' + res_transfer.text)
    try:
        sliver_transfer = api.apiGetData(method='post',api_url=FontAPI.wallet_transfer.value,data={'CheckProviderMember': True, 'FromWalletPointTypeID': 2, 'Point': 1000,'ToWalletPointTypeID': TransferDict.VASlot_silver.value})
    except:
        progressNotify('res_transfer_sliver' + sliver_transfer.text)
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    day = yesterday.strftime("%Y-%m-%d")
    try:
        res = api.apiGetData(method='get',api_url=FontAPI.game_rankingByPoints.value,payload={'Locale': 'zh-TW'})
        if  len(res['Data'][0]['GameList'])<10 or len(res['Data'][1]['GameList'])<10:
            progressNotify('遊戲排行數量不足10個')
    except:
        progressNotify('遊戲排行錯誤')
    try:
        res = api.apiGetData(method='get',api_url=FontAPI.member_contributionRanking_BetCache.value,payload={'StartDate': day+'T00:00:00+08:00','EndDate': day+'T23:59:59+08:00','Top': 10})
        if  len(res['Data'][1]['MemberList'])<10 or len(res['Data'][0]['MemberList'])<10:
            progressNotify('活躍度排行數量不足10個')
    except Exception as e:
        progressNotify(str(e))
        progressNotify('活躍度排行錯誤')
    try:
        res = api.apiGetData(method='get',api_url=FontAPI.member_contributionRanking_TotalWalletPoint.value,payload={'Top':10})
        if len(res['Data']['GoldResult'])<10 or len(res['Data']['SilverResult'])<10:
            progressNotify('玩家排行數量不足10個')
    except:
        progressNotify('玩家排行錯誤')
def login_validate():
    # progressNotify('安安我要開始努力工作惹')
    time.sleep(10) # 追加強制休息測試穩定度
    driver.loginV2(member_account='')
    apitest()
    driver.logout()
    pass
if __name__ == '__main__':
    try:
        # login_validate()
        get_game = gameList()
        for i in []:
            play_game(i,get_game)
    except Exception as e:
        progressNotify(str(e))
        progressNotify('RRRRRR我工作到出錯了請求的支援')
    progressNotify('我工作做完了')
