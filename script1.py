import cv2 as cv

img = cv.imread(cv.samples.findFile("screen1.png"))
cv.imshow("original",img)

img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow("blancinegre",img)

_, result = cv.threshold(img, 60, 255, cv.THRESH_BINARY) #115 per a detectar (les parets exetriors


cv.imshow("staticThreshold",result)


cv.waitKey(0)

cv.destroyAllWindows()
