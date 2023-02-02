#########Importer les modules necessaires########


from tkinter import *
from random import *
import time
from tkinter.font import Font
import random


#####################################
############Fonctions################
#####################################


joueur=1 #variable joueur pour savoir qui jouer
joueur1=[0,0]

def aquidejouer():
    global joueur #prend la variable joueur et permet de la modifier si elle n'est pas dans un def
    if joueur==1:
        aqui=1
        joueur=2
    elif joueur==2:
        aqui=2
        joueur=1
    return joueur

def clic(event):
    global L #prend la variable L en global
    aquidejouer() #exécute
    x=event.x
    y=event.y #prend les coordonnées x et y
    if joueur==1:
            if y<200 and y>=0:
                if x<200 and x>=0:
                    if L[0][0]!=1 and L[0][0]!=5:
                        Canevas.create_rectangle(50,50,150,150,fill='red')
                        L[0][0]=1
                elif x<400 and x>200:
                    if L[0][1]!=1 and L[0][1]!=5:
                        Canevas.create_rectangle(250,50,350,150,fill='red')
                        L[0][1]=1
                elif x<=600 and x>400:
                    if L[0][2]!=1 and L[0][2]!=5:
                        Canevas.create_rectangle(450,50,550,150,fill='red')
                        L[0][2]=1
            elif y<400 and y>200:
                if x<200 and x>=0:
                    if L[1][0]!=1 and L[1][0]!=5:
                        Canevas.create_rectangle(50,250,150,350,fill='red')
                        L[1][0]=1
                elif x<400 and x>200:
                    if L[1][1]!=1 and L[1][1]!=5:
                        Canevas.create_rectangle(250,250,350,350,fill='red')
                        L[1][1]=1
                elif x<=600 and x>400:
                    if L[1][2]!=1 and L[1][2]!=5:
                        Canevas.create_rectangle(450,250,550,350,fill='red')
                        L[1][2]=1
            elif y<=600 and y>400:
                if x<200 and x>=0:
                    if L[2][0]!=1 and L[2][0]!=5:
                        Canevas.create_rectangle(50,450,150,550,fill='red')
                        L[2][0]=1
                elif x<400 and x>200:
                    if L[2][1]!=1 and L[2][1]!=5:
                        Canevas.create_rectangle(250,450,350,550,fill='red')
                        L[2][1]=1
                elif x<=600 and x>400:
                    if L[2][2]!=1 and L[2][2]!=5:
                        Canevas.create_rectangle(450,450,550,550,fill='red')
                        L[2][2]=1
    elif joueur==2:
            if y<200 and y>=0:
                if x<200 and x>=0:
                    if L[0][0]!=1 and L[0][0]!=5:
                        Canevas.create_oval(50,50,150,150,fill='blue')
                        L[0][0]=5
                elif x<400 and x>200:
                    if L[0][1]!=1 and L[0][1]!=5:
                        Canevas.create_oval(250,50,350,150,fill='blue')
                        L[0][1]=5
                elif x<=600 and x>400:
                    if L[0][2]!=1 and L[0][2]!=5:
                        Canevas.create_oval(450,50,550,150,fill='blue')
                        L[0][2]=5
            elif y<400 and y>200:
                if x<200 and x>=0:
                    if L[1][0]!=1 and L[1][0]!=5:
                        Canevas.create_oval(50,250,150,350,fill='blue')
                        L[1][0]=5
                elif x<400 and x>200:
                    if L[1][1]!=1 and L[1][1]!=5:
                        Canevas.create_oval(250,250,350,350,fill='blue')
                        L[1][1]=5
                elif x<=600 and x>400:
                    if L[1][2]!=1 and L[1][2]!=5:
                        Canevas.create_oval(450,250,550,350,fill='blue')
                        L[1][2]=5
            elif y<=600 and y>400:
                if x<200 and x>=0:
                    if L[2][0]!=1 and L[2][0]!=5:
                        Canevas.create_oval(50,450,150,550,fill='blue')
                        L[2][0]=5
                elif x<400 and x>200:
                    if L[2][1]!=1 and L[2][1]!=5:
                        Canevas.create_oval(250,450,350,550,fill='blue')
                        L[2][1]=5
                elif x<=600 and x>400:
                    if L[2][2]!=1 and L[2][2]!=5:
                        Canevas.create_oval(450,450,550,550,fill='blue')
                        L[2][2]=5

    print(L)
    victoire()


