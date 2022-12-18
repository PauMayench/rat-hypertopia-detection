import cv2 as cv
from functions import printimg
from functions import printimg2
from functions import omplirdesderalla
from functions import nomesralla
from functions import robustline

img = cv.imread(cv.samples.findFile("screen2.png"))
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imgb = cv.blur(img, (10,10))


#ret,thresh3 = cv.threshold(imgb,70,150,cv.THRESH_TOZERO)
ret,thresh1 = cv.threshold(imgb,80,255,cv.THRESH_BINARY)

#omplirdesderalla(thresh1)

nomesralla(thresh1)
printimg("parets 1 i 4!", thresh1)

#robustline(thresh1, 80, imgb)
printimg("parets 1 i 4!", thresh1)
