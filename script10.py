import cv2 as cv
from functions import parets_1_4
from functions import printimg
from functions import printimg2

img = cv.imread(cv.samples.findFile("screen1.png"))
imgb = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imgb = cv.blur(imgb, (15,15))

img1 = cv.adaptiveThreshold(imgb,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 12)
#printimg2(("Orgiginal","Parets 1 4"),(img,img1))

while True:
    printimg("original", img)
    printimg("parets", img1)
