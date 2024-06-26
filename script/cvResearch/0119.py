import sys
import numpy as np
import cv2 as cv

im=cv.imread('vis/2018102114573260.png')
im3 = im.copy()

gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
thresh= cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
contours,hierarchy  = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
samples = np.empty((0,900))
responses = []
keys = [i for i in range(48,58)]
count=0
for cnt in contours:
    if cv.contourArea(cnt)>80:
        [x,y,w,h] = cv.boundingRect(cnt)
        if h>25 and h<30:
            count+=1
            cv.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv.resize(roi,(30,30))
            cv.imshow('norm',im)
            key = cv.waitKey(0)
            print(key)
            if key == 27:
                sys.exit()
            elif key in keys:
                responses.append(int(chr(key)))
                sample = roismall.reshape((1,900))
                samples=np.append(samples,sample,0)
            if count == 100:
                break
responses = np.array(responses,np.float32)
responses = responses.reshape((responses.size,1))
print("training complete")

np.savetxt('generalsamples.data',samples)
np.savetxt('generalresponses.data',responses)

cv.waitKey(0)
cv.destroyAllWindows()