import numpy as np
import imutils
import cv2 as cv
def is_contour_bad(c):
    peri = cv.arcLength(c,True)
    approx = cv.approxPolyDP(c,0.04*peri,True)
    print(len(approx))
    return  len(approx) == 6 or len(approx)==7
def auto_Canny(blurred,sigma=0.33):
    v=np.median(blurred)
    lower = int(max(0,(1.0-sigma)*v))
    upper = int(min(0,(1.0+sigma)*v))
    edged = cv.Canny(blurred,lower,upper)
    return edged
image = cv.imread('archive/Example-images/Example-images/test0117.png')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
edged = auto_Canny(gray)
cnts = cv.findContours(edged.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
mask = np.ones(image.shape[:2],dtype="uint8")*255
for c in cnts:
    if is_contour_bad(c):
        cv.drawContours(mask,[c],-1,0,-1)
image=cv.bitwise_and(image,image,mask=mask)
cv.imshow("mask",mask)
cv.imshow("res",image)
cv.waitKey(0)