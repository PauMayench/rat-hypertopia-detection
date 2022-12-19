#necessites functions.py
#Aquest script necessita coma parametres els noms dels fitxers(imatges amb el bpm) elBPM l'escala*100 i 4 valors que son la sensitivitat de detectar cada paret
#la imatge ha d'estar tallada com la del sample1 o sample2

#ex: python3 script11.py sample1.png sample2.png bpm escala*100 80 25 20 80
# normalment aquests valors oscilen entre: (60-90, 10-30, 10-30, 60-90)


import cv2 as cv
from functions import parets_1_4
from functions import printimg
from functions import printimg2
from functions import nbits
from functions import avgmaximinlong
import sys
from funcions2 import comprovar_si_cor_sa

if(len(sys.argv) < 6):
    print("Usage: python3 script11.py sample1.png sample2.png bpm escala*100 p1 p2 p3 p4")
    print("p1 = (60,80), p2 = (10,30), p3 = (10,30), p4 = (60.80)")
    exit(1)

particions = []
freq = 0
for i in range(1,(len(sys.argv)-6)):
    img = cv.imread(cv.samples.findFile(str(sys.argv[i])))

    particions, freq = nbits(img,sys.argv[i], particions , freq)

    print(particions)

resultat = avgmaximinlong(particions,int(sys.argv[len(sys.argv)-5]),int(sys.argv[len(sys.argv)-4]),int(sys.argv[len(sys.argv)-3]),int(sys.argv[len(sys.argv)-2]),int(sys.argv[len(sys.argv)-1]))
comprovar_si_cor_sa(resultat, "long", int(sys.argv[len(sys.argv)-6]))

#falta tallar la foto on toca
#falta cridar funcio calcula si el cor es sa o no


print("acaba l'execucio")

