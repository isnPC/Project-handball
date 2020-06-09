from tkinter import *
from tkinter.messagebox import*
from math import *
import os.path

def veriffichier(listenomfichier):
    """verifier l'état des fichier
    si ils n'existent pas, il les créent
    si ils existent, il vérifi si ils sont vide, si non demande si on garde les données"""
    global f, joueurselec,result
    nbficvide=0
    if os.path.isfile('J1.csv'):
        #le fichier existe
        rechercheselec()
        indicjoueur=[""]*13
        indicjoueur[0]="Les joueurs séléctionner était :"
        for joueur in range(12):
            indicjoueur[0]="Les joueurs séléctionner était :"
            indicjoueur[1+joueur]=joueurselec[joueur]
        indicjoueur=", ".join(indicjoueur)
        indicjoueur=indicjoueur.replace(";,","")
        for fichier in listenomfichier:
            with open(fichier) as fic:
                if fic.readline()!="":
                    #Des joueurs ont déjà était séléctionné
                    if fic.readline()!="":
                        #Il y a des informations dans un fichier
                        if askyesno('','Il existe déjà des données enregistrées souhaiter vous les effacer?\n\n'+indicjoueur,parent=f):
                            mesjoueur()
                            f.destroy()
                            return
                        else:
                            if askyesno('','Voulez-vous aller analyser les données maintenant'):
                                f.destroy()
                                result=1
                            else:
                                showinfo('','Les données que vous allez enregistrés seront ajoutées aux anciennes',parent=f)
                                f.destroy()
                            return
                    else:
                        #Il n'y aucune informations dans le fichier
                        nbficvide=nbficvide+1
                        if nbficvide==24:
                            mesjoueur()
                            f.destroy()
                            return
                else:
                    #Aucun joueur séléctionné
                    mesjoueur()
                    f.destroy()
                    return
    else:
        #le fichier n'existe pas
        mesjoueur()
        f.destroy()
        return


def creafichier():
    """Crée tout les fichiers dont le programme a besoin, avec à l'intérieur en première ligne le nom du joueur"""
    global listenomjoueur,joueurselec
    for joueur in range(12):
        with open(listenomfichier[joueur],'w') as fic:
            envoie=[joueurselec[joueur],"\n"]
            envoie=",".join(envoie)
            fic.write(envoie)
    for joueur in range(12,24):
        with open(listenomfichier[joueur],'w') as fic:
            envoie=[joueurselec[joueur],"\n"]
            envoie=",".join(envoie)
            fic.write(envoie)

def affichageterrain():
    """affiche le terrain"""
    global canvas,curseur
    canvas = Canvas(fenetre, width=1000, height=500, background='white')
    curseur=0
    canvas.bind("<Button-1>", emplacementdonner)
    terrain = canvas.create_rectangle(0,0,1000,500)
    zone = canvas.create_arc(-250,25,250,475, fill="blue",start=270,extent=180)
    zone = canvas.create_arc(750,25,1250,475, fill="yellow",start=90,extent=180)
    rondcentre= canvas.create_oval(425,175,575,325)
    milieu= canvas.create_line(500,0,500,500)
    but=canvas.create_rectangle(0,200,50,300)
    but=canvas.create_rectangle(950,200,1000,300)
    canvas.grid(row = 0,column = 0,columnspan=20)

def mesjoueur():
    """cherche dans le document les prénom-numéro des joueurs et les stochent dans une liste"""
    global joueurselec
    with open('nom_joueur.txt','r') as fic:
        fic.readline()
        nom=fic.readline()
    joueurselec=nom.split(';')
    with open('nom_joueur_adverse.txt','r') as fic:
        fic.readline()
        nom=fic.readline()
    joueurselecadverse=nom.split(';')
    joueurselec.extend(joueurselecadverse)
    creafichier()

def validjoueur():
    """ferme la fenetre pour selectionner les joueurs et lance la fonctions pour crée tout les fichiers"""
    creafichier()
    f.destroy()

