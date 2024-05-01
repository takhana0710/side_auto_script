import random
import time
from testcase.gpg2_chromeset import driver_eng, gpg_api,ma_api,env
from selenium.webdriver.common.by import By
from script.utils import shapev2,miniget,minigetv2,minigetv3_east,ifun_game,ifun_game_new
# from apscheduler.schedulers.blocking import BlockingScheduler
magpg = ma_api()
transfer_dict = {'gpg_gold': 1, 'VASlot_gold': 220101, 'VABattle_gold': 220103, 'gpg_sliver': 2,'VASlot_sliver': 220102, 'VABattle_sliver': 220104,'ifun_gold':90601,'ifun_sliver':90602}
"""
後台查詢
"""
parameter=[
    {'index': 1, 'ksize1': 5, 'fname1': 'ifun.png', 'fname2': 'ifun2.png', 'ksize2': 1},
    {'index': 2, 'ksize1': 5, 'fname1': 'ifun.png', 'fname2': 'ifun2.png', 'ksize2': 1},
    {'index': 3,'ksize1': 5,  'fname1': 'ifun.png', 'fname2': 'ifun2.png', 'ksize2': 5},
    {'index': 4, 'ksize1': 5,'fname1': 'ifun.png', 'fname2': 'ifun2.png', 'ksize2': 5},
    {'index': 5, 'ksize1':5,'fname1':'ifun.png','fname2':'ifun2.png','ksize2':1},
    {'index': 6, 'ksize1':5,'fname1':'ifun.png','fname2':'ifun2.png','ksize2':5},
    {'index': 7, 'ksize1':5,'fname1':'va.png','fname2':'va2.png','ksize2':5},
    {'index': 8, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 5},
    {'index': 9, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 3},
    {'index': 10, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 5},
    {'index': 11, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 5},
    {'index': 12, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 3},#
    {'index': 13, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 5},
    {'index': 14, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 5},
    {'index': 15, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 3},
    {'index': 16, 'ksize1': 3,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 5},
    {'index': 17, 'ksize1': 3,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 3},
    {'index': 18, 'ksize1': 3,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 1},#
    {'index': 19, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 1},#
    {'index': 20, 'ksize1': 1,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 5},
    {'index': 21, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 1},#
    {'index': 22, 'ksize1': 5,'fname1': 'va.png','shape1':4, 'fname2': 'va2.png', 'ksize2': 5},
    {'index': 23, 'ksize1': 3,'fname1': 'va.png','shape1':13,'fname2': 'va2.png', 'ksize2': 3},#
    {'index': 24, 'ksize1': 3,'fname1': 'va.png','shape1':10, 'fname2': 'va2.png', 'ksize2': 1,'shape2':8},#神龍寶藏
    {'index': 25, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 3},#
    {'index': 26, 'ksize1': 5,'fname1': 'va.png', 'fname2': 'va2.png', 'ksize2': 3},#
]
def backSearch():
    # res = magpg.apiGetData(method='get',api_url=env['back_api']+'Member/MemberList',payload={'IsFuzzySearch': True,'PhoneNumber': '  ','Skip': 0,'Show': 50,'Field': 'CreateTime','OrderType': 'desc','IsGuest': False})['Data'] #搜尋全部測試帳號
    # pay = [i.get('MemberID') for i in res if i.get('GoldPoint')<1000 or i.get('SilverPoint')<30000] # 驗證是否沒錢
    # list(map(lambda x: magpg.apiGetData(method='post',api_url=env['back_api']+'Member/CustomerServiceChange',data={"MemberID":x,"PointTypeID":1,"Point":"1000","Note":"QA礦機補錢"}),pay)) # 金幣
    # list(map(lambda x: magpg.apiGetData(method='post', api_url=env['back_api']+'Member/CustomerServiceChange',data={"MemberID": x, "PointTypeID": 2, "Point": "10000", "Note": "QA礦機補錢"}), pay)) # 銀幣
    # res = [i.get('PhoneNumber') for i in res]
    # res.extend(['  22','  21','  20']) # 新增代理本人線
    res = [20,97,96,27,21,22,24,37,23,34,33]
    return res
