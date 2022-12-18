import cv2 as cv
from functions import printimg
from functions import printimg2
from functions import omplirdesderalla
from functions import nomesralla


img = cv.imread(cv.samples.findFile("screen3.png"))
img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imgb = cv.blur(img, (12,12))


ret,thresh1 = cv.threshold(imgb,80,255,cv.THRESH_BINARY)


nomesralla(thresh1)
while True:
    printimg("original", img)
    printimg("parets 1 i 4", thresh1)


