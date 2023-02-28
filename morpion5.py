########## Importer les modules necessaires ##############
from tkinter import *
from random import *
import time
from tkinter.font import Font
import random
import tkinter
##########################################################
##########    Fonctions ##################################
##########################################################
joueur=1
joueur1=0
joueur2=0
niveau=0
nbpion=0
L=[[0,0,0],
   [0,0,0],
   [0,0,0]]
laplace=-1
def jeu():
    def niveaufacile():
            global niveau
            niveau=1
            pagejouerrobot()
    def niveaumoyen():
            global niveau
            niveau=2
            pagejouerrobot()
    def niveaudifficile():
            global niveau
            niveau=3
            pagejouerrobot()
    
    def pagedeniveau():#ouvre la page du choix des niveau
        pagedeniveau = tkinter.Tk()
        pagedeniveau.title("Choix du niveau")
        pagedeniveau.geometry('300x300')
        bouton3 = Button(pagedeniveau, text="niveau facile", command = niveaufacile).pack()#ouuvre la page pour choisir le niveau
        bouton4 = Button(pagedeniveau, text="niveau moyen", command = niveaumoyen).pack()#ferme page choix de mode pour jouer sur page par defaut
        bouton5 = Button(pagedeniveau, text="niveau difficile", command = niveaudifficile).pack()
        
        
        
