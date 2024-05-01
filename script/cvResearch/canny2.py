import numpy as np
import cv2 as cv
im = cv.imread('vis/test.png')
im = cv.GaussianBlur(im,(3,3),0)
# canny = cv2





lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

if __name__=='__main__':
    im = cv.imread('vis/test.png')
    gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    detected_edges = cv.GaussianBlur(gray,(5,5),0)
    detected_edges = cv.Canny(detected_edges,lowThreshold,255,apertureSize=kernel_size)
    contours,hierarchy = cv.findContours(detected_edges,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    res = cv.drawContours(im.copy(),contours,-1,(0,0,255),3)
    # dst = cv.bitwise_and(im,im,mask=detected_edges)
    cv.imshow('canny',res)
    cv.namedWindow('canny')
    cv.waitKey(0)