def rechercheselec():
    """recherche et récupére dans tout les fichiers des joueurs les noms des joueurs qui sont stocker dedans et les stocke dans la liste joueurselec"""
    global joueurselec,listenomfichier
    n=0
    for fichier in listenomfichier:
        with open(fichier) as fic:
            selec=fic.readline()
            selec=selec.strip()
            joueurselec[n]=selec.replace(',','')
        n=n+1

def selectionnomjoueur():
    """demande le nom des joueurs et retourne le nom et le numéro rentré"""
    return "Serkan-42"
    """input("Entrez le prénom du joueur comme suit:Prénom-numéro")"""

def affichagejoueur():
    """affiche la liste des joueur avec les prenom-numéro choisi ou récupéré dans les fichiers et lance une fonction pour savoir qu'elle est le joueur séléctionner"""
    global indicJ,labjoueur,labjoueurad
    rechercheselec()
    labjoueur=LabelFrame(fenetre, text="Notre équipe",padx=5,pady=5)
    labjoueur.grid(row=2,column=0,columnspan=12)
    Button(labjoueur,text=joueurselec[0],command=lambda : selectionjoueur("J1.csv"),fg="blue").grid(row=0,column=0)
    Button(labjoueur,text=joueurselec[1],command=lambda : selectionjoueur("J2.csv"),fg="blue").grid(row=0,column=1)
    Button(labjoueur,text=joueurselec[2],command=lambda : selectionjoueur("J3.csv"),fg="blue").grid(row=0,column=2)
    Button(labjoueur,text=joueurselec[3],command=lambda : selectionjoueur("J4.csv"),fg="blue").grid(row=0,column=3)
    Button(labjoueur,text=joueurselec[4],command=lambda : selectionjoueur("J5.csv"),fg="blue").grid(row=0,column=4)
    Button(labjoueur,text=joueurselec[5],command=lambda : selectionjoueur("J6.csv"),fg="blue").grid(row=0,column=5)
    Button(labjoueur,text=joueurselec[6],command=lambda : selectionjoueur("J7.csv"),fg="blue").grid(row=0,column=6)
    Button(labjoueur,text=joueurselec[7],command=lambda : selectionjoueur("J8.csv"),fg="blue").grid(row=0,column=7)
    Button(labjoueur,text=joueurselec[8],command=lambda : selectionjoueur("J9.csv"),fg="blue").grid(row=0,column=8)
    Button(labjoueur,text=joueurselec[9],command=lambda : selectionjoueur("J10.csv"),fg="blue").grid(row=0,column=9)
    Button(labjoueur,text=joueurselec[10],command=lambda : selectionjoueur("J11.csv"),fg="blue").grid(row=0,column=10)
    Button(labjoueur,text=joueurselec[11],command=lambda : selectionjoueur("J12.csv"),fg="blue").grid(row=0,column=11)

    labjoueurad=LabelFrame(fenetre, text="Equipe adverse",padx=5,pady=5)
    labjoueurad.grid(row=3,column=0,columnspan=12)
    Button(labjoueurad,text=joueurselec[12],command=lambda : selectionjoueur("JA1.csv"),fg="orange").grid(row=0,column=0)
    Button(labjoueurad,text=joueurselec[13],command=lambda : selectionjoueur("JA2.csv"),fg="orange").grid(row=0,column=1)
    Button(labjoueurad,text=joueurselec[14],command=lambda : selectionjoueur("JA3.csv"),fg="orange").grid(row=0,column=2)
    Button(labjoueurad,text=joueurselec[15],command=lambda : selectionjoueur("JA4.csv"),fg="orange").grid(row=0,column=3)
    Button(labjoueurad,text=joueurselec[16],command=lambda : selectionjoueur("JA5.csv"),fg="orange").grid(row=0,column=4)
    Button(labjoueurad,text=joueurselec[17],command=lambda : selectionjoueur("JA6.csv"),fg="orange").grid(row=0,column=5)
    Button(labjoueurad,text=joueurselec[18],command=lambda : selectionjoueur("JA7.csv"),fg="orange").grid(row=0,column=6)
    Button(labjoueurad,text=joueurselec[19],command=lambda : selectionjoueur("JA8.csv"),fg="orange").grid(row=0,column=7)
    Button(labjoueurad,text=joueurselec[20],command=lambda : selectionjoueur("JA9.csv"),fg="orange").grid(row=0,column=8)
    Button(labjoueurad,text=joueurselec[21],command=lambda : selectionjoueur("JA10.csv"),fg="orange").grid(row=0,column=9)
    Button(labjoueurad,text=joueurselec[22],command=lambda : selectionjoueur("JA11.csv"),fg="orange").grid(row=0,column=10)
    Button(labjoueurad,text=joueurselec[23],command=lambda : selectionjoueur("JA12.csv"),fg="orange").grid(row=0,column=11)
    indicJ=Label(fenetre)

