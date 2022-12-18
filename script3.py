import cv2 as cv
from functions import printimg
import numpy as np
from functions import checkifline
from functions import nomesralla
from functions import printimg2

img = cv.imread(cv.samples.findFile("screen5.png"))
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imgb = cv.blur(img, (30,15))

printimg("si",imgb)


for i in range(0,160,10):

    ret,thresh1 = cv.threshold(imgb,i,200,cv.THRESH_BINARY)
    #print(checkifline(thresh1))

    #thresh2 = nomesralla(thresh1)
    printimg2(("Orgiginal",str(i)),(img,thresh1,))


#ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
#ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
#titles = ['Original Image','BINARY','TRUNC','TOZERO']
#images = [img, thresh1, thresh3, thresh4]

#for i in range(6):
    #printimg(titles[i], images[i])

