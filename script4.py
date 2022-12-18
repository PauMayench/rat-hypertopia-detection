import cv2 as cv
from functions import printimg
import numpy as np
from functions import omplirdesderalla
from functions import nomesralla
from functions import robustline

img = cv.imread('screen1.png')
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imgb = cv.blur(img, (10,10))

for i in range(0,255,10):
    ret,thresh3 = cv.threshold(imgb,i,250,cv.THRESH_TOZERO)
    nomesralla(thresh3)
    printimg(str(i) ,thresh3)



#ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
#ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
#titles = ['Original Image','BINARY','TRUNC','TOZERO']
#images = [img, thresh1, thresh3, thresh4]

#for i in range(6):
    #printimg(titles[i], images[i])