def selectionjoueur(place):
    """recupere le nom du joueur séléctionner et crée une variable global avec le joueur et affiche un indicateur sous le joueur choisi"""
    global joueur,indicJ
    indicJ.destroy()
    joueur=place
    num=listenomfichier.index(joueur)
    if num<=11:
        labequipe=labjoueur
        couleur="blue"
    else:
        num=num-12
        labequipe=labjoueurad
        couleur="orange"
    indicJ=Label(labequipe, text="séléctionné↑",bg=couleur)
    indicJ.grid(row=1,column=num)

def affichageaction():
    """affiche la liste d'action et lance une fonction pour savoir qu'elle est l'action séléctionner"""
    global indicA, labaction
    labaction=LabelFrame(fenetre, text="Action",padx=5,pady=5)
    labaction.grid(row=1,column=3,columnspan=9)
    Button(labaction,text='But',command=lambda : selectionaction('but')).grid(row=0,column=0)
    Button(labaction,text='Passe',command=lambda : selectionaction('passe')).grid(row=0,column=1)
    Button(labaction,text='Stop provoqué',command=lambda : selectionaction('stopprovqué')).grid(row=0,column=2)
    Button(labaction,text='Stop subit',command=lambda : selectionaction('stopsubit')).grid(row=0,column=3)
    Button(labaction,text='Balle perdu',command=lambda : selectionaction('balleperdu')).grid(row=0,column=4)
    Button(labaction,text='Interception',command=lambda : selectionaction('interception')).grid(row=0,column=5)
    Button(labaction,text='Arrêt',command=lambda : selectionaction('arret')).grid(row=0,column=6)
    indicA=Label(fenetre)

def selectionaction(mouv):
    """recupere l'action séléctionner
    Crée une variable global avec l'action et affiche un indicateur sous l'action choisi"""
    global action,indicA,listeaction
    action = mouv
    indicA.destroy()

    num=listeaction.index(action)

    indicA=Label(labaction, text="séléctionné↑",bg="green")
    indicA.grid(row=1,column=num)

def affichagelouperreussi():
    """affiche un bouton pour choisir si l'action et louper ou réussite"""
    global indicL,lablouperreussi
    lablouperreussi=LabelFrame(fenetre, text="L'action est",padx=5,pady=5)
    lablouperreussi.grid(row=1,column=12,columnspan=15)
    reu=Button(lablouperreussi,text='Réussi',command=lambda : selectionlouperreussi('reussi')).grid(row=0,column=0)
    loup=Button(lablouperreussi,text='Louper',command=lambda : selectionlouperreussi('louper')).grid(row=0,column=1)
    indicL=Label(fenetre)

