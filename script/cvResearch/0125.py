import cv2 as cv
import numpy as np

img = cv.imread('vis/0110.png')
img2 = cv.GaussianBlur(img.copy(), (15, 15), 0)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
thresh = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.imshow('ddnorm', thresh)
print(len(contours))
contours = sorted(contours, key=cv.contourArea, reverse=True)
print(len(contours))
contours = list(filter(lambda x: cv.contourArea(x) > 100.0, contours))
print(len(contours))
for cnt in contours:
    print(cv.contourArea(cnt))
    [x, y, w, h] = cv.boundingRect(cnt)
    print('width={width},height={height}'.format(width=w, height=h))
    cv.rectangle(thresh, (x, y), (x + w, y + h), (0, 0, 255), 2)
    roi = thresh[y:y + h, x:x + w]
    roismall = cv.resize(roi, (300, 300))
    cv.imshow('norm', thresh)
    key = cv.waitKey(0)
cv.imshow("first", thresh)
cv.waitKey(0)
