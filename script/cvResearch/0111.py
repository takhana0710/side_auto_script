import cv2 as cv
import numpy as np
import imutils
from scipy.spatial import distance as dict
from collections import OrderedDict
class ShapeDetector: # 輪廓檢測
    def detect(self,c):
        shape = "unidentified"
        peri = cv.arcLength(c,True)
        approx = cv.approxPolyDP(c,0.04*peri,True)
        if len(approx) == 3:
            shape="triangle"
        elif len(approx) == 4:
            (x,y,w,h) = cv.boundingRect(approx)
            ar = w/float(h)
            shape = "square" if ar >= 0.95 and ar<=1.05 else "rectangle"
        elif len(approx) == 5:
            shape="pentagon"
        else:
            shape = "circle"
        return shape

class ColorLabeler:
    def __init__(self):
        colors = OrderedDict({
            "red":(255,0,0),
            "green":(0,255,0),
            "blue":(0,0,255)
        })
        self.lab=np.zeros((len(colors),1,3),dtype="uint8")
        self.colorNames = []
        for (i,(name,rgb)) in enumerate(colors.items()):
            self.lab[i] = rgb
            self.colorNames.append(name)
        self.lab = cv.cvtColor(self.lab,cv.COLOR_RGB2Lab)
    def label(self,image,c):
        mask=np.zeros(image.shape[:2],dtype="uint8")
        cv.drawContours(mask,[c],-1,-255,-1)
        mask = cv.erode(mask,None,iterations=2)
        mean= cv.mean(image,mask=mask)[:3]
        minDist = (np.inf,None)
        for (i,row) in enumerate(self.lab):
            d=dict.euclidean(row[0],mean)
            if d<minDist[0]:
                minDist=(d,1)
        return self.colorNames[minDist[1]]

def color(image):
    lower = np.array([0,0,221],dtype='uint8')
    upper = np.array([180,30,255],dtype='uint8')# 過濾白色
    mask=cv.inRange(image,lower,upper)
    output = cv.bitwise_and(image,image,mask=mask)
    # cv.imshow("image",np.hstack([image,output]))
    # cv.waitKey(0)
    output = cv.cvtColor(output,cv.COLOR_HSV2BGR)
    return output

def shape():
    pass

image = cv.imread('vis/test.png')
image = cv.cvtColor(image,cv.COLOR_BGR2HSV)
image = color(image) # 先篩選出白色區塊包含開始按鈕
blur = cv.GaussianBlur(image,(5,5),0)
lab = cv.cvtColor(blur,cv.COLOR_BGR2Lab)
gray = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY)[1] #閥值二值化
cnts = cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd=ShapeDetector()
for c in cnts:
    M=cv.moments(c)
    cX = int((M["m10"]/M["m00"]))
    cY=int((M["m01"]/M["m00"]))
    print(cX,cY)
    text = sd.detect(c)
    if text == 'circle':
        c = c.astype("float")
        c=c.astype("int")
        cv.drawContours(image,[c],-1,(0,255,0),2)
        cv.putText(image,text,(cX,cY),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
        cv.imshow("Image",image)
cv.waitKey(0)