def selectionlouperreussi(lp):
    """recupere si l'action est reussit ou louper
    Crée une variable global dans la qu'elle on met si l'action et louper ou réussi et affiche un indicateur en dessous de reussi ou louper selon ce qui est choisi"""
    global reussite,indicL
    reussite=lp
    indicL.destroy()
    if reussite=="reussi":
        indicL=Label(lablouperreussi, text="séléctionné↑",bg="green")
        indicL.grid(row=1,column=0)
    else:
        indicL=Label(lablouperreussi, text="séléctionné↑",bg="red")
        indicL.grid(row=1,column=1)

def affichageresultat():
    """affiche un bouton résultat qui lance la fonction pour afficher la partit statistique"""
    Button(fenetre,text='Résultat',command=selectionresultat).grid(row=2,column=19)

def selectionresultat():
    """Lance toute les fonctions qui permettent de voir les statistique en fonction de l'action et du joueur séléctionner"""
    global indicA,indicJ,indicL
    if calculestat()!="error":
        choixzone()
        affichageposition()
        affichagestat()
        affichagestatzone()
        lablouperreussi.destroy()
        valid.destroy()
        boutontableur()

def emplacementdonner(event):
    """recupere l'endroit où l'utilisateur à cliquer et le stocke dans deux variables
    affiche un message si l'utilisateur clique en dehors du terrain"""
    global posx,posy,curseur
    posx=0
    posy=0
    x = event.x
    y = event.y
    canvas.delete(curseur)
    if 0<=x<=1000 and 0<=y<=500:
        posx = x
        posy = y
        curseur= canvas.create_oval(posx-3,posy-3,posx+3,posy+3,fill="black")
    else:
        showerror('Vous avez cliqué en dehors du terrian','Veulliez cliquer dans le terrain')

def validation():
    """bouton qui valide les résultat rentré et fait enregistrer les valeur"""
    global valid
    valid=Button(fenetre,text='Validé',command=enregistrerfichier)
    valid.grid(row=1,column=19)

def enregistrerfichier():
    """stocke les information dans un fichier excel
    Entrée:les variables globales contenant le nom du joueur, action, louper/réussi et la position où à été faite l'action
    Sortie: stocke toute les information dans un fichier excel"""
    global posx, posy, action, joueur, reussite
    if posx=='none' or action=='none' or reussite=='none' or joueur=='none':
        if posx=='none':
            showerror("", "Vous n'avez pas séléctionnez la position")
        elif action=='none':
            showerror("", "Vous n'avez pas séléctionnez l'action")
        elif reussite=='none':
            showerror("", "Vous n'avez pas séléctionnez si l'action est réussite")
        elif joueur=='none':
            showerror("", "Vous n'avez pas séléctionnez le joueur")

    else:
        posx=str(posx)
        posy=str(posy)
        envoie=[action,reussite,posx,posy,'\n']
        envoie=",".join(envoie)
        with open(joueur,'a') as fic:
            fic.write(envoie)
        joueur='none'
        action='none'
        posx='none'
        canvas.delete(curseur)
        reussite='none'
        indicA.destroy()
        indicJ.destroy()
        indicL.destroy()

