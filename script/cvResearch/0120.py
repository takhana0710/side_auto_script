import cv2 as cv
import imutils
import numpy as np

img = cv.imread('archive/Example-images/Example-images/mini.png')
img_gray = cv.cvtColor(img.copy(),cv.COLOR_BGR2GRAY)
blur_img = cv.medianBlur(img_gray,5)
# _,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
# th3 = cv.adaptiveThreshold(img.copy(),255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
# _,th4 = cv.threshold(blur_img,127,255,cv.THRESH_BINARY)
# th5 = cv.adaptiveThreshold(blur_img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
# th6 = cv.adaptiveThreshold(blur_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
# contours = cv.findContours(th2.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
# contours=imutils.grab_contours(contours)
# mask = np.ones(img.shape[:2],dtype="uint8")*255
cv.imshow('th2',th2)
cv.waitKey(0)