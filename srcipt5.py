import cv2 as cv
from functions import printimg
from functions import printimg2
from functions import omplirdesderalla

img = cv.imread(cv.samples.findFile("screen1.png"))
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imgb = cv.blur(img, (10,10))


ret,thresh3 = cv.threshold(imgb,70,150,cv.THRESH_TOZERO)
ret,thresh1 = cv.threshold(imgb,80,255,cv.THRESH_BINARY)

omplirdesderalla(thresh1)

printimg2(("blur th THRESH_BINARY","blur th TOZERO 70"),(thresh1,thresh3))