def choixzone():
    """affiche 7 boutons pour savoir si l'utilisateur veut voir les actions sur tout le terrain ou seulement sur une partit"""
    """Button(fenetre,text='Tout le terrain',command=lambda:zonechoisi([0,1001,0,501])).grid(row=1,column=17)
    Button(fenetre,text='Avant droit',command=lambda:zonechoisi([666,1001,250,501])).grid(row=5,column=18)
    Button(fenetre,text='Avant gauche',command=lambda:zonechoisi([666,1001,0,250])).grid(row=3,column=18)
    Button(fenetre,text='Milieu droit',command=lambda:zonechoisi([333,666,250,501])).grid(row=5,column=17)
    Button(fenetre,text='Milieu gauche',command=lambda:zonechoisi([333,666,0,250])).grid(row=3,column=17)
    Button(fenetre,text='Arrière droit',command=lambda:zonechoisi([0,333,250,501])).grid(row=5,column=16)
    Button(fenetre,text='Arrière gauche',command=lambda:zonechoisi([0,333,0,250])).grid(row=3,column=16)"""
    labpos=LabelFrame(fenetre,padx=5,pady=5)
    labpos.grid(row=1,column=16,rowspan=6)
    bouton1 = Radiobutton(labpos, text="Tout le terrain",command=lambda:zonechoisi([0,1001,0,501]),indicatoron =0).pack()
    bouton2 = Radiobutton(labpos, text="Avant droit",command=lambda:zonechoisi([666,1001,250,501]),indicatoron=0).pack()
    bouton3 = Radiobutton(labpos, text="Avant gauche",command=lambda:zonechoisi([666,1001,0,250]),indicatoron=0).pack()
    bouton4 = Radiobutton(labpos, text='Milieu droit',command=lambda:zonechoisi([333,666,250,501]),indicatoron=0).pack()
    bouton5 = Radiobutton(labpos, text='Milieu gauche',command=lambda:zonechoisi([333,666,0,250]),indicatoron=0).pack()
    bouton6 = Radiobutton(labpos, text='Arrière droit',command=lambda:zonechoisi([0,333,250,501]),indicatoron=0).pack()
    bouton7 = Radiobutton(labpos, text='Arrière gauche',command=lambda:zonechoisi([0,333,0,250]),indicatoron=0).pack()



def zonechoisi(endroit):
    """retourne les coordonnées de la zone où l'utilisateur veut voir les emplacement sous la forme[limitegauchex,limdroitex,limitehauty,limitebasy]"""
    global zone
    zone=endroit
    selectionresultat()

def calculestat():
    """recupere toute les stats pour l'action demander et le joueur
    Crée une variable global avec toute les stats pour l'action et le joueur donné sous la forme: stat=[nb total action,nb reussit,[posx],[posy],nb echec,[posx],[posy]]"""
    global action,joueur
    if action=='none' or joueur=='none':
        if action=='none':
            showerror("", "Vous n'avez pas séléctionnez l'action")
        elif joueur=='none':
            showerror("", "Vous n'avez pas séléctionnez le joueur")
        return "error"

    else:
        global stat
        stat=[0,0,[],[],0,[],[]]
        with open(joueur,'r') as fic:
            for ligne in fic:
                doc=ligne.strip()
                doc=ligne.split(',')
                if doc[0]==action:
                    stat[0]=stat[0]+1
                    if doc[1]=='reussi':
                        stat[1]=stat[1]+1
                        posx=doc[2]
                        stat[2].append(posx)
                        posy=doc[3]
                        stat[3].append(posy)
                    else:
                        stat[4]=stat[4]+1
                        posx=doc[2]
                        stat[5].append(posx)
                        posy=doc[3]
                        stat[6].append(posy)
        for coord in range(stat[1]):
            stat[2][coord]=int(stat[2][coord])
            stat[3][coord]=int(stat[3][coord])
        for coord in range(stat[4]):
            stat[5][coord]=int(stat[5][coord])
            stat[6][coord]=int(stat[6][coord])

def affichageposition():
    """Entrée:action séléctionné, joueur selectionné, tout les emplacement de l'action, si elles sont reussit ou non et la zone choisi
    sortie:Affiche les emplacement de toute les actions en vert si elle est réussi et rouge si elle est loupé pour le joueur et l'action donné"""
    affichageterrain()
    global zone, nbreu, nbeche
    nbreu=0
    nbeche=0
    for nb in range(stat[1]):
        if zone[0]<=stat[2][nb]<zone[1] and zone[2]<=stat[3][nb]<zone[3]:
            nbreu=nbreu+1
            emplac=canvas.create_oval(stat[2][nb]-4,stat[3][nb]-4,stat[2][nb]+4,stat[3][nb]+4,fill="green")
    for nb in range(stat[4]):
        if zone[0]<=stat[5][nb]<zone[1] and zone[2]<=stat[6][nb]<zone[3]:
            nbeche=nbeche+1
            emplac=canvas.create_oval(stat[5][nb]-4,stat[6][nb]-4,stat[5][nb]+4,stat[6][nb]+4,fill="red")