def aff1():
    t=Champ.get()
    Donnej1=Lab.configure(text='Joueur 1: '+t)


def aff2():
    global joueur1
    global joueur2
    t=Champ1.get()
    Donnej2=Lab1.configure(text='Joueur 2: '+t)


def afficher(event) :
    message.configure(text="Score="+"3"+str(joueur2).format(joueur1, joueur2))


def affichagecase():
    for j in range(2):
        for i in range(2):
            Canevas.create_rectangle(i*200,200+j*200,600,200+j*200,fill='white')
            Canevas.create_rectangle(200+i*200,j*200,200+i*200,600,fill='white')


def victoire ():
    joueur1=0
    joueur2=0
    if (L[0][0]+L[0][1]+L[0][2]==3 or#parcour les element dans la liste et regarde si le resultat d une ligne =3 le joueur 1 gagne
       L[1][0]+L[1][1]+L[1][2]==3 or
       L[2][0]+L[2][1]+L[2][2]==3 or
       L[0][0]+L[1][1]+L[2][2]==3 or
       L[2][0]+L[1][1]+L[0][2]==3):
        print('Gagné joueur 2')
        joueur2=joueur2+1
        if joueur2==3:
            breake=1
    elif (L[0][0]+L[0][1]+L[0][2]==15 or#si le resultat =15 le joueur 2 gagne
       L[1][0]+L[1][1]+L[1][2]==15 or
       L[2][0]+L[2][1]+L[2][2]==15 or
       L[0][0]+L[1][1]+L[2][2]==15 or
       L[2][0]+L[1][1]+L[0][2]==15):
        print('Gagné joueur 1')
        joueur1=joueur1+1
        if joueur1==3:
            breake=1

def pagedeniveau():#ouvre la page du choix des niveau
    win = Toplevel(pagedechoix)#n arrive pas a afficher de bouton sur cette page

##########################################################
##########    Variables ##################################
##########################################################


L=[[0,0,0],
   [0,0,0],
   [0,0,0]]#liste va varier en fonction de l emplacement des pions


#########################################################
########## Interface graphique ##########################
##########################################################
#choix du mode
pagedechoix = Tk()#cree page pour choisir un mode
pagedechoix.title("Choix de mode")
pagedechoix.geometry('300x300')
bouton1 = Button(pagedechoix, text="1vsbot", command = pagedeniveau).pack()#ouuvre la page pour choisir le niveau
bouton2 = Button(pagedechoix, text="1vs1", command = pagedechoix.destroy).pack()#ferme page choix de mode pour jouer sur page par defaut


#page 1vs1 par defaut
root = Tk()
root.title("Morpion")

#champ1
Lab = Label(root, fg ='blue', bg ='white')
Lab.pack(expand = TRUE, side = TOP, fill = BOTH, padx = 5, pady = 5)
Champ = Entry(root, bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(expand = TRUE, side = TOP, fill = BOTH, padx = 5, pady = 5)
bouton=Button(root, text="Nom ?", command=aff1)
bouton.pack(expand = TRUE, side = TOP, fill = BOTH)
#

#champ 2
Lab1 = Label(root, fg ='red', bg ='white')
Lab1.pack(expand = TRUE, side = TOP, fill = BOTH, padx = 5, pady = 5)
Champ1 = Entry(root, bg ='bisque', fg='maroon')
Champ1.focus_set()
Champ1.pack(expand = TRUE, side = TOP, fill = BOTH, padx = 5, pady = 5)
bouton1=Button(root, text="Nom ?", command=aff2)
bouton1.pack(expand = TRUE, side = TOP, fill = BOTH)
#

#message score
message=Label(root, text="joueur1")
message.pack(expand = TRUE,side = TOP, fill = BOTH, padx = 5, pady = 5)


#Canvas
Canevas = Canvas(root,width=600,height=600,bg ='white')
Canevas.pack()
font = Font(family='Liberation Serif', size=200)
Button(root, text="Quit", command=root.destroy).pack()




###########################################################
########### Receptionnaire d'évènement ####################
###########################################################


Canevas.bind('<Button-1>',clic)
affichagecase()

###################### FIN ###############################

pagedechoix.mainloop()
root.mainloop()
