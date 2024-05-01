"""放一些共同函數或者方法"""
import sys

import pandas as pd
import unittest
from unittest import result
from datetime import datetime
# import cv2 as cv
import numpy as np
import requests
import time
from selenium.webdriver.common.action_chains import ActionChains  # 座標點擊
from selenium.webdriver.common.by import By
# import imutils
from selenium.webdriver.common.keys import Keys
# from imutils.object_detection import non_max_suppression
# import pytesseract
from matplotlib import pyplot as plt
"""圖形相似度"""

ip_config = '192.168.0.35:8000'

# def classify_aHash(image1, image2):
#     image1 = cv.resize(image1, (8, 8))
#     image2 = cv.resize(image2, (8, 8))
#     gray1 = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
#     gray2 = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)
#     hash1 = getHash(gray1)
#     hash2 = getHash(gray2)
#     return Hamming_distance(hash1, hash2)

def getHash(image):
    average = np.mean(image)
    hash = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > average:
                hash.append(1)
            else:
                hash.append(0)
    return hash


def Hamming_distance(hash1, hash2):
    num = 0
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            num += 1
    return num


"""測試結果轉json"""

url = 'http://%s/qa/getresult/' % ip_config


class MyTextTestResult(result.TestResult):
    def __init__(self, descriptions):
        super(MyTextTestResult, self).__init__(descriptions)
        self.descriptions = descriptions
        self.js_data = dict()  # 測試結果json
    
    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return ','.join((doc_first_line, str(test)))
        else:
            return str(test)
    
    def startTest(self, test):
        super(MyTextTestResult, self).startTest(test)
    
    def addSuccess(self, test):
        super(MyTextTestResult, self).addSuccess(test)
        self.js_data['testCase'] = self.getDescription(test)  # 案例名稱
        self.js_data['testResult'] = 'pass'  # 測試結果
        self.js_data['testTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 執行時間
        self.js_data['errorMsg'] = ''  # 錯誤訊息
        self.js_data['qaCheckReason'] = ''  # qa排查狀況註解
        print(requests.post(url, json=self.js_data).text)
    
    def addError(self, test, err):
        super(MyTextTestResult, self).addSuccess(test)
        self.js_data['testCase'] = self.getDescription(test)
        self.js_data['testResult'] = 'error'
        self.js_data['testTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.js_data['errorMsg'] = str(err)
        self.js_data['qaCheckReason'] = ''  # qa排查狀況註解
        print(requests.post(url, json=self.js_data).text)
    
    def addFailure(self, test, err):
        super(MyTextTestResult, self).addFailure(test, err)
        self.js_data['testCase'] = self.getDescription(test)
        self.js_data['testResult'] = 'fail'
        self.js_data['testTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.js_data['errorMsg'] = str(err)
        self.js_data['qaCheckReason'] = ''  # qa排查狀況註解
        print(requests.post(url, json=self.js_data).text)


class MyTextTestRunner(unittest.TextTestRunner):
    NewResultClass = MyTextTestResult
    
    def __init__(self):
        super(MyTextTestRunner, self).__init__()
        self.descriptions = True
    
    def _makeResult(self):  # 製作結果
        return self.NewResultClass(self.descriptions)
    
    def run(self, test):
        result = self._makeResult()
        startTestRun = getattr(result, 'startTestRun', None)
        startTestRun()  # 準備
        test(result)  # 執行
        stopTestRun = getattr(result, 'stopTestRun', None)  # 結束
        stopTestRun()
        return result


"""自動玩遊戲"""


# class ShapeDetector:  # 輪廓檢測
#     def detect(self, c):
#         shape = "unidentified"
#         peri = cv.arcLength(c, True)
#         approx = cv.approxPolyDP(c, 0.04 * peri, True)
#         if len(approx) == 3:
#             shape = "triangle"
#         elif len(approx) == 4:
#             (x, y, w, h) = cv.boundingRect(approx)
#             ar = w / float(h)
#             shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
#         elif len(approx) == 5:
#             shape = "pentagon"
#         else:
#             shape = "circle"
#         return shape


# def color(image, low, upper):
#     lower = np.array(low, dtype='uint8')
#     upper = np.array(upper, dtype='uint8')  # 過濾白色
#     mask = cv.inRange(image, lower, upper)
#     output = cv.bitwise_and(image, image, mask=mask)
#     # cv.imshow("image",np.hstack([image,output]))
#     # cv.waitKey(0)
#     output = cv.cvtColor(output, cv.COLOR_HSV2BGR)
#     cv.imwrite('output_color.png', output)
#     return output


# def shape(): #
#     while True:
#         try:
#             driver.driver.save_screenshot('test.png')
#             image = cv.imread('test.png')
#             # image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
#             # image = color(image)  # 先篩選出白色區塊包含開始按鈕
#             blur = cv.GaussianBlur(image, (3, 3), 0)
#             # lab = cv.cvtColor(blur, cv.COLOR_BGR2Lab)
#             gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
#             thresh = cv.Canny(gray, 0, 255, cv.THRESH_BINARY)  # 閥值二值化
#             cv.imwrite('output.png', thresh)
#             cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#             cnts = imutils.grab_contours(cnts)
#             sd = ShapeDetector()
#             cnts = sorted(cnts,key=cv.contourArea, reverse=True)[:3]  # 排序取出最大的前5個
#             for c in cnts:
#                 M = cv.moments(c)
#                 text = sd.detect(c)
#                 cX = int((M["m10"] / M["m00"]))
#                 cY = int((M["m01"] / M["m00"]))
#                 cv.drawContours(image, [c], -1, (0, 255, 0), 2)
#                 cv.putText(image, text, (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#                 cv.imwrite('result.png', image)
#                 if text == 'circle':
#                     cX = int((M["m10"] / M["m00"]))
#                     cY = int((M["m01"] / M["m00"]))
#                     # ActionChains(driver.driver).move_by_offset(cX, cY).click().perform()
#                     # ActionChains(driver.driver).move_by_offset(-cX, -cY).perform()
#                     print('circle',cX,cY)
#                 elif text=='triangle':
#                     cX = int((M["m10"] / M["m00"]))
#                     cY = int((M["m01"] / M["m00"]))
#                     # ActionChains(driver.driver).move_by_offset(cX, cY).click().perform()
#                     # ActionChains(driver.driver).move_by_offset(-cX, -cY).perform()
#                     print('triangle',cX,cY)
#                     # count+=1
#             # if count == 3:
#             #     break
#         except:
#             driver.driver.save_screenshot('test.png')
#
# def is_contour_bad(c):
#     peri = cv.arcLength(c, True)
#     approx = cv.approxPolyDP(c, 0.02 * peri, True)#多邊形判定
#     print('面積',cv.contourArea(c))
#     print('點',len(approx))
#     return len(approx)
#

# def shapev2(driver):  # 改版後的邊緣偵測
#     time.sleep(20)
#     driver.driver.save_screenshot('test.png')
#     image = cv.imread('test.png')
#     cv.imwrite('D:/test.png',image)
#     v = np.median(image)
#     lower = int(max(0, (1.0 - 0.33) * v))
#     upper = int(min(255, (1.0 + 0.33) * v))
#     blur = cv.GaussianBlur(image, (3, 3), 0)
#     gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
#     thresh = cv.Canny(gray, lower, upper, cv.THRESH_BINARY)  # 閥值二值化
#     cv.imwrite('output.png', thresh)
#     cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     cnts = sorted(cnts, key=cv.contourArea, reverse=True)[:30]  # 排序取出最大的前5個
#     for c in cnts:
#         if is_contour_bad(c) >= 5:
#             M = cv.moments(c)
#             if M['m00'] == 0:
#                 continue
#             cX = int((M["m10"] / M["m00"]))
#             cY = int((M["m01"] / M["m00"]))
#             cv.putText(image, 'clickA', (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#             cv.imwrite('result.png', image)
#             ActionChains(driver.driver).move_by_offset(cX, cY).click().perform()
#             ActionChains(driver.driver).move_by_offset(-cX, -cY).perform()
#     driver.driver.switch_to.frame('cocosIframe')
#     time.sleep(5)
#     for _ in range(2):
#         driver.driver.find_element(By.XPATH, '//canvas[@id="GameCanvas"]').send_keys(Keys.SPACE)
#         time.sleep(5)
#     driver.driver.save_screenshot('game.png')
#     image = cv.imread('game.png')
#     cv.imwrite('D:/game.png',image)
#
# def miniget(driver):
#     time.sleep(15)
#     driver.driver.save_screenshot('mini.png')
#     image = cv.imread('mini.png')
#     get = cv.imread('script/img/get.png')
#     img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     get = cv.cvtColor(get, cv.COLOR_BGR2GRAY)
#     res = cv.matchTemplate(img, get, cv.TM_SQDIFF)
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
#     print(min_loc, min_val)
#     ActionChains(driver.driver).move_by_offset(min_loc[0], min_loc[1]).click().perform()
#     ActionChains(driver.driver).move_by_offset(-min_loc[0], -min_loc[1]).perform()  # 還原滑鼠，否則會因為多次運行而報錯超出視窗
#
#
# def minigetv2(driver):
#     time.sleep(15)
#     driver.driver.save_screenshot('mini.png')
#     image = cv.imread('mini.png')
#     v = np.median(image)
#     lower = int(max(0, (1.0 - 0.33) * v))
#     upper = int(min(255, (1.0 + 0.33) * v))
#     blur = cv.GaussianBlur(image, (3, 3), 0)
#     gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
#     thresh = cv.Canny(gray, lower, upper, cv.THRESH_BINARY)  # 閥值二值化
#     cv.imwrite('output_test.png', thresh)
#
# args = {"east":"script/east_text_detection.pb","min_confidence":0.5, "width":320, "height":320}
# pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files/Tesseract-OCR/tesseract.exe'
# def predictions(prob_score,geo):
#     (numR,numC) = prob_score.shape[2:4]
#     boxes  = []
#     confidence_val =[]
#     for y in range(0,numR):
#         scoresData = prob_score[0,0,y]
#         x0=geo[0,0,y]
#         x1=geo[0,1,y]
#         x2=geo[0,2,y]
#         x3=geo[0,3,y]
#         anglesData = geo[0,4,y]
#         for i in range(0,numC):
#             if scoresData[i] < args['min_confidence']:
#                 continue
#             (offX, offY) = (i * 4.0, y * 4.0)
#             angle = anglesData[i]
#             cos = np.cos(angle)
#             sin = np.sin(angle)
#             h = x0[i] + x2[i]
#             w = x1[i] + x3[i]
#             endX = int(offX + (cos * x1[i]) + (sin * x2[i]))
#             endY = int(offY - (sin * x1[i]) + (cos * x2[i]))
#             startX = int(endX - w)
#             startY = int(endY - h)
#             boxes.append((startX, startY, endX, endY))
#             confidence_val.append(scoresData[i])
#     return (boxes, confidence_val)


# def minigetv3_east(driver):
#     """02/16 EAST模型辨識按鈕"""
#     driver.driver.save_screenshot('mini.png')
#     image = cv.imread('mini.png',cv.COLOR_BGR2GRAY)
#     temp = cv.imread('script/img/close.png',cv.COLOR_BGR2GRAY)
#     # print(type(image))
#     # print(type(temp))
#     res = cv.matchTemplate(image,temp,cv.TM_SQDIFF)
#     min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)
#     im2 = image.copy()
#     im2 = cv.rectangle(im2, (min_loc[0], min_loc[1]), (max_loc[0], max_loc[1]), (0, 255, 0), 2)
#     cv.imwrite('aaa.png', im2)
#     print(min_loc,max_loc)
#     ActionChains(driver.driver).move_by_offset(min_loc[0],min_loc[1]).click().perform()
#     ActionChains(driver.driver).move_by_offset(-min_loc[0],-min_loc[1]).perform() # 還原滑鼠，否則會因為多次運行而報錯超出視窗
#     ActionChains(driver.driver).move_by_offset(max_loc[0],max_loc[1]).click().perform()
#     ActionChains(driver.driver).move_by_offset(-max_loc[0],-max_loc[1]).perform() # 還原滑鼠，否則會因為多次運行而報錯超出視窗
#     time.sleep(3)
#     driver.driver.save_screenshot('mini.png')
#     image = cv.imread('mini.png')
#     cv.imwrite('D:/mini.png',image)
#     orig = image.copy()
#     (origH, origW) = image.shape[:2]
#     (newW, newH) = (args['width'], args['height'])
#     rW = origW / float(newW)
#     rH = origH / float(newH)
#     image = cv.resize(image, (newW, newH))
#     (H, W) = image.shape[:2]
#     blob = cv.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)  # 圖片讀取預處理
#     net = cv.dnn.readNet(args['east'])
#     layerNames = ["feature_fusion/Conv_7/Sigmoid", "feature_fusion/concat_3"]
#     net.setInput(blob)
#     (scores, geometry) = net.forward(layerNames)
#     (boxes, confidence_val) = predictions(scores, geometry)
#
#     boxes = non_max_suppression(np.array(boxes), probs=confidence_val)
#     results = []
#     for (startX, startY, endX, endY) in boxes:
#         startX = int(startX * rW)
#         startY = int(startY * rH)
#         endX = int(endX * rW)
#         endY = int(endY * rH)
#         r = orig[startY:endY, startX:endX]
#         # configuration = ('-l eng --oem 1 --psm 8')
#         configuration = ('-l eng')
#         text = pytesseract.image_to_string(r, config=configuration)
#         results.append(((startX, startY, endX, endY), text))
#     orig_image = orig.copy()
#     for ((start_X, start_Y, end_X, end_Y), text) in results:
#         # print('{}\n'.format(text))
#         text = "".join([x if ord(x) < 128 else "" for x in text]).strip()
#         # cv.rectangle(orig_image, (start_X, start_Y), (end_X, end_Y), (0, 0, 255), 2)
#         # cv.putText(orig_image, text, (start_X, start_Y - 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#         if text != 'GET!':
#             continue
#         else:
#             ActionChains(driver.driver).move_by_offset(start_X, start_Y).click().perform()
#             ActionChains(driver.driver).move_by_offset(-start_X, -start_Y).perform()  # 還原滑鼠，否則會因為多次運行而報錯超出視窗
#     # plt.imshow(orig_image)
#     # plt.title('OutPut')
#     # plt.show()


class TimeSelect:  # 時間選擇器
    def __init__(self):
        self.today = datetime.today().strftime('%Y%m%d')
    
    def OverMonthStart(self):
        """從今天算起兩個月"""
        return pd.date_range(end=self.today, periods=60)[0].strftime('%Y-%m-%dT%H:%M:%S+08:00')
    
    def MonthEnd(self):
        """兩個月結束"""
        return pd.date_range(end=self.today, periods=30)[-1].strftime('%Y-%m-%dT%H:%M:%S+08:00')
    
    def MonthStart(self):
        """從今天算起一個月"""
        return pd.date_range(end=self.today, periods=31)[0].strftime('%Y-%m-%dT%H:%M:%S+08:00')
    def oauthTime(self):
        return pd.date_range(end=self.today, periods=31)[0].strftime('%Y-%m-%d+%H:%M:%S')

# def ifun_game(driver,ksize,filename):
#     img = cv.imread(filename)
#     img2 = img.copy()
#     v = np.median(img2)
#     lower = int(max(0, (1.0 - 0.33) * v))
#     upper = int(min(255, (1.0 + 0.33) * v))
#     img2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
#     img2 = cv.GaussianBlur(img2 ,(ksize,ksize), 0)
#     thresh = cv.Canny(img2, lower, upper, cv.THRESH_BINARY)  # 閥值二值化
#     cnts = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     cnts = sorted(cnts, key=cv.contourArea, reverse=True)[:8]  # 排序取出最大的前5個
#     cv.imwrite('aaa.png',thresh)
#     print(len(cnts))
#     for c in cnts:
#         if is_contour_bad(c) == 4:
#             M = cv.moments(c)
#             if M['m00'] == 0:
#                 continue
#             cX = int((M["m10"] / M["m00"]))
#             cY = int((M["m01"] / M["m00"]))
#             # cv.putText(img, 'clickA', (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#             ActionChains(driver.driver).move_by_offset(cX, cY).click().perform()
#             ActionChains(driver.driver).move_by_offset(-cX, -cY).perform()
#     cv.imwrite(filename, img)
#     # cv.imwrite('aaa.png',thresh)
#
    
# def ifun_game_new(**kwargs):
#     img = cv.imread(kwargs.get('filename'))
#     img2 = img.copy()
#     v = np.median(img2)
#     lower = int(max(0, (1.0 - 0.33) * v))
#     upper = int(min(255, (1.0 + 0.33) * v))
#     img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
#     img2 = cv.GaussianBlur(img2, (kwargs.get('ksize'), kwargs.get('ksize')), 0)
#     thresh = cv.Canny(img2, lower, upper, cv.THRESH_BINARY)  # 閥值二值化
#     cnts, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#     # cnts = imutils.grab_contours(cnts)
#     # cnts = sorted(cnts, key=cv.contourArea, reverse=True)  # 排序取出最大的前5個
#     cv.imwrite('aaa.png', thresh)
#     cnts = list(filter(lambda x:is_contour_bad(x) == kwargs.get('dot'),cnts))
#     for i, c in enumerate(cnts):
#         # if kwargs.get('area')-100<cv.contourArea(c)<kwargs.get('area')+100:
#             M = cv.moments(c)
#             """算出他的重心"""
#             x = int((M["m10"] / M["m00"]))
#             y = int((M["m01"] / M["m00"]))
#             cv.putText(img, 'clickA', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#             cv.drawContours(img, c, -1, (0, 0, 255), 2)
#             ActionChains(kwargs.get('driver').driver).move_by_offset(x, y).click().perform()
#             ActionChains(kwargs.get('driver').driver).move_by_offset(-x, -y).perform()
#             cv.imwrite('res%s.png' % i, img)
#             # break

def delete_contours(contours,delete_list):
    delta=0
    for i in range(len(delete_list)):
        del contours[delete_list[i]-delta]
        delta+=1
    return contours
# def otsu_canny(image, lowrate=0.1):
#     if len(image.shape) > 2:
#         image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#
#     # Otsu's thresholding
#     ret, _ = cv.threshold(image, thresh=0, maxval=255, type=(cv.THRESH_BINARY + cv.THRESH_OTSU))
#     edged = cv.Canny(image, threshold1=(ret * lowrate), threshold2=ret)
#
#     # return the edged image
#     return edged

# def ifun_game_new(**kwargs):
#     img = cv.imread(kwargs.get('filename'))
#     img2 = img.copy()
#     # v = np.median(img2)
#     # lower = int(max(0, (1.0 - 0.33) * v))
#     # upper = int(min(255, (1.0 + 0.33) * v))
#     img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
#     img2 = cv.GaussianBlur(img2, (kwargs.get('ksize'), kwargs.get('ksize')), 0)
#     # thresh = cv.Canny(img2, lower, upper, cv.THRESH_BINARY)  # 閥值二值化
#     thresh = otsu_canny(img2)
#     cnts, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # 線性沒有關聯
#     delete_list = []
#     c, row, col = hierarchy.shape
#     for i in range(row):
#         if hierarchy[0, i, 3] > 0:
#             delete_list.append(i)
#     cnts = delete_contours(cnts, delete_list)
#     delete_list=[]
#     min_size=100
#     for i, c in enumerate(cnts):
#         if cv.arcLength(cnts[i], True) < min_size:
#             delete_list.append(i)
#     cv.imwrite('aaa.png', thresh)
#     temp = np.ones(img.shape, dtype=np.uint8) * 255
#     cv.drawContours(temp, cnts, -1, (0, 0, 0), 2)
#     cv.imwrite('bbb.png',temp)
#     cnts = sorted(cnts, key=cv.contourArea, reverse=True)  # 排序取出最大的前5個
#     # cnts = list(filter(lambda x:is_contour_bad(x) == kwargs.get('dot'),cnts))
#     for i, c in enumerate(cnts):
#         if is_contour_bad(c) == kwargs.get('shape'):
#             M = cv.moments(c)
#             """算出他的重心"""
#             x = int((M["m10"] / M["m00"]))
#             y = int((M["m01"] / M["m00"]))
#             cv.putText(img, 'clickA', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#             cv.drawContours(img, c, -1, (0, 0, 255), 2)
#             ActionChains(kwargs.get('driver').driver).move_by_offset(x, y).click().perform()
#             ActionChains(kwargs.get('driver').driver).move_by_offset(-x, -y).perform()
#             cv.imwrite('res%s.png' % i, img)
#             # break
