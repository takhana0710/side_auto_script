import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  # 座標點擊
import requests
import cv2 as cv
from .utils import classify_aHash

url = ''
hook = 'https://hooks.slack.com/services/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'


class Allgame_Guest:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')
        options.add_argument('--no-sandbox')
        # options.add_argument("--auto-open-devtools-for-tabs") # 開發者模式
        # options.add_argument('--headless')
        options.add_argument('--mute-audio')
        options.add_experimental_option('prefs', {'intl.accept_languages': 'zh_TW'})  # 強制改瀏覽器的語系
        self.driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
        # self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)
        try:
            self.driver.execute_script('window.localStorage.setItem("language","zh-tw");')
            self.driver.find_element(By.XPATH, '//*[@class="member-default-pic"]').click()
            self.driver.find_element(By.XPATH, '//*[@class="btn btn-login-guest"]').click()
            self.driver.implicitly_wait(5)
            for _ in range(2):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/a').click()
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/a').click()
        except:
            requests.post(hook, json={'text': '回歸測試-測試全遊戲創訪客錯誤，請排查'}, headers={'Content-Type': 'application/json'})

    def PlayGame(self):
        self.driver.find_element(By.XPATH, '//*[@class="menu-box"]/a[2]').click()
        li = self.driver.find_elements(By.XPATH, '//*[@class="game-list"]/div')
        for i in li:
            element = self.driver.find_element(By.XPATH, '//*[@class="game-list"]/div[%s]' % str(li.index(i) + 1))
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@class="game-pic-box"]/a').click()
            self.driver.find_element(By.XPATH, '//*[@class="game-coin-box"]/div[2]/div[2]').click()
            time.sleep(8)
            self.driver.switch_to.window(self.driver.window_handles[1])
            for _ in range(7):
                ActionChains(self.driver).move_by_offset(554, 421).click().perform()
                ActionChains(self.driver).move_by_offset(-554, -421).perform()
                try:
                    self.driver.find_element_by_tag_name('canvas').send_keys(Keys.SPACE)
                except:
                    requests.post(hook, json={'text': '回歸測試-測試全遊戲無法偵測到畫面，定位前端頁面數來第%s個' % str(li.index(i) + 1)},
                                  headers={'Content-Type': 'application/json'})
                    continue
            time.sleep(2)
            while True:
                try:
                    self.driver.save_screenshot('script/img/GameResult/game_%s_test.png' % str(li.index(i) + 1))  # 採樣
                    break # 跳離迴圈
                except:
                    time.sleep(10) # retry休息
            if classify_aHash(cv.imread('script/img/GameResult/game_%s.png' % str(li.index(i) + 1)),
                              cv.imread('script/img/GameResult/game_%s_test.png' % str(li.index(i) + 1))) >= 20:
                requests.post(hook, json={'text': '回歸測試-測試全遊戲第%s個原圖匹配差太多請查看' % str(li.index(i) + 1)},
                              headers={'Content-Type': 'application/json'})
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.find_element(By.XPATH, '//*[@class="menu-box"]/a[2]').click()



class Allgame_trial:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')
        options.add_argument('--no-sandbox')
        # options.add_argument("--auto-open-devtools-for-tabs") # 開發者模式
        # options.add_argument('--headless')
        options.add_argument('--mute-audio')
        options.add_experimental_option('prefs', {'intl.accept_languages': 'zh_TW'})  # 強制改瀏覽器的語系
        self.driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
        # self.driver = webdriver.Chrome(options=options)
        self.driver.get(url)
        try:
            self.driver.execute_script('window.localStorage.setItem("language","zh-tw");')
            self.driver.find_element(By.XPATH, '//*[@class="member-default-pic"]').click()
            for i in '  ':  # 改變寫法模擬慢慢輸入避免一次輸入打到送出驗證碼ＡＰＩ導致失敗
                self.driver.find_element(By.XPATH, '//*[@id="MazPhoneNumberInput"]/div[2]/div/input').send_keys(i)
                time.sleep(0.1)
            time.sleep(3)  # 隱性等待
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[3]/a').click()
            """必要時得異常狀況攔截"""
            for i in range(4):
                self.driver.implicitly_wait(2)  # 隱性等待
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div[2]/input[%s]' % str(
                    int(i) + 1)).send_keys('0')
            self.driver.find_element(By.XPATH, '//*[@class="step-box"]/div[4]/a').click()  # 驗證按鈕登入
        except:
            requests.post(hook, json={'text': '回歸測試-測試全遊戲創訪客錯誤，請排查'}, headers={'Content-Type': 'application/json'})

    def PlayGame(self):
        while True:
            try:
                self.driver.find_element(By.XPATH, '//*[@class="menu-box"]/a[2]').click()
                break
            except:
                time.sleep(10)
        li = self.driver.find_elements(By.XPATH, '//*[@class="game-list"]/div')
        for i in li:
            element = self.driver.find_element(By.XPATH, '//*[@class="game-list"]/div[%s]' % str(li.index(i) + 1))
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@class="game-pic-box"]/a').click()
            self.driver.find_element(By.XPATH, '//*[@class="game-coin-box"]/div[2]/div[2]/a[2]').click()
            time.sleep(8)
            self.driver.switch_to.window(self.driver.window_handles[1])
            for _ in range(7):
                ActionChains(self.driver).move_by_offset(554, 421).click().perform()
                ActionChains(self.driver).move_by_offset(-554, -421).perform()
                try:
                    self.driver.find_element_by_tag_name('canvas').send_keys(Keys.SPACE)
                except:
                    requests.post(hook, json={'text': '回歸測試-測試全遊戲無法偵測到畫面，定位前端頁面數來第%s個' % str(li.index(i) + 1)},
                                  headers={'Content-Type': 'application/json'})
                    continue
            time.sleep(2)
            while True:
                try:
                    self.driver.save_screenshot('script/img/GameResult/game_%s_trial.png' % str(li.index(i) + 1))  # 採樣
                    break # 跳離迴圈
                except:
                    time.sleep(10) # retry休息
            if classify_aHash(cv.imread('script/img/GameResult/game_%s.png' % str(li.index(i) + 1)),
                              cv.imread('script/img/GameResult/game_%s_trial.png' % str(li.index(i) + 1))) >= 20:
                requests.post(hook, json={'text': '回歸測試-測試全遊戲第%s個原圖匹配差太多請查看' % str(li.index(i) + 1)},
                              headers={'Content-Type': 'application/json'})
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.find_element(By.XPATH, '//*[@class="menu-box"]/a[2]').click()
