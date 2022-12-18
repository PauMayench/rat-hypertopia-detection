import cv2 as cv
import numpy as np
from functions import printimg
from functions import checkifline
from functions import nomesralla


img = cv.imread(cv.samples.findFile("screen3.png"))
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)


blr = 6
imgb = cv.blur(img, (blr,blr))
printimg("no", imgb)

parametre = 50
ret,img1 = cv.threshold(imgb,parametre,255,cv.THRESH_BINARY)
nomesralla(img1)

while(not checkifline(img1) and parametre < 255 ):

    parametre += 3
    ret,img1 = cv.threshold(imgb,parametre,255,cv.THRESH_BINARY)
    nomesralla(img1)
    #printimg("Parets 1 4",img1)

if (parametre > 255):
        print("F no trobat")
else:
    printimg("si", img1)

#ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
#ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
#titles = ['Original Image','BINARY','TRUNC','TOZERO']
#images = [img, thresh1, thresh3, thresh4]

#for i in range(6):
    #printimg(titles[i], images[i])

