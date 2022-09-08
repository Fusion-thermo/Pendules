from tkinter import *
from math import cos, sin, tan, pi, sqrt
from time import time


hauteur=500
largeur=hauteur
origine_x=largeur//2
origine_y=hauteur//3

rayon_balle=3
teta_initial=90  #degrés
longueur_fil=140
pesanteur=100


def radians(angle):
	return angle*2*pi/360

def deplacement():
	#Canevas.delete(ALL)
	global x,y,teta_max

	x_prec=x
	y_prec=y
	#mettre teta_max*=0.998 pour avoir de la friction
	teta_max*=1

	teta=radians(teta_max)*cos( sqrt(pesanteur/longueur_fil) * (time()-debut_temps) )
	x=sin(teta) * longueur_fil + origine_x
	y=cos(teta) * longueur_fil + origine_y
	
	Canevas.coords(fil,origine_x,origine_y,x,y)
	Canevas.coords(balle,x-rayon_balle,y-rayon_balle,x+rayon_balle,y+rayon_balle)
	#Canevas.create_line(x_prec,y_prec,x,y)




	fenetre.after(40,deplacement)







debut_temps=time()

fenetre=Tk()

Canevas=Canvas(fenetre,height=hauteur,width=largeur)
Canevas.pack(padx=5,pady=5)

x=sin(radians(teta_initial)) * longueur_fil + origine_x
y=cos(radians(teta_initial)) * longueur_fil + origine_y
teta_max=teta_initial

#permet de créer les objets et on a plus qu'à mettre leurs cos à jour

fil=Canevas.create_line(origine_x,origine_y,x,y)
balle=Canevas.create_oval(x-rayon_balle,y-rayon_balle,x+rayon_balle,y+rayon_balle,fill='red')


deplacement()

fenetre.mainloop()