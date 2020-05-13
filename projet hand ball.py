from tkinter import *
from tkinter.messagebox import*
from math import *
import os.path

def veriffichier():
    """verifier l'état des fichier
    si ils n'existent pas, il les créent
    si ils existent, il vérifi si ils sont vide, si non demande si on garde les données"""
    global listenomfichier,action,joueur,joueurselec,f

    listenomfichier=["J1.csv","J2.csv","J3.csv","J4.csv","J5.csv","J6.csv","J7.csv","JA1.csv","JA2.csv","JA3.csv","JA4.csv","JA5.csv","JA6.csv","JA7.csv"]
    if os.path.isfile('J1.csv'):
        #le fichier existe
        for fichier in listenomfichier:
            with open(fichier) as fic:
                if fic.readline()!="":
                    if fic.readline()!="":
                        if askyesno('','Il existe déjà des données enregistrées souhaiter vous les effacer?',parent=f):
                            if askyesno('','Voulez vous garder les joueurs séléctionné la fois précédente ?',parent=f):
                                rechercheselec()
                                creafichier()
                                f.destroy()
                                return
                            else:
                                mesjoueur()
                                showinfo('','Toutes données ont été supprimées',parent=f)
                                return
                        else:
                            showinfo('','Les données que vous allez enregistrés seront ajoutées aux anciennes',parent=f)
                            f.destroy()
                            return
                    else:
                        if askyesno('','Voulez vous garder les joueurs séléctionné la fois précédente ?',parent=f):
                            rechercheselec()
                            creafichier()
                            f.destroy()
                            return
                        else:
                            mesjoueur()
                            return
                else:
                    mesjoueur()
                    return
    else:
        #le fichier n'existe pas
        mesjoueur()
        return

def creafichier():
    """Crée tout les fichiers dont le programme a besoin, avec à l'intérieur en première ligne le nom du joueur"""
    global listenomjoueur,joueurselec
    for joueur in range(7):
        with open(listenomfichier[joueur],'w') as fic:
            envoie=[joueurselec[joueur],"\n"]
            envoie=",".join(envoie)
            fic.write(envoie)
    for joueur in range(7,14):
        with open(listenomfichier[joueur],'w') as fic:
            envoie=[listenomfichier[joueur],"\n"]
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


def qljoueur(joueur):
    """récupére les joueurs des joueur séléctionner et les stock dans la liste joueurselec"""
    global joueurselec
    nb=joueurselec.index("")
    joueurselec[nb]=joueur


def mesjoueur():
    """cherche dans le document les prénom-numéro des joueurs et affiche des boutons avec les nom récupéré"""
    global f
    with open('nom_joueur.txt','r') as fic:
        fic.readline()
        nom=fic.readline()
        nom=nom.split(';')
    Label(f,text="Choississez vos 7 joueurs").grid(row=0,column=0,columnspan=3)
    Button(f,text=nom[0],command=lambda : qljoueur(nom[0])).grid(row=1,column=0)
    Button(f,text=nom[1],command=lambda : qljoueur(nom[1])).grid(row=1,column=1)
    Button(f,text=nom[2],command=lambda : qljoueur(nom[2])).grid(row=1,column=2)
    Button(f,text=nom[3],command=lambda : qljoueur(nom[3])).grid(row=2,column=0)
    Button(f,text=nom[4],command=lambda : qljoueur(nom[4])).grid(row=2,column=1)
    Button(f,text=nom[5],command=lambda : qljoueur(nom[5])).grid(row=2,column=2)
    Button(f,text=nom[6],command=lambda : qljoueur(nom[6])).grid(row=2,column=3)
    Button(f,text=nom[7],command=lambda : qljoueur(nom[7])).grid(row=3,column=0)
    Button(f,text=nom[8],command=lambda : qljoueur(nom[8])).grid(row=3,column=1)
    Button(f,text=nom[9],command=lambda : qljoueur(nom[9])).grid(row=3,column=2)
    Button(f,text="valider",command=validjoueur).grid(row=4,column=1)

