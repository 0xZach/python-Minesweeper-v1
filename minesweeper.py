import tkinter as tk
import tkinter.font as font
import random as r


def creationMainFrame(difficulty,frame):
 
    
    def afficherBombs(): # fonction d'affichage de toute les bombes
        
        for i in range(100): # pour chaque case, on vérifie s'il y a une bombe et on applique la couleur
            
            if(infos['is_'+str(i)+'_bombed'] == False and infos['case_'+str(i)]["background"] == "red4"):
                infos['case_'+str(i)].configure(background="SpringGreen4")
                
            if(infos['is_'+str(i)+'_bombed'] == True and infos['case_'+str(i)]["background"] != "gray26"):
                infos['case_'+str(i)].configure(background="gray26")
    
    
    def gagner(): # fonction qui renvois un booleen, True si le joueur à gagné, False si ce n'est pas le cas
        for i in range(100): # pour chaque case, on vérifie si elle ne contient pas de bombe ET a déjà été découverte
            
            if(infos['is_'+str(i)+'_bombed'] == False and infos['case_'+str(i)]["background"] != "OliveDrab1"):
                return False # si une case ne correspond pas, alors on return false
                
        return True

    
    def numberOfBombs(wbutton): # returns int, nombre de bombes autour de la case
        
        nbBomb = 0
        list_ligne=[-1,0,1]
        list_colon=[-10,0,10]
        
        for i in list_ligne:
            if(wbutton+i >= 0 and wbutton+i < 100): # on test si on est bien dans le nombre de boutons
                
                for j in list_colon:
                    if((wbutton+j >= 0 and wbutton+j < 100) and (wbutton+j+i >=0 and wbutton+j+i < 100)): # on test si on est bien dans le nombre de boutons
                        
                        if(infos['is_'+str(wbutton+i+j)+'_bombed']== True and (infos[str(wbutton)+"_X"]+i>=0 and infos[str(wbutton)+"_X"]+i<=9)):
                            
                            if(infos['is_'+str(wbutton+i+j)+'_bombed']== True and (infos[str(wbutton)+"_Y"]>=0 and infos[str(wbutton)+"_Y"]<=9)):
                                nbBomb+=1
        
                
        return nbBomb
    
    
    def checkButtons(wbutton,first):
        list_Ligne=[-1,0,1] #listes des changements de coordonnées en ligne
        list_Colon=[-10,0,10] #listes des changements de coordonnées en colonne
        
        for i in list_Ligne:
            
            if(wbutton+i >= 0 and wbutton+i < 100): # on test si on est bien dans le nombre de boutons
                    #on teste si il y a une bombe dans la case '+i' et on vérifie si les coordonnées sont entre 0 et 9 (de 0 à la taille de ligne)
                    for j in list_Colon:
                        #print(j)
                        if((wbutton+j >= 0 and wbutton+j < 100) and (wbutton+j+i >=0 and wbutton+j+i < 100)): # on test si on est bien dans le nombre de boutons
                             
                            if(first==False):
                                 if(infos['case_'+str(wbutton+i+j)]['background']=='SpringGreen4'): # on regarde si la case est toujours caché et on ne la teste que dans le cas où elle l'est
                                     
                                    if(infos['is_'+str(wbutton+i+j)+'_bombed']== False and (infos[str(wbutton)+"_X"]+i>=0 and infos[str(wbutton)+"_X"]+i<=9)):
                                        if(infos['is_'+str(wbutton+j+i)+'_bombed'] == False and (infos[str(wbutton)+"_Y"]>=0 and infos[str(wbutton)+"_Y"]<=9)):
                                        # on vérifie si les coordonnées sont entre 0 et 9 (de 0 à la taille de la colonne)
                                            infos['case_'+str(wbutton+i+j)].configure(background="OliveDrab1") # on configure la nouvelle couleur
                                            #print(wbutton+i+j,i,j)
                                            
                                            nb_Bombs = numberOfBombs(wbutton+i+j)
                                            if(nb_Bombs > 0):
                                                infos['case_'+str(wbutton+i+j)].configure(text=nb_Bombs)
                                            elif(nb_Bombs == 0):
                                                checkButtons(wbutton+i+j,False)
                            
                            else:
                                if(infos['is_'+str(wbutton+i+j)+'_bombed']== False and (infos[str(wbutton)+"_X"]+i>=0 and infos[str(wbutton)+"_X"]+i<=9)):
                                    if(infos['is_'+str(wbutton+j+i)+'_bombed'] == False and (infos[str(wbutton)+"_Y"]>=0 and infos[str(wbutton)+"_Y"]<=9)):
                                    # on vérifie si les coordonnées sont entre 0 et 9 (de 0 à la taille de la colonne)
                                        infos['case_'+str(wbutton+i+j)].configure(background="OliveDrab1") # on configure la nouvelle couleur
                                        #print(wbutton+i+j,i,j)
                                        
                                        nb_Bombs = numberOfBombs(wbutton+i+j)
                                        if(nb_Bombs > 0):
                                            infos['case_'+str(wbutton+i+j)].configure(text=nb_Bombs)
                                        elif(nb_Bombs == 0):
                                            checkButtons(wbutton+i+j,False)

           
    def onclick(wbutton,jouable):
        if(jouable.get()==1):
            # couleurs cases bombe: red4 ; gray26
            if(infos['is_'+str(wbutton)+'_bombed'] == True and infos['case_'+str(wbutton)]['background']!="gray26"):
                # on donne la couleur à la case si elle contient une bombe est n'est pas déjà colorée
                infos['case_'+str(wbutton)].configure(relief='sunken')
                infos['case_'+str(wbutton)].configure(background="gray26")
                # on affiche les autres bombes
                afficherBombs()
                # on termine la partie
                jouable.set(2)
                
                # on créé la fenetre d'affichage du message de fin de partie
                lose_frame = tk.Tk()
                lose_frame.title('Minesweeper ZS 1.0')
                lose_frame.geometry('180x120')
                lose_frame.configure(bg='light goldenrod')
                losefont = font.Font(family='Helvetica', size=30, weight='bold')
                replayfont = font.Font(family='Helvetica', size=15, weight='bold')
                replay = tk.Button(lose_frame, text="Replay?", font = replayfont, background='goldenrod', activebackground='goldenrod', borderwidth=4, command= lambda:rejouer(jouable,lose_frame))
                replay.pack()
                replay.place(y=60,x=40)
                lose = tk.Label(lose_frame, text="You lost!", font = losefont, background='light goldenrod', relief="solid")
                lose.pack()
                lose.place(y=0,x=4)
                
            elif(infos['case_'+str(wbutton)]['background']!="OliveDrab1" and infos['case_'+str(wbutton)]['background']!="gray26"):
                # on donne la couleur bleu à la case si elle ne contient une bombe est n'est pas déjà bleu
                checkButtons(wbutton,False)
                #print(gagner())
                if(gagner() == True): # si on a gagné
                    # on affiche l'emplacement des bombes
                    afficherBombs()
                    
                    # on termine la partie
                    jouable.set(2)
                    
                    # on affiche le message de fin de partie.
                    win_frame = tk.Tk()
                    win_frame.title('Minesweeper ZS 1.0')
                    win_frame.geometry('180x120')
                    win_frame.configure(bg='light goldenrod')
                    winfont = font.Font(family='Helvetica', size=30, weight='bold')
                    replayfont = font.Font(family='Helvetica', size=15, weight='bold')
                    replay = tk.Button(win_frame, text="Replay?", font = replayfont, background='goldenrod', activebackground='goldenrod', borderwidth=4,command= lambda:rejouer(jouable,win_frame))
                    replay.pack()
                    replay.place(y=60,x=40)
                    win = tk.Label(win_frame, text="You Won!", font = winfont, background='light goldenrod', relief="solid")
                    win.pack()
                    win.place(y=0,x=4)
        
        elif(jouable.get() == 0):
            infos['case_'+str(wbutton)]['background']="OliveDrab1"
            bomb_list=[wbutton]
            while(len(bomb_list) < 26):
                bomb = r.randrange(100)
                dispo = True
                j = 0
                while(j < len(bomb_list) and dispo == True):
                    if(bomb_list[j] == bomb):
                        dispo = False
                    j=j+1
                if(dispo == True):
                    bomb_list.append(bomb)
                    infos['is_'+str(bomb)+'_bombed']=True
            jouable.set(1)
            checkButtons(wbutton,True)
        
    
    def left_click_press(event,i):
        infos['case_'+str(i)].configure(relief='sunken')
        onclick(i,jouable)
    def left_click_release(event):
        event.widget.configure(relief='raised')
    
    def right_click_press(event):
        event.widget.configure(relief='sunken')
        if(event.widget['background']=="SpringGreen4" and infos['nbr_flags'] < 25):
            event.widget.configure(background="red4")
            infos['nbr_flags'] = infos['nbr_flags'] + 1
            nbr_flags['text']= "flags left: "+str(25 - infos['nbr_flags'])
        elif(event.widget['background']=="red4" and infos['nbr_flags'] <= 25):
            event.widget.configure(background="SpringGreen4")
            infos['nbr_flags'] = infos['nbr_flags'] - 1
            nbr_flags['text']= "flags left: "+str(25 - infos['nbr_flags'])
    def right_click_release(event):
        event.widget.configure(relief='raised')
    
    def rejouer(jouable, end_frame):
        frame.destroy()
        demarrage(end_frame)
    


    
    
    # //////////////////////////////////////////////////début de la fonction//////////////////////////////////////////////////////////////
    




    #switch(difficulty)
    infos = {}

    frame.geometry('850x850') # on défini la taille de la fenetre
    
    offsetY = 0  # int qui s'incrémentera pour faire plusieurs lignes
    
    jouable = tk.IntVar()
    jouable.set(0) # intVar qui décide si cliquer sur les boutons fait une action ou non.
    
    GameFont = font.Font(family='Helvetica', size=10, weight='bold')
    
    infos['nbr_flags']=0
    
    nbr_flags = tk.Label(frame, text="flags left: "+str(25-infos['nbr_flags']), font=GameFont, relief='solid', background='goldenrod')
    nbr_flags.pack
    nbr_flags.place(x = 27, y = 5)
    
    display_nbrBombs = tk.Label(frame, text="number of bombs: 25", font=GameFont, relief='solid', background='goldenrod')
    display_nbrBombs.pack
    display_nbrBombs.place(x = 672, y = 5)
    
    for i in range(100):
        name="case_"+str(i)
        infos[name]= tk.Label(frame, text="", width=8, height=4, font=GameFont, relief='raised', anchor='center')
        
        infos[name].bind("<ButtonPress-1>", lambda event,i=i:left_click_press(event,i))
        infos[name].bind("<ButtonRelease-1>", left_click_release)
        
        infos[name].bind("<ButtonPress-3>", right_click_press)
        infos[name].bind("<ButtonRelease-3>", right_click_release)
        
        infos[name].configure(background="SpringGreen4")
        
        infos['is_'+str(i)+'_bombed']=False
        
        """
        if(randrange(4) == 3): # 25% de bombes
            infos['is_'+str(i)+'_bombed']=True
        else:
            infos['is_'+str(i)+'_bombed']=False
        """
        
        # en fonction dun random entre 0 et 1, on donne la propriété correspondante
        # si True alors il y aura une bombe
        # si False alors il n'y aura pas de bombe
        
        #print(infos)
            
        infos[name].place(x = 80 * (i%10) + 27) # calcul de la valeur de largeur de la case en fonction du reste de i%10

        infos[name].place(y = 80*offsetY + 32) # calcul de la valeur de hauteur de la case en fonction de offsetY


        infos[str(i)+'_X']= i%10 # on récupère la place X dans le tableau de taille [X][Y]
        
        infos[str(i)+'_Y']= offsetY # on récupère la place Y dans le tableau de taille [X][Y]


        if(80*(i%10) == 720):  # on teste si on est arrivé à la fin de la largeur du tableau
            offsetY = offsetY + 1     # si on est à la fin du tableau on incrémente le compteur de ligne

