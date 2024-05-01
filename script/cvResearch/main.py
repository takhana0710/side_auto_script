from PIL import Image
from pytesseract import *
import cv2 as cv
image=cv.imread('login.png',cv.COLOR_RGB2GRAY)
a=image_to_string(image,lang='chi_tra')
print(''.join(a.split()))