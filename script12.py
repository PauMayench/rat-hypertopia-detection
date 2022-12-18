import cv2 as cv
from functions import parets_1_4
from functions import printimg
from functions import printimg2
from functions import nbits
import sys
from functions import printimg


img = cv.imread(cv.samples.findFile("sample1.png"))
imgb = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imgb = cv.blur(imgb, (15,15))

x = int(len(img)*0.80)

for  y in range(100):
    imgb[y][100] = 255

for  y in range(100):
    imgb[y][415] = 255
printimg("a", imgb)

print(len(img), len(img[0]))

