
import time
from testcase.gpg2_chromeset import driver_eng,FontAPI,env,TransferDict
from selenium.webdriver.common.action_chains import ActionChains  # 座標點擊
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
def progressNotify(msg):
    hook='https://hooks.slack.com/services/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' # gpg_game
    # hook = 'https://hooks.slack.com/services/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' # CEIS_QA
    requests.post(hook, json={"text":msg}, headers={'Content-Type': 'application/json'})
driver = driver_eng(url=env['font_url'])
action = ActionChains(driver.driver)
driver.changeLanguage()
# driver.loginV2(member_account=env['member_account'],send_site=env['site_send'])
# driver.logout()
driver.loginV2(identity='guest')
token=driver.getToken()
# print(FontAPI.member_memberInfo.value)
member_info = requests.get(url=FontAPI.member_memberInfo.value,headers={"Authorization":f"Bearer {token}"}).json()
# print(member_info)
time.sleep(30)
res_transfer = requests.post(url=FontAPI.wallet_transfer.value,headers={"Authorization":f"Bearer {token}"},
                             json={'CheckProviderMember': True, 'FromWalletPointTypeID': 2, 'Point': 30000,
                                    'ToWalletPointTypeID':TransferDict.VASlot_silver.value}).json()
print(res_transfer)
time.sleep(10)
if env['env'] == 'ph':
    site = '日本'
elif env['env'] == 'sp':
    site = '新加坡'
else:
    site = '台灣正式站'
progressNotify(msg=f'訪客的會員ID:{member_info["Data"]["MemberID"]}在{site}開始玩遊戲')
res_game = requests.get(url=env['font_api']+'Game/GameList',params={"Locale": "en-US"}).json()
for j,i in enumerate(res_game['Data'][:10]):
    if i["Vendor"]["GameProvider"]!="VA":
        continue
    driver.driver.get(env['font_url']+f'game/detail/{i["GameID"]}')
    if j==0:
        driver.driver.execute_script("arguments[0].click();", driver.driver.find_element(By.XPATH,'//div[contains(@class,"game-detail__play") and text()="立即遊玩"]'))
        driver.driver.find_element(By.XPATH, '//div[contains(@class,"game-pop__coin__label")]').click()
        driver.driver.find_element(By.XPATH,'//div[contains(@class,"wallet-sample__item") and text()="全部"]').click()
        driver.driver.find_element(By.XPATH, '//div[text()="確認轉帳"]').click()
        driver.driver.find_element(By.XPATH, '//div[contains(@class,"wallet__close")]').click()
    time.sleep(5)
    driver.driver.execute_script("arguments[0].click();", driver.driver.find_element(By.XPATH,'//div[contains(@class,"game-detail__play") and text()="立即遊玩"]'))
    driver.driver.find_element(By.XPATH, '//div[contains(@class,"game-pop__coin__label")]').click()
    driver.driver.find_element(By.XPATH, '//div[text()="直接進入遊戲"]').click()
    driver.driver.switch_to.window(driver.driver.window_handles[1])  # 切換操作分業視窗
    size = driver.driver.get_window_size()
    width = size['width'] / 2
    height = size['height'] * 0.53
    for _ in range(2):
        action.move_by_offset(width, height).click().perform()
        action.move_by_offset(-width, -height).click().perform()
        action.move_by_offset(width, size['height'] * 0.1).click().perform()
        action.move_by_offset(-width, -size['height'] * 0.1).click().perform()
        time.sleep(2)
        driver.driver.find_element(By.XPATH, '//canvas[@id="GameCanvas"]').send_keys(Keys.SPACE)
        time.sleep(5)
        # if len(driver.driver.window_handles) > 1:
        #     driver.driver.switch_to.window(driver.driver.window_handles[-1])
        #     print('=====>'+str(i['GameID']))
    driver.driver.close()
    driver.driver.switch_to.window(driver.driver.window_handles[0]) 
progressNotify(msg='測試完成')