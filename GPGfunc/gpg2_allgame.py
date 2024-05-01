import time
import random
from testcase.gpg2_chromeset import driver_eng
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  # 座標點擊
# from script.utils import classify_aHash
import cv2 as cv
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
back_url = '  Token/SignIn'


class ManageGPG():  # 後台GPG功能實作
    def __init__(self, acc_info=None):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
        if acc_info == None:
            data = {"Account": "GenesisPerfectGame", "Password": "123456", "Device": "Macintosh, Chrome"}
        else:
            data = {"Account": acc_info['account'], "Password": acc_info['password'], "Device": "Macintosh, Chrome"}
        self.token = requests.post(back_url, json=data, headers=self.headers).json()['access_token']

    def CustomerServiceChange(self, MemberID):
        url = '  Member/CustomerServiceChange'
        self.headers['authorization'] = 'Bearer %s' % self.token
        data = {"MemberID": MemberID, "PointTypeID": 1, "Point": "1000", "Note": "QA for automation gpg mining test"}
        response = requests.post(url, headers=self.headers, json=data).json()
        print(response)
        time.sleep(1)

class driver(driver_eng):
    def allGame(self):
        # self.AgentLogin(account='trial888888881', password='kdith43')
        self.loginV2()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//div[contains(@class,"aside__container")]/ul/li[2]').click()
        list(map(lambda i: self.playGame(i[0] + 1),
                 enumerate(self.driver.find_elements_by_xpath('//div[contains(@class,"game__list__wrap")]/div/div'))))

    def playGame(self, i):
        # WebDriverWait(self.selfdriver,10,0.5).until(EC.element_located_to_be_selected,(By.XPATH,'//div[contains(@class,"game__list__wrap")]/div/div[{index}]/div/picture/img'.format(index=i)))
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//div[contains(@class,"game__list__wrap")]/div/div[{index}]'.format(index=i)).click()
        self.driver.implicitly_wait(10)
        button = self.driver.find_element_by_xpath('//div[contains(@class,"game-detail__play")]')
        self.driver.execute_script("arguments[0].click();", button)
        try:
            res = random.choice(self.driver.find_elements_by_xpath('//div[contains(@class,"game-pop__coin__list")]'))
        except:
            self.driver.find_element_by_xpath('//div[contains(@class,"game-detail__play")]').click()
            res = random.choice(self.driver.find_elements_by_xpath('//div[contains(@class,"game-pop__coin__list")]'))
        res.click()
        self.playGamev1(i)
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切換操作分業視窗
        self.driver.find_element_by_xpath('//a[@href="/game"]').click()
        # self.cvpress(,'test')

    def takePicture(self, index):
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切換操作分業視窗
        time.sleep(10)
        ActionChains(self.driver).move_by_offset(964, 730).click().perform()
        ActionChains(self.driver).move_by_offset(-964, -730).perform()
        self.driver.save_screenshot('script/img/GameResult/game_%s.png' % index)
        self.driver.close()

    def playGamev1(self, index):
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切換操作分業視窗
        time.sleep(20)
        ActionChains(self.driver).move_by_offset(964, 730).click().perform()
        ActionChains(self.driver).move_by_offset(-964, -730).perform()
        self.driver.switch_to_frame('cocosIframe')  # 新ＶＡ外包iframe 處理
        for _ in range(5):
            self.driver.find_element_by_xpath('//canvas[@id="GameCanvas"]').send_keys(Keys.SPACE)
            time.sleep(3)
        self.driver.save_screenshot('script/img/GameResult/game_%s.png' % index)
        self.driver.close()

    def cvpress(self, index):
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切換操作分業視窗
        count = 0
        identity = 'test'
        while True:
            try:
                self.driver.save_screenshot('script/img/GameResult/game_%s_%s.png' % (index, identity))  # 顏色採樣
                ActionChains(self.driver).move_by_offset(964, 730).click().perform()
                ActionChains(self.driver).move_by_offset(-964, -730).perform()
                self.driver.find_element_by_tag_name('canvas').send_keys(Keys.SPACE)
                if classify_aHash(cv.imread('script/img/GameResult/game_%s.png' % index),
                                  cv.imread('script/img/GameResult/game_%s_%s.png' % (index, identity))) < 10:
                    for _ in range(4):
                        ActionChains(self.driver).move_by_offset(964, 730).click().perform()
                        ActionChains(self.driver).move_by_offset(-964, -730).perform()
                        self.driver.find_element_by_tag_name('canvas').send_keys(Keys.SPACE)
                    self.driver.save_screenshot('script/img/GameResult/game_%s_%s.png' % (index, identity))  # 點擊採樣
                    break
                else:
                    count += 1  # retry次數
                    if count >= 40:  # 先抓30
                        break
            except:
                pass
        if classify_aHash(cv.imread('script/img/GameResult/game_%s.png' % index),
                          cv.imread('script/img/GameResult/game_%s_%s.png' % (index, identity))) >= 20:
            pass
        self.driver.quit()

def run():
    driver().allGame()


if __name__=='__main__':
    driver().allGame()

    # scheduler = BlockingScheduler()
    # scheduler.add_job(run,"interval",minutes=30)
    # scheduler.start()