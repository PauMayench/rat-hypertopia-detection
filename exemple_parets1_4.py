import cv2 as cv
from functions import parets_1_4
from functions import printimg
from functions import printimg2

img = cv.imread(cv.samples.findFile("screen4.png"))

img1 = parets_1_4(img)

#printimg2(("Orgiginal","Parets 1 4"),(img,img1))

while True:
    printimg("original", img)
    printimg("parets", img1)
