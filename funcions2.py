import cv2 as cv
#from funcions import show_foto, pujar_saturacio, netejar_foto, nomesralla
from copy import deepcopy

def calcular_valors(img, x_ini, x_final, tipus, escala): # Resultats es donen com a [IVS, LVID, LVPW] i cada tupla (expansio, reduccio). Type es o "long" o "short". Escala el nombre de unitats que son tota l'altura de la foto


	img2 = deepcopy(img)

	img = img[0:len(img), x_ini:x_final]

	resultat = [[0, len(img)], [0, len(img)], [0, len(img)]]



	for x in range(len(img[0])):
		IVS = 0
		LVID = 0
		LVPW = 0

		y = 0
		y_inicial = y
		count = 0
		while (y < len(img)): # Posar la Y al primer punt
			if img[y][x] == 255:
				#print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
				y_inicial = y
				break

			print("x")
			y += 1
		y+=1

		while (y < len(img)): # Posar la Y al segon punt
			if img[y][x] == 255:
				IVS = y-y_inicial
				y_inicial = y
				break
			y += 1
		y+=1
		while (y < len(img)): # Posar la Y al tercer punt
			if img[y][x] == 255:
				LVID = y-y_inicial
				y_inicial = y
				break
			y += 1
		y+=1
		while (y < len(img)): # Posar la Y al quart punt
			if img[y][x] == 255:
				LVPW = y-y_inicial
				break
			y += 1

		#print(IVS)
		#print(LVID)
		#print(LVPW)

		if (LVID > resultat[1][0]): # Es un nou maxim
			resultat[0][0] = IVS
			resultat[1][0] = LVID
			resultat[2][0] = LVPW

		if (LVID < resultat[1][1]): # Es un nou minim
			resultat[0][1] = IVS
			resultat[1][1] = LVID
			resultat[2][1] = LVPW

	esc = (escala/len(img))/100
	resultat[0][0] = resultat[0][0] * esc
	resultat[1][0] = resultat[1][0] * esc
	resultat[2][0] = resultat[2][0] *esc
	resultat[0][1] = resultat[0][1] * esc
	resultat[1][1] = resultat[1][1] * esc
	resultat[2][1] = resultat[2][1] * esc
	return resultat
	
	# Falta canviar els resultats de pixels a unitats

def comprovar_si_cor_sa(resultat, tipus, HR):



	dolentes = 0 # Nombre de mesures no sanes
	if (tipus == "long"):
		print("IVS;d ", resultat[0][0])
		print("IVS;s ", resultat[0][1])
		print("LVID;d ", resultat[1][0])
		print("LVID;s ", resultat[1][1])
		print("LVPW;d ", resultat[2][0])
		print("LVPW;s ", resultat[2][1])

		if (resultat[0][0] > 0.71+0.15 or resultat[0][0] < 0.71-0.15):
			dolentes += 1
		if (resultat[0][1] > 0.97+0.19 or resultat[0][1] < 0.97-0.19):
			dolentes += 1
		if (resultat[1][0] > 3.69+0.41 or resultat[1][0] < 2.2-0.41):
			dolentes += 1
		if (resultat[1][1] > 2.2+0.5 or resultat[1][1] < 2.2-0.5):
			dolentes += 1
		if (resultat[2][0] > 0.79+0.22 or resultat[2][0] < 0.79-0.22):
			dolentes += 1
		if (resultat[2][1] > 1.12+0.33 or resultat[2][1] < 1.12-0.33):
			dolentes += 1

		LVESV = (7/(2.4+resultat[1][1]))*resultat[1][1]**3
		if (LVESV > 19.35+11.3 or LVESV < 19.35-11.3):
			dolentes += 1
		LVEDV = (7/(2.4+resultat[1][0]))*resultat[1][0]**3
		if (LVEDV > 57.7-16.5 or LVEDV < 57.7-16.5):
			dolentes += 1
		EF = (LVEDV-LVESV)/LVEDV*100
		if (EF > 71+11 or EF < 71-11):
			dolentes += 1
		FS = (resultat[1][0]-resultat[1][1])/resultat[1][0]*100
		if (FS > 43+9 or FS < 43-9):
			dolentes += 1
		SV = LVEDV-LVESV
		if (SV > 35.1-8.5 or SV < 35.1-8.5):
			dolentes += 1
		CO = SV*float(HR)
		if (CO > 17.7+3.8 or CO < 17.7-3.8):
			dolentes += 1

	elif (tipus == "short"):
		print("LVAW;d ", resultat[0][0])
		print("LVAW;s ", resultat[0][1])
		print("LVID;d ", resultat[1][0])
		print("LVID;s ", resultat[1][1])
		print("LVPW;d ", resultat[2][0])
		print("LVPW;s ", resultat[2][1])

		if (resultat[0][0] > 0.71+0.15 or resultat[0][0] < 0.71-0.15):
			dolentes += 1
		if (resultat[0][1] > 0.97+0.19 or resultat[0][1] < 0.97-0.19):
			dolentes += 1
		if (resultat[1][0] > 3.69+0.41 or resultat[1][0] < 2.2-0.41):
			dolentes += 1
		if (resultat[1][1] > 2.2+0.5 or resultat[1][1] < 2.2-0.5):
			dolentes += 1
		if (resultat[2][0] > 0.79+0.22 or resultat[2][0] < 0.79-0.22):
			dolentes += 1
		if (resultat[2][1] > 1.12+0.33 or resultat[2][1] < 1.12-0.33):
			dolentes += 1

		if (resultat[0][0] > 0.71+0.15 or resultat[0][0] < 0.71-0.15):
			dolentes += 1
		if (resultat[0][1] > 0.97+0.19 or resultat[0][1] < 0.97-0.19):
			dolentes += 1
		if (resultat[1][0] > 3.69+0.41 or resultat[1][0] < 2.2-0.41):
			dolentes += 1
		if (resultat[1][1] > 2.2+0.5 or resultat[1][1] < 2.2-0.5):
			dolentes += 1
		if (resultat[2][0] > 0.79+0.22 or resultat[2][0] < 0.79-0.22):
			dolentes += 1
		if (resultat[2][1] > 1.12+0.33 or resultat[2][1] < 1.12-0.33):
			dolentes += 1
		
		lv_mass = 0
		if (lv_mass > 25.7+3.6 or lv_mass < 25.7-3.6):
			dolentes += 1

		LVESV =0
		if (LVESV > 19.35+11.3 or LVESV < 19.35-11.3):
			dolentes += 1
		LVEDV = 0
		if (LVEDV > 57.7-16.5 or LVEDV < 57.7-16.5):
			dolentes += 1
		EF =0
		if (EF > 71+11 or EF < 71-11):
			dolentes += 1
		FS = 0
		if (FS > 43+9 or FS < 43-9):
			dolentes += 1
		SV = 0
		if (SV > 35.1-8.5 or SV < 35.1-8.5):
			dolentes += 1
		CO = 0
		if (CO > 17.7+3.8 or CO < 17.7-3.8):
			dolentes += 1


	if (dolentes > 2):
		print("El cor no és sa.")


	return resultat



