from tkinter import *
from time import time
import numpy as np
from scipy.integrate import odeint
from random import randint


hauteur=800
largeur=1100
origine_x=largeur//2
origine_y=hauteur//2

longueur_fil=140
masse=1
rayon_balle=10


g= 9.81

def radians(angle):
	angle=int(angle)
	return angle*2*np.pi/360


def pend(y, t, L1, L2, m1, m2):
	"""Return the first derivatives of y = theta1, z1, theta2, z2."""
	theta1, z1, theta2, z2 = y

	c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)

	theta1dot = z1
	#print(type(m2),type(c),type(L1),type(z1))
	#print(m2*g*np.sin(theta2))
	z1dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) - (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
	theta2dot = z2
	z2dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) + 
	         m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)

	dydt = [theta1dot, z1dot, theta2dot, z2dot]
	return dydt


def solution():
	global angles_1, angles_2
	# Pendulum rod lengths (m), bob masses (kg).
	L1, L2 = 1, float(longueur.get()) #on met longeur fil 1 en tant que référence à 1, donc il faut adapter L2
	m1, m2 = 1, float(masse.get())

	y0 = np.array([radians(int(teta_initial_var_1.get())), 0.0,radians(int(teta_initial_var_2.get())), 0.0])

	t = np.linspace(0, 100, 5001)

	sol = odeint(pend, y0, t, args=(L1, L2, m1, m2))


	angles_1=[sol[i,0] for i in range(len(sol[:,0]))]
	angles_2=[sol[i,2] for i in range(len(sol[:,2]))]

	#return angles_1,angles_2
	deplacement()



def deplacement():
	global x1,y1,compteur,x2,y2,angles_1, angles_2

	compteur+=1

	x1_prec=x1
	y1_prec=y1
	x2_prec=x2
	y2_prec=y2


	teta_1=angles_1[compteur]
	teta_2=angles_2[compteur]
	x1=np.sin(teta_1) * longueur_fil + origine_x
	y1=np.cos(teta_1) * longueur_fil + origine_y
	x2=np.sin(teta_2) * longueur_fil * float(longueur.get()) + x1
	y2=np.cos(teta_2) * longueur_fil * float(longueur.get()) + y1

	
	Canevas.coords(fil_1,origine_x,origine_y,x1,y1)
	Canevas.coords(balle_1,x1-rayon_balle,y1-rayon_balle,x1+rayon_balle,y1+rayon_balle)
	Canevas.coords(fil_2,x1,y1,x2,y2)
	Canevas.coords(balle_2,x2-rayon_balle*float(masse.get()),y2-rayon_balle*float(masse.get()),x2+rayon_balle*float(masse.get()),y2+rayon_balle*float(masse.get()))
	if compteur>1:
		Canevas.create_line(x1_prec,y1_prec,x1,y1, fill="red")
		Canevas.create_line(x2_prec,y2_prec,x2,y2, fill="blue")


	fenetre.after(20,deplacement)




def demo_pendules(rien="rien"):
	x1=np.sin(radians(angle1.get())) * longueur_fil + origine_x
	y1=np.cos(radians(angle1.get())) * longueur_fil + origine_y
	x2=np.sin(radians(angle2.get())) * longueur_fil * float(longueur.get())  + x1
	y2=np.cos(radians(angle2.get())) * longueur_fil * float(longueur.get())  + y1

	Canevas.coords(fil_1,origine_x,origine_y,x1,y1)
	Canevas.coords(balle_1,x1-rayon_balle,y1-rayon_balle,x1+rayon_balle,y1+rayon_balle)
	Canevas.coords(fil_2,x1,y1,x2,y2)
	Canevas.coords(balle_2,x2-rayon_balle*float(masse.get()),y2-rayon_balle*float(masse.get()),x2+rayon_balle*float(masse.get()),y2+rayon_balle*float(masse.get()))
	teta_initial_var_1.set(angle1.get())
	teta_initial_var_2.set(angle2.get())







fenetre=Tk()
fenetre.attributes('-fullscreen', True)

Canevas=Canvas(fenetre,height=hauteur,width=largeur)
Canevas.pack(padx=5,pady=5,side=LEFT)


Bouton1 = Button(fenetre,  text = 'Quitter',  command = fenetre.destroy)
Bouton1.pack()

longueur=StringVar()
longueur.set(1.5)
echelle_longueur=Scale(fenetre,  orient='horizontal',  from_=0.2,  to=4,  resolution=0.2,  \
tickinterval=1,  label='Rapport des longueurs de fil',  variable=longueur,  command=demo_pendules)
echelle_longueur.pack()

masse=StringVar()
masse.set(1)
echelle_masse=Scale(fenetre,  orient='horizontal',  from_=0.2,  to=5,  resolution=0.2,  \
tickinterval=1,  label='Rapport des masses',  variable=masse,  command=demo_pendules)
echelle_masse.pack()

angle1=StringVar()
angle1.set(randint(90,180))
teta_initial_var_1=StringVar()
teta_initial_var_1.set(angle1.get())
echelle_angle1=Scale(fenetre,  orient='horizontal',  from_=0,  to=180,  resolution=5,  \
tickinterval=60,  label='Angle 1',  variable=angle1,  command=demo_pendules)
echelle_angle1.pack()

angle2=StringVar()
angle2.set(randint(90,180))
teta_initial_var_2=StringVar()
teta_initial_var_2.set(angle2.get())
echelle_angle2=Scale(fenetre,  orient='horizontal',  from_=0,  to=360,  resolution=10,  \
tickinterval=120,  label='Angle 2',  variable=angle2,  command=demo_pendules)
echelle_angle2.pack()

Bouton3 = Button(fenetre,  text = 'Lancer',  command = solution)
Bouton3.pack()

#a1,a2=solution(int(angle1.get()),int(angle2.get()))

x1=np.sin(radians(angle1.get())) * longueur_fil + origine_x
y1=np.cos(radians(angle1.get())) * longueur_fil + origine_y
x2=np.sin(radians(angle2.get())) * longueur_fil * float(longueur.get()) + x1
y2=np.cos(radians(angle2.get())) * longueur_fil * float(longueur.get()) + y1

#permet de créer les objets et on a plus qu'à mettre leurs cos à jour
fil_1=Canevas.create_line(origine_x,origine_y,x1,y1)
fil_2=Canevas.create_line(x1,y1,x2,y2)
balle_1=Canevas.create_oval(x1-rayon_balle,y1-rayon_balle,x1+rayon_balle,y1+rayon_balle,fill='red')
balle_2=Canevas.create_oval(x2-rayon_balle*float(masse.get()),y2-rayon_balle*float(masse.get()),x2+rayon_balle*float(masse.get()),y2+rayon_balle*float(masse.get()),fill='blue')

compteur=-1

demo_pendules("rien")

fenetre.mainloop()