def affichagestatzone():
    """Entrée: la zone choisit, nombre de reussite dans la zone choisit et le nombre d'echecs dans la zone
    Affiche le pourcentage de réussite, le nombre de réussite et le nombre d'echecs pour la zone séléctionnez"""
    global pourcentage, R, L, labstat
    pourcentage.destroy()
    R.destroy()
    L.destroy()

    if zone !=[0,1001,0,501]:
        if (nbreu+nbeche)==0:
            pourcentage=Label(labstat, text="Pas d'informations",width="21")
            pourcentage.grid(row=2,column=15)
            R=Label(labstat, text="Pas d'informations",width="21", bg = "green")
            R.grid(row=4,column=15)
            L=Label(labstat, text="Pas d'informations",width="21", bg="red")
            L.grid(row=6,column=15)
        else:
            pourreu=(nbreu/(nbreu+nbeche))*100
            pourreu=round(pourreu,2)
            pourreu="Pourcentage réussite "+str(pourreu)+"%"
            nbreussite=str(nbreu)+" "+action+" reussit"
            nbechec=str(nbeche)+" "+action+" louper"
            pourcentage=Label(labstat, text=pourreu,width="21")
            pourcentage.grid(row=2,column=15)
            R=Label(labstat, text=nbreussite,width="21", bg = "green")
            R.grid(row=4,column=15)
            L=Label(labstat, text=nbechec,width="21", bg="red")
            L.grid(row=6,column=15)

def affichagestat():
     """Entrée: le pourcentage de réussite, le nombre d'action réussit et louper a partir du fichier exel et l'action séléctionner
     Affiche le pourcentage de réussite, le nombre de réussite et le nombre d'echecs pour l'action séléctionnez"""
     global labstat
     labstat=LabelFrame(fenetre, text="Les stats sont:",padx=5,pady=5)
     labstat.grid(row=1,column=15,rowspan=4)
     if stat[0]==0:
        Label(labstat, text="Manque d'informations",width="21").grid(row=1,column=15)
        Label(labstat, text="Manque d'informations",width="21", bg = "green").grid(row=3,column=15)
        Label(labstat, text="Manque d'informations",width="21", bg="red").grid(row=5,column=15)
     else:
        pourreu=(stat[1]/stat[0])*100
        pourreu=round(pourreu,2)
        pourreu="Pourcentage réussite "+str(pourreu)+"%"
        nbreussite=str(stat[1])+" "+action+" reussit en tout"
        nbechec=str(stat[4])+" "+action+" louper en tout"
        Label(labstat, text=pourreu,width="21").grid(row=1,column=15)
        Label(labstat, text=nbreussite,width="21", bg = "green").grid(row=3,column=15)
        Label(labstat, text=nbechec,width="21", bg="red").grid(row=5,column=15)

