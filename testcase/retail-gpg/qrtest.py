import cv2

img = cv2.imread("test.jpg")

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(img)
print(data)