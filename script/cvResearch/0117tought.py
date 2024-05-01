import numpy as np
import cv2 as cv
def auto_Canny(blurred,sigma=0.33):
    v=np.median(blurred)
    lower = int(max(0,(1.0-sigma)*v))
    upper = int(min(0,(1.0+sigma)*v))
    edged = cv.Canny(blurred,lower,upper)
    return edged
image = cv.imread('vis/0110t2.png')
output = image.copy()
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray,(5,5),0)
# auto = cv.threshold(gray,127,255,cv.THRESH_BINARY)
auto = auto_Canny(blurred)
# contours,hierarchy=cv.findContours(auto,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
circles = cv.HoughCircles(auto,cv.HOUGH_GRADIENT,1.2,100)
# print(circles)
if circles is not None:
    circles = np.round(circles[0,]).astype("int")
    for (x,y,r) in circles:
        cv.circle(output,(x,y),r,(0,255,0),4)
        cv.rectangle(output,(x-5,y-5),(x+5,y+5),(0,212,255),-1)
        cv.imshow("circles",auto)
        cv.imshow("output",np.hstack([image,output]))
cv.waitKey(0)