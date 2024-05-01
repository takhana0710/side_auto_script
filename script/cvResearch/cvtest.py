import cv2 as cv
import numpy as np

class ShapeAnalysis:
    def __init__(self):
        self.shapes={'triangle':0,'rectangle':0,'polygons':0,'circles':0}
    def analysis(self,frame):
        h,w,ch = frame.shape
        result = np.zeros((h,w,ch),dtype=np.uint8)
        print('start to detect lines ....')
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        cv.imshow("input image",frame)
        contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for cnt in range(len(contours)):
            cv.drawContours(result,contours,cnt,(0,255,0),2)
            epsilon=0.01*cv.arcLength(contours[cnt],True)
            approx=cv.approxPolyDP(contours[cnt],epsilon,True)
            corners = len(approx)
            shape_type=""
            if corners == 3:
                count = self.shapes['triangle']
                count+=1
                self.shapes['triangle'] = count
                shape_type='三角形'
            if corners == 4:
                count = self.shapes['rectangle']
                count = count + 1
                self.shapes['rectangle'] = count
                shape_type = "矩形"
            if corners >= 10:
                count = self.shapes['circles']
                count = count + 1
                self.shapes['circles'] = count
                shape_type = "圆形"
            if 4 < corners < 10:
                count = self.shapes['polygons']
                count = count + 1
                self.shapes['polygons'] = count
                shape_type = "多边形"
            p = cv.arcLength(contours[cnt], True)
            area = cv.contourArea(contours[cnt])
            print("周长: %.3f, 颜色: %s 形状: %s "% (p, area, shape_type))
        cv.imshow("Analysis Result", self.draw_text_info(result))
        cv.imwrite("test-result.png", self.draw_text_info(result))
        return self.shapes
    def draw_text_info(self, image):
        c1 = self.shapes['triangle']
        c2 = self.shapes['rectangle']
        c3 = self.shapes['polygons']
        c4 = self.shapes['circles']
        cv.putText(image, "triangle: "+str(c1), (10, 20), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
        cv.putText(image, "rectangle: " + str(c2), (10, 40), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
        cv.putText(image, "polygons: " + str(c3), (10, 60), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
        cv.putText(image, "circles: " + str(c4), (10, 80), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
        return image


src = cv.imread('vis/shape.png')
obj = ShapeAnalysis()
obj.analysis(src)
cv.waitKey(0)
cv.destroyAllWindows()