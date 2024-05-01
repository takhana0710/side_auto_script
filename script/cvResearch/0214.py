import cv2 as cv
import numpy as np
im = cv.imread('aaa.jpg')
im_gray=cv.cvtColor(im,cv.COLOR_BGR2GRAY)
ret,im_inv = cv.threshold(im_gray,127,255,cv.THRESH_BINARY_INV)
kernel = 1/16*np.array([[1,2,1],[2,4,2],[1,2,1]])
im_blur = cv.filter2D(im_inv,-1,kernel)
im_res = cv.threshold(im_blur,127,255,cv.THRESH_BINARY)
im2,contours = cv.findContours(im_res,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

