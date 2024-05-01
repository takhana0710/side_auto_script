import pytesseract
from PIL import Image

img = Image.open(r"archive/example-images/Example-images/SCtest2.png")

print(pytesseract.image_to_string(img,lang='eng'))


