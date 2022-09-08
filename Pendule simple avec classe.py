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


class masse:
	def __init__(self,angle,longueur):
		self.x=sin(angle) * longueur + origine_x
		self.y=cos(angle) * longueur + origine_y
		self.longueur_fil=longueur

	def coords(self,angle):
		self.x=sin(angle) * self.longueur_fil + origine_x
		self.y=cos(angle) * self.longueur_fil + origine_y


def radians(angle):
	return angle*2*pi/360

def deplacement():
	Canevas.delete(ALL)

	Canevas.create_line(origine_x,origine_y,balle.x,balle.y)
	Canevas.create_oval(balle.x-rayon_balle,balle.y-rayon_balle,balle.x+rayon_balle,balle.y+rayon_balle,fill='red')

	teta=radians(teta_initial)*cos( sqrt(pesanteur/longueur_fil) * (time()-debut_temps) )
	balle.coords(teta)



	fenetre.after(20,deplacement)







balle=masse(radians(teta_initial),longueur_fil)
debut_temps=time()
#print(debut_temps)

fenetre=Tk()

Canevas=Canvas(fenetre,height=hauteur,width=largeur)
Canevas.pack(padx=5,pady=5)


deplacement()

fenetre.mainloop()