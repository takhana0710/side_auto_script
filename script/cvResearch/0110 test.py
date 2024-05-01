import cv2 as cv
import numpy as np

image = cv.imread('vis/test.png')
hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
kernel_2 = np.ones((2,2),np.uint8)#2x2的卷積核
kernel_3 = np.ones((3,3),np.uint8)#3x3的卷積核
kernel_4 = np.ones((4,4),np.uint8)#4x4的卷積核
lower = np.array([24, 34, 46])
upper = np.array([34,255,255])
#mask是把HSV圖片中在顏色範圍內的區域變成白色，其他區域變成黑色
mask = cv.inRange(hsv, lower, upper)
#下面四行是用卷積進行濾波
erosion = cv.erode(mask,kernel_3,iterations = 1)
erosion = cv.erode(erosion,kernel_3,iterations = 1)
dilation = cv.dilate(erosion,kernel_3,iterations = 1)
dilation = cv.dilate(dilation,kernel_3,iterations = 1)
#target是把原圖中的非目標顏色區域去掉剩下的影象
target = cv.bitwise_and(image, image, mask=dilation)
#將濾波後的影象變成二值影象放在binary中
ret, binary = cv.threshold(dilation,127,255,cv.THRESH_BINARY)
#在binary中發現輪廓，輪廓按照面積從小到大排列
contours, hierarchy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
p=0
for i in contours:#遍歷所有的輪廓
    x,y,w,h = cv.boundingRect(i)#將輪廓分解為識別物件的左上角座標和寬、高
    # cv.rectangle(image,(x,y),(x,w,y,h),(0,255,),3)
    print('p=',p,x,y,w,h)
#給識別物件寫上標號
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(image,str(p),(x-10,y-10), font, 1,(0,0,255),2)#加減10是調整字元位置
    p+=1
cv.imshow('target', target)
cv.imshow('Mask', mask)
cv.imshow("prod", dilation)
cv.imshow('Img', image)
# cv2.imwrite('Img.png', Img)
while True:
    Key = chr(cv.waitKey(15) & 255)
    if Key == 'q':
        cv.destroyAllWindows()
        break
