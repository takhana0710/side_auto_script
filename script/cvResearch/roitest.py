import numpy as np
import cv2 as cv

img = cv.imread('vis/shape.png')
img1 = cv.resize(img,(600,400))
cv.imshow("Original",img1)

roi = np.zeros(img1.shape,np.uint8)
contour = np.array([(30,30),(300,30),(200,300)])
cv.drawContours(roi,[contour],0,(0,0,255),thickness=cv.FILLED)
cv.imshow('roi',roi)
res = cv. bitwise_and(img1,roi)
cv.imshow('res',res)
cv.waitKey(0)
cv.destroyAllWindows()