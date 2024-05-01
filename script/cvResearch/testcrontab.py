from collections import OrderedDict
import argparse
import imutils
import numpy as np
from scipy.spatial import distance as dict
import cv2 as cv
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

# ap = argparse.ArgumentParser()
# ap.add_argument("-i",'--image',required=True,help="path to the input image")
# args=vars(ap.parse_args())
image = cv.imread('vis/0110t2.png')
resized = imutils.resize(image,width=800)
ratio = image.shape[0]/float(resized.shape[0])
blurred = cv.GaussianBlur(image,(9,9),0)
gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
lab = cv.cvtColor(blurred,cv.COLOR_BGR2Lab)
thresh=cv.threshold(gray,180,255,cv.THRESH_BINARY)[1]
cv.imshow("Thresh",thresh)
cnts = cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# print(cnts)
sd=ShapeDetector()
cl=ColorLabeler()
# cv.imshow("Image",image)
# cv.waitKey(0)
for c in cnts:
    M=cv.moments(c)
    print(M)
    cX = int((M["m10"]/M["m00"]))
    cY=int((M["m01"]/M["m00"]))
    shape = sd.detect(c)
    color = cl.label(lab,c)

    c = c.astype("float")
    # c*=ratio
    c=c.astype("int")
    text = "{} {}".format(color,shape)
    cv.drawContours(image,[c],-1,(0,255,0),2)
    cv.putText(image,text,(cX,cY),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
    cv.imshow("Image",image)
    cv.waitKey(0)



