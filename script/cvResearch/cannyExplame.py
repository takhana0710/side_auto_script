import numpy as np
import argparse
import glob
import cv2
import os


def auto_canny(image,sigma=0.33):
    v=np.median(image)
    lower = int(max(0,(1.0-sigma)*v))
    upper = int(min(255,(1.0+sigma)*v))
    edged = cv2.Canny(image,lower,upper)
    return edged


ap = argparse.ArgumentParser()
ap.add_argument("-i","--images",required=True,help="path to input dataset of image")
args = vars(ap.parse_args())

file_dir = "vis/"
if not os.path.isdir(file_dir):
    os.makedirs(file_dir)

i=0
img_names = glob.glob(args["images"]+"/*.png")
for imagePath in img_names:
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(3,3),0)
    wide =  cv2.Canny(blurred,10,200)
    tight= cv2.Canny(blurred,225,250)
    auto = auto_canny(blurred)
    result = np.hstack([wide,tight,auto])
    i+=1
    save_name = 'upvis/'+str(i)+".png"
    cv2.imshow("Original",image)
    cv2.imshow("Edged",result)
    cv2.imwrite(save_name,result)
    cv2.waitKey(0)
