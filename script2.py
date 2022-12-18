import cv2 as cv

img = cv.imread(cv.samples.findFile("screen1.png"))
cv.imshow("original",img)

img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
imgb = cv.blur(img, (10,10))

_, result = cv.threshold(imgb, 80, 255, cv.THRESH_BINARY)
_, trunc = cv.threshold(imgb, 80, 255, cv.TRUNCATE)




cv.imshow("staticThreshold",result)
cv.imshow("staticThreshold",trunc)


cv.waitKey(0)
cv.destroyAllWindows()
