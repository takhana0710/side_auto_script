import numpy as np
import cv2

def resize(image,width=None,height=None,inter=cv2.INTER_AREA):
    dim=None
    (h,w)=image.shape[:2]
    if width == None:
        r=height/float(h)
        dim=(int(w*r),height)
    else:
        r=width/float(w)
        dim=(width,int(h*r))
    resized=cv2.resize(image,dim,interpolation=inter)
    return resized


def order_points(pts):
    rect=np.zeros((4,2),dtype='float32')
    s=pts.sum(axis=1)
    print(s)
    rect[0]=pts[np.argmin(s)]
    rect[2]=pts[np.argmax(s)]
    diff = np.diff(pts,axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[2] = pts[np.argmax(diff)]
    return rect

# def four_point_transform(image,pts):
#     rect=order_points(pts)
#     (tl,tr,br,bl) = rect
#     widthA = np.sqrt(((br[0]-bl[0])**2)+((br[1]-bl[1])**2))
#     widthB = np.sqrt(((tr[0]-tl[0])**2)+((tr[1]-tl[1])**2))
#     maxWidth = max(int(widthA),int(widthB))
#     heightA = np.sqrt(((tr[0]-br[0])**2)+((tr[1]-br[1])**2))
#     heightB = np.sqrt(((tl[0]-bl[0])**2)+((tl[1]-bl[1])**2))
#     maxHeight = max(int(heightA),int(heightB))
#     dst = np.array([[0,0],[maxWidth-1,maxHeight-1],[0,maxHeight-1],],dtype='float32')
#     M=cv2.getPerspectiveTransform(rect,dst)
#     warped = cv2.warpPerspective(image,M,(maxWidth,maxHeight))
#     return warped
#
# def get_image_processingResult():
#     img_path=''
#     orig,ratio,secreenCnt = edged_detection(img_path)

image = cv2.imread('vis/test.png')
ratio = image.shape[0]/500.0
orig = image.copy()
image=resize(orig,height=500)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(gray,75,255)
print("STEP1:邊緣檢測")
cnts = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts,key = cv2.contourArea,reverse=True)[:5] # 排序取出最大的前5個
# screenCnt=np.empty(shape=5)
for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.1*peri,True)# 輪廓近似
    print(len(approx))
    screenCnt = approx
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("OutLine", image)
    # cv2.imshow("Image",image)
    cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
    # if len(approx) ==4:
    #     screenCnt = approx
print("STEP2:獲取輪廓")