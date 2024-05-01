import imutils
import numpy as np
import cv2 as cv
from imutils.object_detection import non_max_suppression
import pytesseract
from matplotlib import pyplot as plt

"""基於ＥＡＳＴ模型訓練的範例"""
args = {"image":"archive/example-images/Example-images/SCtest2.png",
        "east":"archive/east_text_detection.pb",
        "min_confidence":0.5, "width":320, "height":320}
image = cv.imread(args['image'])

orig=image.copy()
(origH,origW) = image.shape[:2]
(newW,newH) = (args['width'],args['height'])

rW=origW/float(newW)
rH=origH/float(newH)
image  = cv.resize(image,(newW,newH))
(H,W) = image.shape[:2]
blob = cv.dnn.blobFromImage(image,1.0,(W,H),(123.68,116.78,103.94),swapRB=True,crop=False) #圖片讀取預處理
net = cv.dnn.readNet(args['east'])
layerNames = ["feature_fusion/Conv_7/Sigmoid","feature_fusion/concat_3"]
net.setInput(blob)
(scores,geometry) = net.forward(layerNames)
def predictions(prob_score,geo):
    (numR,numC) = prob_score.shape[2:4]
    boxes  = []
    confidence_val =[]
    for y in range(0,numR):
        scoresData = prob_score[0,0,y]
        x0=geo[0,0,y]
        x1=geo[0,1,y]
        x2=geo[0,2,y]
        x3=geo[0,3,y]
        anglesData = geo[0,4,y]
        for i in range(0,numC):
            if scoresData[i] < args['min_confidence']:
                continue
            (offX,offY)=(i*4.0,y*4.0)
            angle = anglesData[i]
            cos=np.cos(angle)
            sin=np.sin(angle)
            h=x0[i]+x2[i]
            w=x1[i]+x3[i]
            endX=int(offX+(cos*x1[i])+(sin*x2[i]))
            endY=int(offY-(sin*x1[i])+(cos*x2[i]))
            startX=int(endX-w)
            startY = int(endY-h)
            boxes.append((startX,startY,endX,endY))
            confidence_val.append(scoresData[i])
    return (boxes,confidence_val)

(boxes,confidence_val) = predictions(scores,geometry)

boxes = non_max_suppression(np.array(boxes),probs=confidence_val)
results = []

for(startX,startY,endX,endY) in boxes:
    startX= int(startX*rW)
    startY =int(startY*rH)
    endX = int(endX*rW)
    endY = int(endY*rH)
    r=orig[startY:endY,startX:endX]
    configuration = ('-l eng --oem 1 --psm 8')
    text = pytesseract.image_to_string(r,config=configuration)
    results.append(((startX,startY,endX,endY),text))

orig_image = orig.copy()

for ((start_X, start_Y, end_X, end_Y), text) in results:
    print('{}\n'.format(text))
    text = "".join([x if ord(x) < 128 else "" for x in text]).strip()
    cv.rectangle(orig_image,(start_X,start_Y),(end_X,end_Y),(0,0,255),2)
    cv.putText(orig_image,text,(start_X,start_Y-30),cv.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
plt.imshow(orig_image)
plt.title('OutPut')
plt.show()