"""
fonction: creationMainFrame
paramètres: un int, un objet de type Tk
sortie: créé des cases pour l'objet en paramètre (l'int difficulty ne sert pas encore)
"""


    
    
    # //////////////////////////////////////////////////début du programme//////////////////////////////////////////////////////////////
    





def demarrage(frame):
    """
    mainFrame = tk.Tk()
    mainFrame.title('Minesweeper ZS 1.0')
    mainFrame.configure(bg='light goldenrod')
    
    title.forget()
    prop.forget()
    start.forget()
    """
    creationMainFrame(0,frame)

    #print(infos_cases,len(infos_cases))
    #frame.destroy()

root= tk.Tk()
root.title('Minesweeper ZS 1.0')
root.geometry('300x200+810+440')
root.configure(bg='light goldenrod')

titlefont = font.Font(family='Helvetica', size=20, weight='bold')

labelDepart= tk.Label(root, text="Minesweeper", background='goldenrod', font=titlefont, relief="solid")
labelProp = tk.Label(root, text="Made by Sylvain Masclet", background='light goldenrod')
boutonDepart= tk.Button(root, text='Start the game!', background='goldenrod', activebackground='goldenrod', command= lambda:demarrage(root))

labelDepart.pack
labelProp.pack
boutonDepart.pack
labelDepart.place(x=60, y=50)
labelProp.place(x=0,y=180)
boutonDepart.place(x=100, y=100)

root.mainloop()


