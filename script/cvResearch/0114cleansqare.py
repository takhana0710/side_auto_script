import cv2 as cv
import numpy as np
from skimage.morphology import skeletonize

def get_skeleton_image(threshold_image):
    skeleton = skeletonize(threshold_image/255)
    skeleton = skeleton.astype(np.uint8)
    skeleton*=255
    return skeleton

image = cv.imread('vis/0110.png')
gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
_,threshold_image = cv.threshold(gray_image,100,255,cv.THRESH_BINARY)
cv.imshow("threshold_image",threshold_image)
kernel = cv.getStructuringElement(cv.MORPH_CROSS,(3,3))
dilate_image = cv.dilate(threshold_image,kernel=kernel,iterations=2)
erode_image = cv.erode(dilate_image,kernel=kernel,iterations=1)
cv.imshow("erode_image",erode_image)

contours,hierarchy = cv.findContours(erode_image,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
max_cnt = max(contours,key=lambda x:cv.arcLength(x,closed=True))
max_cnt_image=np.zeros_like(erode_image)
cv.drawContours(max_cnt_image,[max_cnt],-1,255,-1)
cv.imshow("max_cnt_image",max_cnt_image)
skeleton_image=get_skeleton_image(max_cnt_image)
cv.imshow('skeleton_image',skeleton_image)
cv.waitKey(0)