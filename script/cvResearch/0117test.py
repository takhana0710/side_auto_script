import numpy as np
import cv2 as cv
import imutils
"""
今天演算測試
灰階處理＋高斯
邊緣二值化（canny）
檢測所有圖像後才切
單一解析每個才切形狀
"""
def auto_Canny(blurred,sigma=0.33):
    v=np.median(blurred)
    lower = int(max(0,(1.0-sigma)*v))
    upper = int(min(0,(1.0+sigma)*v))
    edged = cv.Canny(blurred,lower,upper)
    return edged

def ShapeDetector(c):
    shape = "unidentified"
    peri = cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, 0.4 * peri, True)
    if len(approx) == 3:
        shape = "triangle"
    elif len(approx) == 4:
        (x, y, w, h) = cv.boundingRect(approx)
        ar = w / float(h)
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
    elif len(approx) == 5:
        shape = "pentagon"
    else:
        shape = "circle"
    return shape


img = cv.imread('archive/Example-images/Example-images/mini.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray,(5,5),0)
auto = cv.adaptiveThreshold(blurred,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
cnts = cv.findContours(auto.copy(),cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts=sorted(cnts,key=cv.contourArea,reverse=True)[:1]
for i in cnts:
    M = cv.moments(i)
    try:
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))
        sd = ShapeDetector(i)
        print(cX, cY)
        c = i.astype("float")
        c = c.astype("int")
        cv.drawContours(img, [c], -1, (0, 255, 0), 2)
        cv.putText(img, sd, (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    except:
        continue
    cv.imshow("Image", img)
cv.waitKey(0)

