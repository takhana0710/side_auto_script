import sys
import cv2 as cv
import numpy as np

samples = np.loadtxt('generalsamples.data',np.float32)
responses=np.loadtxt('generalresponses.data',np.float32)
responses=responses.reshape((responses.size,1))
model = cv.ml.KNearest_create()
model.train(samples,cv.ml.ROW_SAMPLE,responses)

def getNum(path):
    im=cv.imread(path)
    out = np.zeros(im.shape,np.uint8)
    gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
    for i in range(gray.__len__()):
        for j in range(gray[0].__len__()):
            if gray[i][j] == 0:
                gray[i][j] = 255
            else:
                gray[i][j] = 0
    thresh = cv.adaptiveThreshold(gray,255,1,1,11,2)
    contours,hierarchy = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    count=0
    numbers = []
    for cnt in contours:
        if cv.contourArea(cnt)>80:
            [x,y,w,h] = cv.boundingRect(cnt)
            if h>25:
                cv.rectangle(im,(x,y),(x+w,x+h),(0,255,0),2)
                roi = thresh[y:y+h,x:x+h]
                roismall = cv.resize(roi,(30,30))
                roismall = roismall.reshape((1,900))
                roismall=np.float32(roismall)
                retval,results,neigh_resp,dists=model.findNearest(roismall,k=1)
                string = str(int((results[0][0])))
                numbers.append(int((results[0][0])))
                cv.putText(out,string,(x,y+h),0,1,(0,255,0))
                count+=1
            if count == 10:
                break
    return numbers,out

numbers,out = getNum('vis/2018102114573260.png')
print(numbers)
cv.imshow('aaa',out)
cv.waitKey(0)