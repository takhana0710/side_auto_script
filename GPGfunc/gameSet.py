import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def centroid(moments):
    """根据图像矩计算质心"""
    x_centroid = round(moments['m10'] / moments['m00'])
    y_centroid = round(moments['m01'] / moments['m00'])
    return x_centroid, y_centroid
def is_contour_bad(c):
    peri = cv.arcLength(c, True)#周長
    approx = cv.approxPolyDP(c, 0.04 * peri, True)#多邊形判定
    print('面積',cv.contourArea(c))
    print('點',len(approx))
    return len(approx)

filename = 'ifun.png'
ksize = 3
img = cv.imread(filename)
img2 = img.copy()
v = np.median(img2)
lower = int(max(0, (1.0 - 0.33) * v))
upper = int(min(255, (1.0 + 0.33) * v))
print(lower,upper)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
img2 = cv.GaussianBlur(img2, (ksize, ksize), 0)
thresh = cv.Canny(img2, lower, upper, cv.THRESH_BINARY)  # 閥值二值化
cnts, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv.contourArea, reverse=True) # 排序取出最大的前5個
cv.imwrite('aaa.png', thresh)
print(len(cnts))
for i,c in enumerate(cnts):
    is_contour_bad(c)
    # if is_contour_bad(c) == 4:
    M = cv.moments(c)
    # if M['m00'] == 0:
    #     continue
    
    """算出他的重心"""
    x = int((M["m10"] / M["m00"]))
    y = int((M["m01"] / M["m00"]))
    # x, y = centroid(M)
    cv.putText(img, 'clickA', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    print(str(x)+','+str(y))
    if i%2==0:
        cv.drawContours(img, c, -1, (0, 0, 255), 2)
    else:
        cv.drawContours(img, c, -1, (0, 255, 0), 1)
    cv.imshow('show', img)
    cv.waitKey()