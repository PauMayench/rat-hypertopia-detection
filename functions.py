import cv2 as cv
import numpy as np
from copy import deepcopy

def printimg(nom,img):

    cv.imshow(nom,img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def printimg2(noms,imgs):

    for i in range(len(noms)):
        cv.imshow(noms[i],imgs[i])

    cv.waitKey(0)
    cv.destroyAllWindows()


def omplirdesderalla(img):
    len2 = int(len(img) / 2)

    for y in range(len(img[0])):
        b = False
        for a in range(len2):
            x = (len2) - a
            if(not b and img[x][y] > 250): b = True
            if(b): img[x][y] = 255

    for y in range(len(img[0])):
        b = False
        for a in range(len2):
            x = (len2) + a
            if(not b and img[x][y] > 250): b = True
            if(b): img[x][y] = 255
    return

def nomesralla(img2):
    img = deepcopy(img2)
    len2 = int(len(img) / 2)

    for y in range(len(img[0])):
        b = False
        for a in range(len2):
            x = (len2) - a - 1
            if(not b and img[x][y] > 250):
                b = True
            elif(b): img[x][y] = 0

    for y in range(len(img[0])):
        b = False
        for a in range(len2):
            x = (len2) + a
            if(not b and img[x][y] > 250):
                b = True
            elif(b): img[x][y] = 0

    return img

def checkifnext(img, x, y):
    #print("dins2")
    for x2 in range(-5,5):
        #print("checking x:" , x + x2, "y: ", y, "val: ", x+x2 < len(img),  x+x2 > 0 , y + 1 < len(img[0]), img[x + x2][y + 1 ])
        if(x+x2 < len(img) and x+x2 > 0 and y < len(img[0]) and img[x + x2][y + 1 ] > 200):
            return True

    #print("ill return false")
    return False


def checkifline(img):
    #print("dins 1", )
    x = findxup(img, 0)
    y = 0
    while( y + 1 < len(img[0])):
        x = findxup(img, y)
        if(not checkifnext(img, x, y)):
            return False

        y += 1

    x = findxdown(img, 0)
    y = 0
    while( y + 1 < len(img[0])):
        x = findxdown(img, y)
        if(not checkifnext(img, x, y)):
            return False

        y += 1
    return True




def findxup(img, y):

    x = 0
    while(x < len(img) and img[x][y] < 250 ):
        x += 1
    return x


def findxdown(img, y):

    x = len(img) -1
    while( x > 0 and img[x][y] < 250 ):
        x -= 1
    return x

def parets_1_4(img): #parametre: imatge original, retorna una imatge amb les dos parets ( 1 i 4)

    img3 = cv.cvtColor(img,cv.COLOR_RGB2GRAY)

    #for blr in range(12,15):
        #print("for blr", blr)

        #imgb = cv.blur(img3, (blr,blr))


        #parametre = 50
        #ret,img1 = cv.threshold(imgb,parametre,255,cv.THRESH_BINARY)
        #img1 = nomesralla(img1)

        #while(not checkifline(img1) and parametre < 150 ):
            ##print("param = ", parametre)
            #parametre += 5
            #ret,img1 = cv.threshold(imgb,parametre,255,cv.THRESH_BINARY)
            #nomesralla(img1)
            #print(parametre)
            ##printimg(str(parametre), img1)

        #if (checkifline(img1) ):
            #return img1
        #else:
            #print("not trobat", blr)

    for blr in range(10,20):
        print("for blr", blr)

        imgb = cv.blur(img3, (blr,blr))


        parametre = 50
        ret,img1 = cv.threshold(imgb,parametre,255,cv.THRESH_BINARY)
        img1 = nomesralla(img1)

        while(not checkifline(img1) and parametre < 200 ):
            #print("param = ", parametre)
            parametre += 3
            ret,img1 = cv.threshold(imgb,parametre,255,cv.THRESH_BINARY)
            #img1 = cv.adaptiveThreshold(imgb,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, parametre, 4)
            nomesralla(img1)
            printimg(str(parametre), img1)

        if (parametre < 210):
            return img1
        else:
            print("not trobat", blr)

    return img1

def valid(img, x,y):
    if(x > 0 and x < len(img) and y > 0 and x < len(img[0])):
        return True
    return False

def notinlist(x,y,vis):
    if [x,y] in vis:
        return False
    return True


def es_grup_mes_gran(img, y ,x, n_elem):
    llist = [[x,y]]
    vis = [[x,y]]

    while(len(llist) + len(vis) < n_elem and len(llist) != 0):

        if (notinlist(llist[0][0] -1,  llist[0][1], vis) and valid(llist[0][0] -1,  llist[0][1]) and img[llist[0][0]-1, llist[0][1]] > 250): llist.append([llist[0][0]-1, llist[0][1]])
        if (notinlist(llist[0][0] +1,  llist[0][1], vis) and valid(llist[0][0] +1,  llist[0][1]) and img[llist[0][0]+1, llist[0][1]] > 250): llist.append([llist[0][0]+1, llist[0][1]])
        if (notinlist(llist[0][0] ,  llist[0][1] +1, vis) and valid(llist[0][0],  llist[0][1] + 1) and img[llist[0][0], llist[0][1] +1] > 250): llist.append([llist[0][0], llist[0][1] + 1])
        if (notinlist(llist[0][0] ,  llist[0][1] -1, vis) and valid(llist[0][0],  llist[0][1] - 1) and img[llist[0][0], llist[0][1] -1] > 250): llist.append([llist[0][0], llist[0][1] - 1])
        if (notinlist(llist[0][0] -1,  llist[0][1]-1, vis) and valid(llist[0][0] -1,  llist[0][1] - 1) and img[llist[0][0]-1 , llist[0][1] -1] > 250): llist.append([llist[0][0]-1, llist[0][1] - 1])
        if (notinlist(llist[0][0] +1,  llist[0][1]-1, vis) and valid(llist[0][0] +1,  llist[0][1] - 1) and img[llist[0][0]+1 , llist[0][1] -1] > 250): llist.append([llist[0][0]+1, llist[0][1] - 1])
        if (notinlist(llist[0][0] -1,  llist[0][1]+1, vis) and valid(llist[0][0] -1,  llist[0][1] + 1) and img[llist[0][0]-1 , llist[0][1] +1] > 250): llist.append([llist[0][0]-1, llist[0][1] + 1])
        if (notinlist(llist[0][0] +1,  llist[0][1]+1, vis) and valid(llist[0][0] +1,  llist[0][1] + 1) and img[llist[0][0]+1 , llist[0][1] +1] > 250): llist.append([llist[0][0]+1, llist[0][1] + 1])

        vis.append([llist[0][0], llist[0][1]])




    if(len(llist) == 0):
        return True

    return False



def buscar_cami(imatge, imatge_objectiu, x, y, intensitat, count): # Retorna true si el pixel esta conectat a la part superior o inferior de la foto. Li entra una imatge amb edge detection feta (COUNT HA DE COMENÇAR COM A 0)
	if (y < len(imatge)*0.1 or y > len(imatge)*0.9):
		return True

	for yy in range(intensitat):
		for xx in range(intensitat):
			if (int(y-intensitat/2 + yy) < len(imatge) and int(x-intensitat/2 + xx) < len(imatge[0]) and imatge_objectiu[int(y-intensitat/2 + yy)][int(x-intensitat/2 + xx)] == 255):
				return True
	return False


def netejar_foto(imatge, intensitat): # Entra imatge amb edge detection i torna la imatge amb els pixels que comuniquen amb la part superior o inferior
	imatge_final = deepcopy(imatge)
	for y in range(len(imatge_final)): # Posar tots els pixels a negre
		for x in range(len(imatge_final[0])):
			imatge_final[y][x] = 0

	count = 0
	canvi = True
	while (canvi):
		canvi = False
		for y in range(int(len(imatge)/2)): # Mirar si cada pixel pertany a una illa o no (d'adalt fins la meitat)
			for x in range(len(imatge[0])):
				if (imatge[y][x] == 255 and buscar_cami(imatge, imatge_final, x, y, intensitat, 0)):
					if (imatge_final[y][x] != 255):
						canvi = True
					imatge_final[y][x] = 255

		for y in range(len(imatge)-1, int(len(imatge)/2), -1): # Mirar si cada pixel pertany a una illa o no (d'abaix fins la meitat)
			for x in range(len(imatge[0])):
				if (imatge[y][x] == 255 and buscar_cami(imatge, imatge_final, x, y, intensitat, 0)):
					if (imatge_final[y][x] != 255):
						canvi = True
					imatge_final[y][x] = 255


		print(count)
		count += 1

	return imatge_final

def paret_dins(img):

    img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    imgb2 = cv.blur(img, (20,5))
    printimg("imgb2",imgb2)

    ret,paretsdins = cv.threshold(imgb2,25,255,cv.THRESH_BINARY)
    #paretsdins = cv.adaptiveThreshold(imgb2,200,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 111, 12)
    printimg("imgb2",paretsdins)
    paretsdins = netejar_foto(paretsdins, 5)
    paretsdins = nomesralla(paretsdins)
    return paretsdins

def nbits(img, nomimg, particions2, freq):
    particions = deepcopy(particions2)
    img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    ret,img = cv.threshold(img,25,255,cv.THRESH_BINARY)
    imgb = cv.blur(img, (5,5))
    x = int(len(img)*0.80)
    y = 0
    print("dins")
    y2 = 0
    if(freq == 0):
        while(y < len(img[0]) and imgb[x][y] < 240):
            y += 1
        y2 = y + 10
        #print("primer w")
        while(y2 < len(img[0]) and imgb[x][y2] < 240):
            y2 += 1
        particions.append([nomimg, y, y2])
        freq = y2 - y


    #print("sefons w")

    y = y2
    print("dins w3", y)
    while(y < len(img[0]) and imgb[x][y] < 240):
            y += 1

    #print("w")

    while(y < len(img[0])):
        y = y2
        y2 = y +10
        while(y2 < len(img[0]) and imgb[x][y2] < 240):
            y2 += 1

        if ( y2 < len(img[0]) and y2 - y > freq - 50 and y2 - y < freq + 50 ):
            particions.append([nomimg, y, y2])
           # print(particions)

    #print(particions)
    return particions, freq

def juntar(img1,img2):
    img = deepcopy(img1)
    for x in range(len(img1)):
        for y in range(len(img1[0])):
            if(img2[x][y] > 240):
                img[x][y] = 255
    #printimg("juntar",img)
    return img

#def juntar(img1,img2,yy,yy2):

    #for x in range(len(img1)):
        #for y in range(yy,yy2):
            #if(img2[x][y] == 250):
                #img1[x][y] = 250

    #return img1

def maximin23(imgname, yi, yf):
    img = cv.imread(cv.samples.findFile(imgname))
    img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    imgb = cv.blur(img, (15,10))
    ret,img = cv.threshold(img,25,255,cv.THRESH_BINARY)
    paretsdins = netejar_foto(paretsdins, 5)
    paretsdins = nomesralla(paretsdins)

    return maxx, minn


def maximin14(imgname, yi, yf):

    #funcio del xavi max i min
    return maxx, minn

def avgmaximinx(particions,p1,p2,p3,p4):

    imgname = "a"
    for i in range(len(particions)):
        if(particions[i][0] != imgname):
            imgname = particions[i][0]
            img = cv.imread(cv.samples.findFile(imgname))
            img = img[0:int(0.7*len(img))  ,0:len(img[0]) - 1 ]
            img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)

            imgb1 = cv.blur(img, (10,10))

            ret,paret2 = cv.threshold(imgb1,p2,255,cv.THRESH_BINARY)

            #paret2 = netejar_foto(paret2, 10)
            paret2 = nomesralladalt(paret2)
            #printimg("p2",paret2)
            ret,paret3 = cv.threshold(imgb1,p3,255,cv.THRESH_BINARY)
            #printimg("paretsdins",paretsdins)
            paret3 = netejar_foto(paret3, 10)
            paret3 = nomesrallabaix(paret3)
            #printimg("p3",paret3)
            paretsdins = juntar(paret2,paret3)
            #printimg("paretsdins",paretsdins)

            imgb2 = cv.blur(img, (10,10))
            ret,paret1 = cv.threshold(imgb2,p1,255,cv.THRESH_BINARY)
            paret1= nomesralladalt(paret1)
            #printimg("p1",paret1)
            ret,paret4 = cv.threshold(imgb2,p4,255,cv.THRESH_BINARY)
            paret4 = nomesrallabaix(paret4)
            #printimg("p4",paret4)
            paretsfora = juntar(paret1,paret4)

            imgparets = juntar(paretsdins,paretsfora)#,particions[i][1],particions[i][2])
#            printimg2(("originsl","4parets","pfora", "pdins"),(img,imgparets,paretsfora,paretsdins))
            printimg2(("originsl","4parets"),(img,imgparets))

 #funcio del xavi max i min
        maxx += maxxx
        minn += minnn

    return maxx/len(particions), minn/len(particions)

def nomesralladalt(img2):
    img = deepcopy(img2)
    len2 = int(len(img) / 2)

    for y in range(len(img[0])):
        b = False
        for a in range(len2):
            x = (len2) - a - 1
            if(not b and img[x][y] > 250):
                b = True
            elif(b): img[x][y] = 0

    for y in range(len(img[0])):
        b = False
        for a in range(len2):
            x = (len2) + a
            img[x][y] = 0

    return img

def nomesrallabaix(img2):
    img = deepcopy(img2)
    len2 = int(len(img) / 2)
    for y in range(len(img[0])):
        b = False
        for a in range(len2):
            x = (len2) - a - 1
            img[x][y] = 0

    for y in range(len(img[0])):
        b = False
        for a in range(len2):
            x = (len2) + a
            if(not b and img[x][y] > 250):
                b = True
            elif(b): img[x][y] = 0

    return img
