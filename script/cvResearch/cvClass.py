import cv2 as cv
import numpy as np
class CvFunc():
    def __init__(self,path):
        self.image = cv.imread(path)
    def kernel(self,k):
        """卷積核"""
        return np.ones((k,k),np.uint8)
    def erosion(self,**kwargs):
        """影像腐蝕"""
        return cv.erode(kwargs.get('image'),kernel=kwargs.get('kernel'),iterations=1)
    def dilation(self,**kwargs):
        """影像膨脹"""
        return cv.dilate(kwargs.get('image'),kernel=kwargs.get('kernel'),iterations=1)
    def bitwiseAnd(self,**kwargs):
        """圖像掩膜"""
        return cv.bitwise_and(kwargs.get('image'), kwargs.get('image'), mask=kwargs.get('mask'))
    def threshold(self,**kwargs):
        """影像二值化"""
        ret,binary = cv.threshold(kwargs.get('image'), 127, 255, cv.THRESH_BINARY)
        return binary
    def findContours(self,**kwargs):
        """尋找圖形在二值化之後"""
        return cv.findContours(kwargs.get('binary'),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    def boundingRect(self,**kwargs):
        """解析區塊資訊回傳 x y w h"""
        return cv.boundingRect(kwargs.get('image'))
    
        