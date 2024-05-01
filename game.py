from testcase.gpg2_chromeset import driver_eng, FontAPI,TransferDict,gpg_api
import requests
from selenium.webdriver.common.action_chains import ActionChains  # 座標點擊
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from multiprocessing import Process, Pool
import os
import random
driver = driver_eng()
action = ActionChains(driver.driver)
token = ''
refresh = ''
mini = ''
def gameList():
    res = requests.get(FontAPI.game_gameList.value,params={'Locale': 'zh-TW'}).json()['Data']
    return list(filter(lambda x:x['GameName']=="\",res))

def play_game(member,game):
    token2 = '\"' + token + '\"'
    refresh2 = '\"' + refresh + '\"'
    mini2 = '\"' + mini + '\"'
    js = f"""localStorage.setItem("userToken",\'[{token2},{refresh2},{mini2}]\')"""
    driver.driver.execute_script(js)
    driver.closeDaily(refresh=True)
    time.sleep(10)
    # driver.loginV2(member_account=member)
    # print(driver.token)
    # print('*******************')
    # print(driver.refresh)
    # print('*******************')
    # print(driver.mini)
    api = gpg_api(token = token)
    for i in game:
        # while True:
            # res = api.apiGetData(method='get', api_url=FontAPI.wallet_search.value,payload={'CheckProviderMember': True, 'UpdateFromProvider': True, 'Locale': 'zh-TW'})
            # if res['Status']['Code'] == '0':
            #     wallet_list = res['Data']
            #     coda = list(filter(lambda x: x.get('WalletPointTypeID') == TransferDict.VABattle_gold.value, wallet_list))
            #     if coda[0]["Balance"] < 5000:
            #         api.apiGetData(method='post', api_url=FontAPI.wallet_transfer.value,data={'CheckProviderMember': True, 'FromWalletPointTypeID': 1, 'Point': 1000,'ToWalletPointTypeID': TransferDict.VASlot_gold.value})
            #     else:
            #         break
            # else:
            #     time.sleep(3)
        try:
            game_link = requests.get(url=FontAPI.game_gameLink.value,headers={"Authorization":"Bearer "+ token},params={"Platform": "web","PointTypeID": 1,
            "GameID": i['GameID'],
            "GameProvider": i['Vendor']['GameProvider'],
            "GameProviderGameID": i['Vendor']['GameProviderGameID'],
            "ReturnUrl": f'{i["GameID"]}',
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
        while True:
           driver.driver.find_element(By.XPATH, '//canvas[@id="GameCanvas"]').send_keys(Keys.SPACE)
           time.sleep(5)
           res = api.apiGetData(method='get', api_url=FontAPI.wallet_search.value,payload={'CheckProviderMember': False, 'UpdateFromProvider': True, 'Locale': 'zh-TW'})
           balance = list(filter(lambda x:x['WalletPointTypeID'] == TransferDict.VABattle_gold.value,res['Data']))
           if balance[0]['Balance'] < 2000:
               break
        # if len(driver.driver.window_handles) > 1:
        #     driver.driver.switch_to.window(driver.driver.window_handles[-1])
        # driver.driver.close()
        # driver.driver.switch_to.window(driver.driver.window_handles[0])
if __name__ == '__main__':
    game = gameList()
    play_game('',game=game)
