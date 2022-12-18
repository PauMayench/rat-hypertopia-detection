import cv2 as cv
from functions import printimg
import numpy as np
from functions import checkifline
from functions import nomesralla
from functions import printimg2
from functions import netejar_foto

from functions import paret_dins


img = cv.imread(cv.samples.findFile("screen4.png"))
paretsdins = paret_dins(img)




while True:
    printimg("a",paretsdins)
    printimg("a",img)
#printimg2(("Orgiginal","paretsdins","si"),(img,paretsdins, paretsdins2))


#ret,paretsfora = cv.threshold(imgb1,75,255,cv.THRESH_BINARY)
#printimg("a",paretsfora)
#paretsfora = netejar_foto(paretsfora, 5)
#printimg("a",paretsfora)
#paretsfora = nomesralla(paretsfora)
#printimg("a",paretsfora)
