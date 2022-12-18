#necessites functions.py
#Aquest script necessita coma parametres els noms dels fitxers (imatges amb el bpm) i 4 valors que son la sensitivitat de detectar cada paret
#ex: python3 script11.py sample1.png sample2.png 80 25 20 80
# normalment aquests valors oscilen entre: (60-90, 10-30, 10-30, 60-90)


import cv2 as cv
from functions import parets_1_4
from functions import printimg
from functions import printimg2
from functions import nbits
from functions import avgmaximinx
import sys



particions = []
freq = 0
for i in range(1,(len(sys.argv)-4)):
    img = cv.imread(cv.samples.findFile(str(sys.argv[i])))

    particions, freq = nbits(img,sys.argv[i], particions , freq)

    print(particions)

avgmaximinx(particions,int(sys.argv[len(sys.argv)-4]),int(sys.argv[len(sys.argv)-3]),int(sys.argv[len(sys.argv)-2]),int(sys.argv[len(sys.argv)-1]))




print(nbitstotal)