"""
前台登入
"""
def transferWallet(api):
    # print('轉帳中')
    api.apiGetData(method='post',data={'CheckProviderMember': True, 'FromWalletPointTypeID': transfer_dict.get('gpg_gold'),'Point': '500', 'ToWalletPointTypeID': transfer_dict.get('VASlot_gold')},api_url=env['font_api'] + 'Wallet/Transfer')
    api.apiGetData(method='post',data={'CheckProviderMember': True, 'FromWalletPointTypeID': transfer_dict.get('gpg_gold'),'Point': '500', 'ToWalletPointTypeID': transfer_dict.get('ifun_gold')},api_url=env['font_api'] + 'Wallet/Transfer')
    # api.apiGetData(method='post',data={'CheckProviderMember': True, 'FromWalletPointTypeID': transfer_dict.get('gpg_sliver'),'Point': '10000', 'ToWalletPointTypeID': transfer_dict.get('VASlot_sliver')},api_url=env['font_api'] + 'Wallet/Transfer')
    # time.sleep(30) # 等金額錢包同步
def playGame():
    driver = driver_eng()
    account = '  '+str(random.choice(backSearch()))
    # print(account)
    gameList = driver.playGame(account=account)
    api = gpg_api(token=driver.token)
    check = api.apiGetData(method='get',payload={'CheckProviderMember': True,'UpdateFromProvider': True},api_url=env['font_api']+'Wallet/Search').get('Data')
    if check == None: # 當錢包取得錯誤
        return False
    index = 23
    para = list(filter(lambda x:x.get('index')==index,parameter)).pop()
    driver.gameDetail(index)
    if index<7:
        [transferWallet(api) for i in check if (i.get('WalletPointTypeID') == transfer_dict.get('ifun_gold') and i.get('Balance') < 100)]
        while True:
           print('AAAAA')
           try:
               driver.driver.find_element(By.XPATH,'//div[contains(@class,"game-pop__coin__list")]/div[%s]' % 1).click()
               driver.driver.switch_to.window(driver.driver.window_handles[1])  # 切換操作分業視窗
               break
           except:
               continue
        time.sleep(random.randint(60,80))
        driver.driver.save_screenshot(para.get('fname1'))
        ifun_game_new(driver=driver,ksize=para.get('ksize1'),filename=para.get('fname1'),area=para.get('area1'),dot=para.get('dot1'))
        print('r2')
        time.sleep(2)
        driver.driver.save_screenshot(para.get('fname2'))
        ifun_game_new(driver=driver,ksize=para.get('ksize2'),filename=para.get('fname2'),area=para.get('area2'),dot=para.get('dot2'))
        time.sleep(5)
    else:
        [transferWallet(api) for i in check if (i.get('WalletPointTypeID') == transfer_dict.get('VASlot_gold') and i.get('Balance') < 100)]
        while True:
            try:
                driver.driver.find_element(By.XPATH,'//div[contains(@class,"game-pop__coin__list")]/div[%s]' % 2).click()
                driver.driver.switch_to.window(driver.driver.window_handles[1])  # 切換操作分業視窗
                break
            except:
                continue
        time.sleep(random.randint(20,30))
        driver.driver.save_screenshot(para.get('fname1'))
        ifun_game_new(driver=driver,ksize=para.get('ksize1'),filename=para.get('fname1'),shape=para.get('shape1'))
        print('r2')
        time.sleep(2)
        driver.driver.save_screenshot(para.get('fname2'))
        # ifun_game_new(driver=driver,ksize=para.get('ksize2'),filename=para.get('fname2'),shape=para.get('shape2'))
    # driver.driver.switch_to.window(driver.driver.window_handles[0])  # 切換操作分業視窗
    # driver.mining()
    # driver.driver.switch_to.frame(driver.driver.find_element(By.XPATH,'//iframe[contains(@class,"mine__frame")]'))
    # minigetv3_east(driver)
    # driver.exit()
    # return True

# if playGame() == False:
#     print('錢包獲取失敗')
if __name__=='__main__':
    playGame()
    # scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(playGame,"cron",minute='*/5',hour='2-20')
    # try:
    #     scheduler.start()
    # except (KeyboardInterrupt, SystemExit) as e:
    #     print(e)