################################ Page robot ##################################################################################################################################################################
        
            
        
            

    #def niveaumoyen():
        
    #def niveaudifficile():
        



    def matrix_zero():
        global L
        L=[[0,0,0],
           [0,0,0],
           [0,0,0]]
    def pagejouerrobot():
        matrix_zero()
        #variable joueur pour savoir qui jouer
        def affichagecase():
            for j in range(2):
                for i in range(2):
                    Canevas.create_rectangle(i*200,200+j*200,600,200+j*200,fill='white')
                    Canevas.create_rectangle(200+i*200,j*200,200+i*200,600,fill='white')

        def victoire ():
            global joueur1,joueur2
            if (L[0][0]+L[0][1]+L[0][2]==3 or#parcour les element dans la liste et regarde si le resultat d une ligne =3 le joueur 1 gagne
               L[1][0]+L[1][1]+L[1][2]==3 or
               L[2][0]+L[2][1]+L[2][2]==3 or
               L[0][0]+L[1][1]+L[2][2]==3 or
               L[2][0]+L[1][1]+L[0][2]==3 or
               L[0][0]+L[1][0]+L[2][0]==3 or
               L[0][1]+L[1][1]+L[2][1]==3 or
               L[0][2]+L[1][2]+L[2][2]==3):
                print('Gagné joueur 2')
                joueur2=joueur2+1
                root.destroy()
                if joueur2==1:
                    if joueur1==0:
                        mon_label.config(text="0-1")
                        mon_label2.config(text="0-1")
                    elif joueur1==1:
                        mon_label.config(text="1-1")
                        mon_label2.config(text="1-1")
                    elif joueur1==2:
                        mon_label.config(text="2-1")
                        mon_label2.config(text="2-1")
                    
                elif joueur2==2:
                    if joueur1==0:
                        mon_label.config(text="0-2")
                        mon_label2.config(text="0-2")
                    elif joueur1==1:
                        mon_label.config(text="1-2")
                        mon_label2.config(text="1-2")
                    elif joueur1==2:
                        mon_label.config(text="2-2")
                elif joueur2==3:
                    if joueur1==0:
                        mon_label.config(text="0-3")
                    elif joueur1==1:
                        mon_label.config(text="1-3")
                    elif joueur1==2:
                        mon_label.config(text="2-3")
                if joueur1==3:
                    pagedechoix.destroy()
                elif joueur2==3:
                    pagedechoix.destroy()

            elif (L[0][0]+L[0][1]+L[0][2]==15 or#si le resultat =15 le joueur 2 gagne
               L[1][0]+L[1][1]+L[1][2]==15 or
               L[2][0]+L[2][1]+L[2][2]==15 or
               L[0][0]+L[1][1]+L[2][2]==15 or
               L[2][0]+L[1][1]+L[0][2]==15 or
               L[0][0]+L[1][0]+L[2][0]==15 or
               L[0][1]+L[1][1]+L[2][1]==15 or
               L[0][2]+L[1][2]+L[2][2]==15):
                time.sleep(1)
                root.destroy()
                joueur1=joueur1+1
                print(joueur1,joueur2)
                if joueur1==1:
                    if joueur2==0:
                        mon_label.config(text="1-0")
                    elif joueur2==1:
                        mon_label.config(text="1-1")
                    elif joueur2==2:
                        mon_label.config(text="1-2")
                    
                elif joueur1==2:
                    if joueur2==0:
                        mon_label.config(text="2-0")
                    elif joueur2==1:
                        mon_label.config(text="2-1")
                    elif joueur2==2:
                        mon_label.config(text="2-2")
                elif joueur1==3:
                    if joueur2==0:
                        mon_label.config(text="3-0")
                    elif joueur2==1:
                        mon_label.config(text="3-1")
                    elif joueur2==2:
                        mon_label.config(text="3-2")
                if joueur1==3:
                    pagedechoix.destroy()
                    root.destroy()
                elif joueur2==3:
                    pagedechoix.destroy()
            
                




        def aquidejouer():
            global joueur,nbpion #prend la variable joueur et permet de la modifier si elle n'est pas dans le def
            
            if joueur==1:
                joueur=2
                
                        
                        
                
            elif joueur==2:
                joueur=1
                
                
            print(joueur)
            return joueur
        
        def aff1():
            t=Champ.get()
            


        def aff2():
            global joueur1
            global joueur2
            t=Champ1.get()
        def estcesquecestbon():
            global laplace
            if L[0][0]+L[0][1]+L[0][2]==2:
                #si le resultat =15 le joueur 2 gagne
            elif L[1][0]+L[1][1]+L[1][2]==2:
                laplace=1
            elif L[2][0]+L[2][1]+L[2][2]==2:
                laplace=2
            
            
                

        

        def cbonoupas(event):
            global L,nbpion,laplace #prend la variable L en global
            joueur=2 #exécute
            m=-1
            n=-1
            x=event.x
            y=event.y #prend les coordonnées x et y
            if joueur==2:
                for j in range(3):
                    m+=1
                    n=-1
                    for i in range(3):
                        n+=1
                        if y<i*200+200 and y>=i*200:
                            if x<j*200+200 and x>=j*200:
                                if L[m][n]!=1 and L[m][n]!=5:
                                    Canevas.create_oval(j*200+50,i*200+50,j*200+150,i*200+150,fill='blue')
                                    L[m][n]=5
                        
                                    if niveau==1:
                                        pionoupas=0
                                        nbpion=5
                                        a=0
                                        while pionoupas<=nbpion or a>30:
                                            nombrechoisi=random.randint(0,2)
                                            nombrechoisi2=random.randint(0,2)    
                                            if L[nombrechoisi][nombrechoisi2]!=1 and L[nombrechoisi][nombrechoisi2]!=5:  
                                                Canevas.create_rectangle(nombrechoisi*200+50,nombrechoisi2*200+50,nombrechoisi*200+150,nombrechoisi2*200+150,fill='red')                                                       
                                                L[nombrechoisi][nombrechoisi2]=1
                                                pionoupas=nbpion+1
                                                a=a+1
                                                print(a)
                                    elif niveau==2:
                                        pionoupas=0
                                        nbpion=5
                                        a=0
                                        estcequecestbon()
                                        while pionoupas<=nbpion or a>30:
                                            if laplace==0:
                                                for i in range(3):
                                                    Canevas.create_rectangle(laplace*200+50,i*200+50,laplace*200+150,i*200+150,fill='red')
                                            
                                                
                                            nombrechoisi=random.randint(0,2)
                                            nombrechoisi2=random.randint(0,2)    
                                            if L[nombrechoisi][nombrechoisi2]!=1 and L[nombrechoisi][nombrechoisi2]!=5:  
                                                Canevas.create_rectangle(nombrechoisi*200+50,nombrechoisi2*200+50,nombrechoisi*200+150,nombrechoisi2*200+150,fill='red')                                                       
                                                L[nombrechoisi][nombrechoisi2]=1
                                                pionoupas=nbpion+1
                                                a=a+1
                                                print(a)
                                    elif niveau==3:
                                        pionoupas=0
                                        nbpion=5
                                        a=0
                                        while pionoupas<=nbpion or a>30:
                                            nombrechoisi=random.randint(0,2)
                                            nombrechoisi2=random.randint(0,2)    
                                            if L[nombrechoisi][nombrechoisi2]!=1 and L[nombrechoisi][nombrechoisi2]!=5:  
                                                Canevas.create_rectangle(nombrechoisi*200+50,nombrechoisi2*200+50,nombrechoisi*200+150,nombrechoisi2*200+150,fill='red')                                                       
                                                L[nombrechoisi][nombrechoisi2]=1
                                                pionoupas=nbpion+1
                                                a=a+1
                                                print(a)
                                    
            
            
            
            
                                
                                          
            root.after(1000,victoire)
        root = Tk()
        root.title("Morpion")
        #canvas
        
        

        


        #Canvas
        Canevas = Canvas(root,width=600,height=600,bg ='white')
        Canevas.pack()
        font = Font(family='Liberation Serif', size=200)
        Button(root, text="Quit", command=root.destroy).pack()
        affichagecase()



        Canevas.bind('<Button-1>',cbonoupas)
    
        root.mainloop()
        ########################### Page 1v1 ###################################
    
    def matrix_zero():
        global L
        L=[[0,0,0],
           [0,0,0],
           [0,0,0]]
    def pagejouer():
        matrix_zero()
        #variable joueur pour savoir qui jouer
        def affichagecase():
            for j in range(2):
                for i in range(2):
                    Canevas.create_rectangle(i*200,200+j*200,600,200+j*200,fill='white')
                    Canevas.create_rectangle(200+i*200,j*200,200+i*200,600,fill='white')

        def victoire ():
            global joueur1,joueur2
            if (L[0][0]+L[0][1]+L[0][2]==3 or#parcour les element dans la liste et regarde si le resultat d une ligne =3 le joueur 1 gagne
               L[1][0]+L[1][1]+L[1][2]==3 or
               L[2][0]+L[2][1]+L[2][2]==3 or
               L[0][0]+L[1][1]+L[2][2]==3 or
               L[2][0]+L[1][1]+L[0][2]==3 or
               L[0][0]+L[1][0]+L[2][0]==3 or
               L[0][1]+L[1][1]+L[2][1]==3 or
               L[0][2]+L[1][2]+L[2][2]==3):
                print('Gagné joueur 2')
                joueur2=joueur2+1
                root.destroy()
                if joueur2==1:
                    if joueur1==0:
                        mon_label.config(text="0-1")
                    elif joueur1==1:
                        mon_label.config(text="1-1")
                    elif joueur1==2:
                        mon_label.config(text="2-1")
                    
                elif joueur2==2:
                    if joueur1==0:
                        mon_label.config(text="0-2")
                    elif joueur1==1:
                        mon_label.config(text="1-2")
                    elif joueur1==2:
                        mon_label.config(text="2-2")
                elif joueur2==3:
                    if joueur1==0:
                        mon_label.config(text="0-3")
                    elif joueur1==1:
                        mon_label.config(text="1-3")
                    elif joueur1==2:
                        mon_label.config(text="2-3")
                if joueur1==3:
                    pagedechoix.destroy()
                elif joueur2==3:
                    pagedechoix.destroy()

            elif (L[0][0]+L[0][1]+L[0][2]==15 or#si le resultat =15 le joueur 2 gagne
               L[1][0]+L[1][1]+L[1][2]==15 or
               L[2][0]+L[2][1]+L[2][2]==15 or
               L[0][0]+L[1][1]+L[2][2]==15 or
               L[2][0]+L[1][1]+L[0][2]==15 or
               L[0][0]+L[1][0]+L[2][0]==15 or
               L[0][1]+L[1][1]+L[2][1]==15 or
               L[0][2]+L[1][2]+L[2][2]==15):
                root.destroy()
                joueur1=joueur1+1
                print(joueur1,joueur2)
                if joueur1==1:
                    if joueur2==0:
                        mon_label.config(text="1-0")
                    elif joueur2==1:
                        mon_label.config(text="1-1")
                    elif joueur2==2:
                        mon_label.config(text="1-2")
                    
                elif joueur1==2:
                    if joueur2==0:
                        mon_label.config(text="2-0")
                    elif joueur2==1:
                        mon_label.config(text="2-1")
                    elif joueur2==2:
                        mon_label.config(text="2-2")
                elif joueur1==3:
                    if joueur2==0:
                        mon_label.config(text="3-0")
                    elif joueur2==1:
                        mon_label.config(text="3-1")
                    elif joueur2==2:
                        mon_label.config(text="3-2")
                if joueur1==3:
                    pagedechoix.destroy()
                    root.destroy()
                elif joueur2==3:
                    pagedechoix.destroy()
            
                




        def aquidejouer():
            global joueur #prend la variable joueur et permet de la modifier si elle n'est pas dans le def
            if joueur==1:
                joueur=2
                message.config(text="Au rouge de jouer !",fg="red")
            elif joueur==2:
                joueur=1
                message.config(text="Au bleu de jouer !",fg="blue")
            print(joueur)
            return joueur
        def aff1():
            t=Champ.get()
            Donnej1=Lab.configure(text='Joueur 1: '+t)


        def aff2():
            global joueur1
            global joueur2
            t=Champ1.get()
            Donnej2=Lab1.configure(text='Joueur 2: '+t)
        


        def cbonoupas(event):
            global L #prend la variable L en global
            aquidejouer() #exécute
            m=-1
            n=-1
            x=event.x
            y=event.y #prend les coordonnées x et y
            for j in range(3):
                m+=1
                n=-1
                for i in range(3):
                    n+=1
                    if y<i*200+200 and y>=i*200:
                        if x<j*200+200 and x>=j*200:
                            if L[m][n]!=1 and L[m][n]!=5:
                                if joueur==1:
                                    Canevas.create_rectangle(j*200+50,i*200+50,j*200+150,i*200+150,fill='red')
                                    L[m][n]=1
                                elif joueur==2:
                                    Canevas.create_oval(j*200+50,i*200+50,j*200+150,i*200+150,fill='blue')
                                    L[m][n]=5
            victoire()
        root = Tk()
        root.title("Morpion")
        #canvas
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
        message=Label(root, text="Au bleu de jouer !",fg="blue")
        message.pack(expand = TRUE,side = TOP, fill = BOTH, padx = 5, pady = 5)


        #Canvas
        Canevas = Canvas(root,width=600,height=600,bg ='white')
        Canevas.pack()
        font = Font(family='Liberation Serif', size=200)
        Button(root, text="Quit", command=root.destroy).pack()
        affichagecase()



        Canevas.bind('<Button-1>',cbonoupas)
    
        root.mainloop()

    pagedechoix = tkinter.Tk()
    pagedechoix.title("Choix de mode")
    pagedechoix.geometry('300x300')
    
    bouton1 = Button(pagedechoix, text="1vsbot", command = pagedeniveau).pack()#ouuvre la page pour choisir le niveau
    bouton2 = Button(pagedechoix, text="1vs1", command = pagejouer).pack()#ferme page choix de mode pour jouer sur page par defaut
    mon_labelscore = Label(pagedechoix,fg="red", text = "Le score est de :")
    mon_labelscore.pack()
    mon_label = Label(pagedechoix, text = "0-0",fg="blue")
    mon_label.pack()
                           
    pagedechoix.mainloop()

jeu()