def validjoueur():
    """ferme la fenetre pour selectionner les joueurs et lance la fonctions pour crée tout les fichiers"""
    creafichier()
    f.destroy()

def rechercheselec():
    """recherche et récupére dans tout les fichiers des joueurs les noms des joueurs qui sont stocker dedans et les stocke dans la liste joueurselec"""
    global joueurselec
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
    global indicJ
    rechercheselec()
    Button(fenetre,text=joueurselec[0],command=lambda : selectionjoueur("J1.csv"),fg="blue").grid(row=3,column=3)
    Button(fenetre,text=joueurselec[1],command=lambda : selectionjoueur("J2.csv"),fg="blue").grid(row=3,column=4)
    Button(fenetre,text=joueurselec[2],command=lambda : selectionjoueur("J3.csv"),fg="blue").grid(row=3,column=5)
    Button(fenetre,text=joueurselec[3],command=lambda : selectionjoueur("J4.csv"),fg="blue").grid(row=3,column=6)
    Button(fenetre,text=joueurselec[4],command=lambda : selectionjoueur("J5.csv"),fg="blue").grid(row=3,column=7)
    Button(fenetre,text=joueurselec[5],command=lambda : selectionjoueur("J6.csv"),fg="blue").grid(row=3,column=8)
    Button(fenetre,text=joueurselec[6],command=lambda : selectionjoueur("J7.csv"),fg="blue").grid(row=3,column=9)

    Button(fenetre,text=joueurselec[7],command=lambda : selectionjoueur("JA1.csv"),fg="blue").grid(row=5,column=3)
    Button(fenetre,text=joueurselec[8],command=lambda : selectionjoueur("JA2.csv"),fg="blue").grid(row=5,column=4)
    Button(fenetre,text=joueurselec[9],command=lambda : selectionjoueur("JA3.csv"),fg="blue").grid(row=5,column=5)
    Button(fenetre,text=joueurselec[10],command=lambda : selectionjoueur("JA4.csv"),fg="blue").grid(row=5,column=6)
    Button(fenetre,text=joueurselec[11],command=lambda : selectionjoueur("JA5.csv"),fg="blue").grid(row=5,column=7)
    Button(fenetre,text=joueurselec[12],command=lambda : selectionjoueur("JA6.csv"),fg="blue").grid(row=5,column=8)
    Button(fenetre,text=joueurselec[13],command=lambda : selectionjoueur("JA7.csv"),fg="blue").grid(row=5,column=9)
    indicJ=Label(fenetre)

def selectionjoueur(place):
    """recupere le nom du joueur séléctionner et crée une variable global avec le joueur et affiche un indicateur sous le joueur choisi"""
    global joueur,indicJ
    indicJ.destroy()
    joueur=place
    num=listenomfichier.index(joueur)
    if num<=6:
        indicJ=Label(fenetre, text="séléctionné↑",bg="blue")
        indicJ.grid(row=4,column=3+num)
    else:
        num=num-7
        indicJ=Label(fenetre, text="séléctionné↑",bg="blue")
        indicJ.grid(row=6,column=3+num)

def affichageaction():
    """affiche la liste d'action et lance une fonction pour savoir qu'elle est l'action séléctionner"""
    global indicA
    Button(fenetre,text='But',command=lambda : selectionaction('but')).grid(row=1,column=3)
    Button(fenetre,text='Passe',command=lambda : selectionaction('passe')).grid(row=1,column=4)
    Button(fenetre,text='Stop provoqué',command=lambda : selectionaction('stopprovqué')).grid(row=1,column=5)
    Button(fenetre,text='Stop subit',command=lambda : selectionaction('stopsubit')).grid(row=1,column=6)
    Button(fenetre,text='Balle perdu',command=lambda : selectionaction('balleperdu')).grid(row=1,column=7)
    Button(fenetre,text='Interception',command=lambda : selectionaction('interception')).grid(row=1,column=8)
    Button(fenetre,text='Arrêt',command=lambda : selectionaction('arret')).grid(row=1,column=9)
    indicA=Label(fenetre)