def tableur():
    """récupère toutes les infos dans tout les fichier
    Crée un grand fichier avec le nombre de réusite sur le nombre totale d'action et le pourcentage de réussite pour chaque action de chaque joueur"""
    global listeaction
    listenomfichier=[["J1.csv","J2.csv","J3.csv","J4.csv","J5.csv","J6.csv","J7.csv","J8.csv","J9.csv","J10.csv","J11.csv","J12.csv"],["JA1.csv","JA2.csv","JA3.csv","JA4.csv","JA5.csv","JA6.csv","JA7.csv","JA8.csv","JA9.csv","JA10.csv","JA11.csv","JA12.csv"]]
    with open('stat_general.csv','w') as fic:
            fic.write("joueur/action,But,Passe,Stop provoque,Stop subit,Balle perdu,Interception,Arret,\n")
    for moy in range(2):
        moyenne=[0]*7
        infoabs=[0]*7
        for joueur in listenomfichier[moy]:
            with open(joueur,'r') as fic:
                personne=fic.readline()
            personne=personne.strip()
            envoie=[""]*9
            envoie[0]=personne
            envoie[8]='\n'
            place=1
            for action in listeaction:
                stat=[0,0,0]
                with open(joueur,'r') as fic:
                    for ligne in fic:
                        doc=ligne.strip()
                        doc=ligne.split(',')
                        if doc[0]==action:
                            stat[0]=stat[0]+1
                            if doc[1]=='reussi':
                                stat[1]=stat[1]+1
                            else:
                                stat[2]=stat[2]+1
                if stat[0]!=0:
                    pourcentage=(stat[1]/stat[0])*100
                    pourcentage=round(pourcentage,2)
                    moyenne[place-1]=moyenne[place-1]+pourcentage
                    pourcentage=str(pourcentage)
                    stat[0]=str(stat[0])
                    stat[1]=str(stat[1])
                    case=[stat[1]," reussi sur ",stat[0]," soit ",pourcentage,"%"]
                    case="".join(case)
                    envoie[place]=case
                    place=place+1
                else:
                    envoie[place]="Manque d'information"
                    infoabs[place-1]=infoabs[place-1]+1
                    place=place+1
            envoie=",".join(envoie)
            envoie=envoie.replace(',,',',')
            with open('stat_general.csv','a') as fic:
                fic.write(envoie)
        for act in range(7):
            if infoabs[act]==12:
                moyenne[act]="Il n y a aucune informations"
            else:
                moyenne[act]=moyenne[act]/(12-infoabs[act])
                moyenne[act]=round(moyenne[act])
                moyenne[act]=str(moyenne[act])
        with open('stat_general.csv','a') as fic:
                fic.write("Moyenne du pourcentage du reussite pour l'equipe,")
                for moyen in range(7):
                    fic.write(moyenne[moyen])
                    fic.write(",")
                fic.write("\n")
    with open('stat_general.csv','a') as fic:
        fic.write("Moyenne du pourcentage du reussite pour les 2 equipes,=(B9+B17)/2,=(C9+C17)/2,=(D9+D17)/2,=(E9+E17)/2,=(F9+F17)/2,=(G9+G17)/2,=(H9+H17)/2")
    showinfo('', 'Un tableur a été crée avec toutes les statistiques de chaque joueur')

def boutontableur():
    """Affiche un bouton pour activer la fonction "tableur"""
    Button(fenetre,text="Tableur",command=tableur).grid(row=1,column=19)

def boutonexit():
    """Affiche unn bouton pour sortir du programme et pour effacer ou pas les données"""
    sortir= Button(fenetre,text='Quitter',command=exit).grid(row=3,column=19)

def exit():
    """Demande si il faut enlever toutes les informations de chaque fichier pour pouvoir re-écrire sur les même fichiers à la prochaine utilisation
    ou si il faut garder les informations enregistré"""
    fenetre.destroy()


posx='none'
joueur='none'
action='none'
reussite='none'
listeaction=["but","passe","stopprovqué","stopsubit","balleperdu","interception","arret"]
listenomfichier=["J1.csv","J2.csv","J3.csv","J4.csv","J5.csv","J6.csv","J7.csv","J8.csv","J9.csv","J10.csv","J11.csv","J12.csv","JA1.csv","JA2.csv","JA3.csv","JA4.csv","JA5.csv","JA6.csv","JA7.csv","JA8.csv","JA9.csv","JA10.csv","JA11.csv","JA12.csv"]
zone=[0,1001,0,501]
joueurselec=[""]*24
result=0

f=Tk()
veriffichier(listenomfichier)
f.mainloop()

fenetre =Tk()
affichageterrain()
pourcentage=Label(fenetre)
R=Label(fenetre)
L=Label(fenetre)
affichageaction()
affichageresultat()
affichagejoueur()
validation()
boutonexit()
affichagelouperreussi()
if result==1:
    action=""
    joueur="J1.csv"
    selectionresultat()
fenetre.mainloop()