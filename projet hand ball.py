from tkinter import *
from tkinter.messagebox import*

def affichageterrain():
    """affiche le terrain"""
    global canvas,curseur
    canvas = Canvas(fenetre, width=1000, height=500, background='white')
    curseur=0
    canvas.bind("<Button-1>", emplacementdonner)
    canvas.create_rectangle(0,0,1000,500)
    canvas.create_arc(-250,25,250,475, fill="blue",start=270,extent=180)
    canvas.create_arc(750,25,1250,475, fill="yellow",start=90,extent=180)
    canvas.create_oval(425,175,575,325)
    canvas.create_line(500,0,500,500)
    canvas.create_rectangle(0,200,50,300)
    canvas.create_rectangle(950,200,1000,300)
    canvas.grid(row = 0,column = 0,columnspan=20)

def selectionnomjoueur():
    """demande le nom des joueurs et les mets dans une liste"""
    return input("Entrez le prénom du joueur comme suit:Prénom-numéro")

def affichagejoueur():
    """affiche la liste des joueur"""
    """fait par Serkan"""
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("J1.csv"),fg="blue").grid(row=3,column=3)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("J2.csv"),fg="blue").grid(row=3,column=4)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("J3.csv"),fg="blue").grid(row=3,column=5)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("J4.csv"),fg="blue").grid(row=3,column=6)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("J5.csv"),fg="blue").grid(row=3,column=7)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("J6.csv"),fg="blue").grid(row=3,column=8)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("J7.csv"),fg="blue").grid(row=3,column=9)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("JA1.csv"),fg="orange").grid(row=5,column=3)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("JA2.csv"),fg="orange").grid(row=5,column=4)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("JA3.csv"),fg="orange").grid(row=5,column=5)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("JA4.csv"),fg="orange").grid(row=5,column=6)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("JA5.csv"),fg="orange").grid(row=5,column=7)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("JA6.csv"),fg="orange").grid(row=5,column=8)
    Button(fenetre,text=selectionnomjoueur(),command=lambda : selectionjoueur("JA7.csv"),fg="orange").grid(row=5,column=9)
def selectionjoueur(place):
    """recupere le nom du joueur séléctionner
    Crée une variable global avec le joueur"""
    global joueur
    joueur=place

def affichageaction():
    """affiche la liste d'action"""
    """fait par Serkan"""
    Button(fenetre,text='But',command=lambda : selectionaction('but')).grid(row=1,column=3)
    Button(fenetre,text='Passe',command=lambda : selectionaction('passe')).grid(row=1,column=4)
    Button(fenetre,text='Stop provoqué',command=lambda : selectionaction('stopprovqué')).grid(row=1,column=5)
    Button(fenetre,text='Stop subit',command=lambda : selectionaction('stopsubit')).grid(row=1,column=6)
    Button(fenetre,text='Balle perdu',command=lambda : selectionaction('balleperdu')).grid(row=1,column=7)
    Button(fenetre,text='Interception',command=lambda : selectionaction('interception')).grid(row=1,column=8)
def selectionaction(mouv):
    """recupere l'action séléctionner
    Crée une variable global avec l'action"""
    """fait par Serkan"""
    global action
    action = mouv

def affichagelouperreussi():
    """affiche l'option reussit ou louper"""
    """fait par Alexis"""
    Button(fenetre,text='Réussi',command=lambda : selectionlouperreussi('reussi')).grid(row=1,column=15)
    Button(fenetre,text='Louper',command=lambda : selectionlouperreussi('louper')).grid(row=1,column=16)
def selectionlouperreussi(lp):
    """recupere si l'action est reussit ou louper
    Crée une variable global avec le résultat"""
    """fait par Alexis"""
    global reussite
    reussite=lp
def affichageresultat():
    """affiche un bouton résultat"""
    Button(fenetre,text='Résultat',command=selectionresultat).grid(row=3,column=19)
def selectionresultat():
    """recupere si l'utilisateur appuye sur résultat
    renvoie une variable pour voir les résultats"""

def emplacementdonner(event):
    """recupere l'endroit où l'utilisateur à cliquer et le stocke dans une variable"""
    global posx,posy,curseur
    posx = event.x
    posy = event.y
    canvas.delete(curseur)
    curseur= canvas.create_oval(posx-3,posy-3,posx+3,posy+3,fill="black")

def validation():
    """bouton qui valide les résultat rentré et fait enregistrer les valeur"""
    Button(fenetre,text='Validé',command=enregistrerfichier).grid(row=1,column=19)

def enregistrerfichier():
    """stocke les information dans un fichier excel
    Entrée:les variables globales contenant le nom du joueur, action, louper/réussi et la position où à été faite l'action
    Sortie: stocke toute les information dans un fichier excel"""
    global posx, posy, action, joueur, reussite
    if posx=='none' or action=='none' or reussite=='none' or joueur=='none':
        if posx=='none':
            showerror("Titre 4", "Vous n'avez pas séléctionnez la position")
        elif action=='none':
            showerror("Titre 4", "Vous n'avez pas séléctionnez l'action")
        elif reussite=='none':
            showerror("Titre 4", "Vous n'avez pas séléctionnez si l'action est réussite")
        elif joueur=='none':
            showerror("Titre 4", "Vous n'avez pas séléctionnez le joueur")

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

def calculestat():
    """recupere le nombre de reussi et de gagner pour l'action demander
    Crée une variable global avec le pourcentage de réussite pour l'action"""
    """fait par Alexis"""
def affichageposition():
    """Entrée:action séléctionné, joueur selectionné, tout les emplacement de l'action et si elles sont reussit ou non
    sortie:Affiche les emplacement de toute les actions en vert si elle est réussi et rouge si elle est loupé pour un joueur et une action donné"""
def affichagestat():
     """Entrée: le pourcentage de réussite, le nombre d'action réussit et louper a partir du fichier exel et le joueur séléctionner
     Affiche le pourcentage de réussite à coté de chaque action et le nombre de réussite-le nombre d'echecs acoté du pourcentage """


posx='none'
joueur='none'
action='none'
reussite='none'
fenetre = Tk()
affichageaction()
affichageterrain()
affichageresultat()
affichagejoueur()
affichagelouperreussi()
validation()
fenetre.mainloop()
