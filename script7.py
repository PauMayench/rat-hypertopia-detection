import cv2 as cv
from functions import parets_1_4
from functions import printimg

img = cv.imread(cv.samples.findFile("screen1.png"))

img1 = parets_1_4(img)

printimg("Parets 1 4",img1)
