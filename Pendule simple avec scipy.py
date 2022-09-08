from tkinter import *
from math import cos, sin, tan, pi, sqrt
from time import time
import numpy as np
from scipy.integrate import odeint



teta_initial=90  #degrés

def radians(angle):
	return angle*2*pi/360


def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt


b = 0.25
c = 5.0

y0 = [radians(90), 0.0]

t = np.linspace(0, 100, 5001)

sol = odeint(pend, y0, t, args=(b, c))

angles=[round(sol[i,0],4) for i in range(len(sol[:,0]))]
angles_degres=[round(sol[i,0]*180/np.pi,1) for i in range(len(sol[:,0]))]
#print(angles,type(angles))



hauteur=500
largeur=hauteur
origine_x=largeur//2
origine_y=hauteur//3

rayon_balle=3
longueur_fil=140


def deplacement():
	#Canevas.delete(ALL)
	global x,y,compteur

	#mettre teta_max*=0.998 pour avoir de la friction
	compteur+=1

	teta=angles[compteur]
	x=sin(teta) * longueur_fil + origine_x
	y=cos(teta) * longueur_fil + origine_y
	
	Canevas.coords(fil,origine_x,origine_y,x,y)
	Canevas.coords(balle,x-rayon_balle,y-rayon_balle,x+rayon_balle,y+rayon_balle)



	fenetre.after(20,deplacement)







debut_temps=time()

fenetre=Tk()

Canevas=Canvas(fenetre,height=hauteur,width=largeur)
Canevas.pack(padx=5,pady=5)

x=sin(radians(teta_initial)) * longueur_fil + origine_x
y=cos(radians(teta_initial)) * longueur_fil + origine_y
compteur=-1

#permet de créer les objets et on a plus qu'à mettre leurs cos à jour

fil=Canevas.create_line(origine_x,origine_y,x,y)
balle=Canevas.create_oval(x-rayon_balle,y-rayon_balle,x+rayon_balle,y+rayon_balle,fill='red')

Bouton1 = Button(fenetre,  text = 'Quitter',  command = fenetre.destroy)
Bouton1.pack()

deplacement()

fenetre.mainloop()