def selectionaction(mouv):
    """recupere l'action séléctionner
    Crée une variable global avec l'action et affiche un indicateur sous l'action choisi"""
    global action,indicA,listeaction
    action = mouv
    indicA.destroy()

    num=listeaction.index(action)
    if num<=6:
        indicA=Label(fenetre, text="séléctionné↑",bg="green")
        indicA.grid(row=2,column=3+num)

def affichagelouperreussi():
    """affiche un bouton pour choisir si l'action et louper ou réussite"""
    global indicL,reu,loup
    reu=Button(fenetre,text='Réussi',command=lambda : selectionlouperreussi('reussi'))
    reu.grid(row=1,column=15)
    loup=Button(fenetre,text='Louper',command=lambda : selectionlouperreussi('louper'))
    loup.grid(row=1,column=16)
    indicL=Label(fenetre)

def selectionlouperreussi(lp):
    """recupere si l'action est reussit ou louper
    Crée une variable global dans la qu'elle on met si l'action et louper ou réussi et affiche un indicateur en dessous de reussi ou louper selon ce qui est choisi"""
    global reussite,indicL
    reussite=lp
    indicL.destroy()
    if reussite=="reussi":
        indicL=Label(fenetre, text="séléctionné↑",bg="green")
        indicL.grid(row=2,column=15)
    else:
        indicL=Label(fenetre, text="séléctionné↑",bg="red")
        indicL.grid(row=2,column=16)

def affichageresultat():
    """affiche un bouton résultat qui lance la fonction pour afficher la partit statistique"""
    Button(fenetre,text='Résultat',command=selectionresultat).grid(row=4,column=19)

def selectionresultat():
    """Lance toute les fonctions qui permettent de voir les statistique en fonction de l'action et du joueur séléctionner"""
    global indicA,indicJ,indicL
    if calculestat()!="error":
        choixzone()
        affichageposition()
        affichagestat()
        affichagestatzone()
        reu.destroy()
        loup.destroy()
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
    Button(fenetre,text='Validé',command=enregistrerfichier).grid(row=2,column=19)

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
    Button(fenetre,text='Tout le terrain',command=lambda:zonechoisi([0,1001,0,501])).grid(row=1,column=17)
    Button(fenetre,text='Avant droit',command=lambda:zonechoisi([666,1001,250,501])).grid(row=5,column=18)
    Button(fenetre,text='Avant gauche',command=lambda:zonechoisi([666,1001,0,250])).grid(row=3,column=18)
    Button(fenetre,text='Milieu droit',command=lambda:zonechoisi([333,666,250,501])).grid(row=5,column=17)
    Button(fenetre,text='Milieu gauche',command=lambda:zonechoisi([333,666,0,250])).grid(row=3,column=17)
    Button(fenetre,text='Arrière droit',command=lambda:zonechoisi([0,333,250,501])).grid(row=5,column=16)
    Button(fenetre,text='Arrière gauche',command=lambda:zonechoisi([0,333,0,250])).grid(row=3,column=16)

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
    global pourcentage, R, L
    pourcentage.destroy()
    R.destroy()
    L.destroy()
    if zone !=[0,1001,0,501]:
        if (nbreu+nbeche)==0:
            pourcentage=Label(fenetre, text="Pas d'informations",width="21")
            pourcentage.grid(row=2,column=15)
            R=Label(fenetre, text="Pas d'informations",width="21", bg = "green")
            R.grid(row=4,column=15)
            L=Label(fenetre, text="Pas d'informations",width="21", bg="red")
            L.grid(row=6,column=15)
        else:
            pourreu=(nbreu/(nbreu+nbeche))*100
            pourreu=round(pourreu,2)
            pourreu="Pourcentage réussite "+str(pourreu)+"%"
            nbreussite=str(nbreu)+" "+action+" reussit"
            nbechec=str(nbeche)+" "+action+" louper"
            pourcentage=Label(fenetre, text=pourreu,width="21")
            pourcentage.grid(row=2,column=15)
            R=Label(fenetre, text=nbreussite,width="21", bg = "green")
            R.grid(row=4,column=15)
            L=Label(fenetre, text=nbechec,width="21", bg="red")
            L.grid(row=6,column=15)

def affichagestat():
     """Entrée: le pourcentage de réussite, le nombre d'action réussit et louper a partir du fichier exel et l'action séléctionner
     Affiche le pourcentage de réussite, le nombre de réussite et le nombre d'echecs pour l'action séléctionnez"""
     if stat[0]==0:
        Label(fenetre, text="Manque d'informations",width="21").grid(row=1,column=15)
        Label(fenetre, text="Manque d'informations",width="21", bg = "green").grid(row=3,column=15)
        Label(fenetre, text="Manque d'informations",width="21", bg="red").grid(row=5,column=15)
     else:
        pourreu=(stat[1]/stat[0])*100
        pourreu=round(pourreu,2)
        pourreu="Pourcentage réussite "+str(pourreu)+"%"
        nbreussite=str(stat[1])+" "+action+" reussit en tout"
        nbechec=str(stat[4])+" "+action+" louper en tout"
        Label(fenetre, text=pourreu,width="21").grid(row=1,column=15)
        Label(fenetre, text=nbreussite,width="21", bg = "green").grid(row=3,column=15)
        Label(fenetre, text=nbechec,width="21", bg="red").grid(row=5,column=15)

def tableur():
    """récupère toutes les infos dans tout les fichier
    Crée un grand fichier avec le nombre de réusite sur le nombre totale d'action et le pourcentage de réussite pour chaque action de chaque joueur"""
    global listenomfichier,listeaction
    with open('stat_general.csv','w') as fic:
            fic.write("joueur/action,But,Passe,Stop provoqué,Stop subit,Balle perdu,Interception,Arrêt,\n")
    for joueur in listenomfichier:
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
                pourcentage=str(pourcentage)
                stat[0]=str(stat[0])
                stat[1]=str(stat[1])
                case=[stat[1]," réussi sur ",stat[0]," soit ",pourcentage,"%"]
                case="".join(case)
                envoie[place]=case
                place=place+1
            else:
                envoie[place]="Manque d'information"
                place=place+1
        envoie=",".join(envoie)
        envoie=envoie.replace(',,',',')
        with open('stat_general.csv','a') as fic:
            fic.write(envoie)
    showinfo('', 'Un tableur a été crée avec toutes les statistiques de chaque joueur')

def boutontableur():
    """Affiche un bouton pour activer la fonction "tableur"""
    Button(fenetre,text="Tableur",command=tableur).grid(row=2,column=19)


def boutonexit():
    """Affiche unn bouton pour sortir du programme et pour effacer ou pas les données"""
    sortir= Button(fenetre,text='Quitter',command=exit).grid(row=6,column=19)

def exit():
    """Demande si il faut enlever toutes les informations de chaque fichier pour pouvoir re-écrire sur les même fichiers à la prochaine utilisation
    ou si il faut garder les informations enregistré"""
    if askyesno('', 'Voulez vous effacer toute les données enregistré'):
        for joueur in range(14):
            with open(listenomfichier[joueur],'w') as fic:
                fic.write("")
        showinfo('', 'Les données ont été supprimé')
        fenetre.destroy()
    else:
        fenetre.destroy()


joueurselec=[""]*14
f=Tk()
veriffichier()
f.mainloop()



zone=[0,1001,0,501]
posx='none'
joueur='none'
action='none'
reussite='none'
listeaction=["but","passe","stopprovqué","stopsubit","balleperdu","interception","arret"]
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
fenetre.mainloop()








