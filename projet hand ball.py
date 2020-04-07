﻿from tkinter import *
fenetre = Tk()
def affichageterrain():
    """affiche le terrain"""
    canvas = Canvas(fenetre, width=800, height=400, background='white')
    balle = canvas.create_oval(-200,20,200,380, fill="blue")
    balle = canvas.create_oval(600,20,1000,380, fill="yellow")
    rondcentre= canvas.create_oval(340,140,460,260)
    milieu= canvas.create_line(400,0,400,400)
    but=canvas.create_rectangle(0,160,40,240)
    but=canvas.create_rectangle(760,160,800,240)
    texte=canvas.create_text(27,7,text="coté allier")
    canvas.grid()
def selectionnomjoueur():
    """demande le nom des joueurs et les mets dans une liste"""

def affichagejoueur():
    """affiche la liste des joueur"""
    """fait par Serkan"""
def selectionjoueur():
    """recupere le nom du joueur séléctionner et le met dans une variable"""
    """fait par Alexis"""
def affichageaction():
    """affiche la liste d'action"""
    """fait par Serkan"""
def selectionaction():
    """recupere l'action séléctionner et le met dans une variable"""
    """fait par Serkan"""
def affichagelouperreussi():
    """affiche l'option reussit ou louper"""
    """fait par Alexis"""
def selectionlouperreussi():
    """recupere si l'action est reussit ou louper et le met dans une variable"""
    """fait par Alexis"""
def affichageresultat():
    """affiche un bouton résultat"""
def selectionresultat():
    """recupere si l'utilisateur appuye sur résultat
    renoie une variable pour voir les résultats variable"""
def emplacementdonner():
    """recupere l'endroit où l'utilisateur à cliquer et le stocke dans une variable"""
def enregistrerfichier(joueur,action,reussit,positionx,positiony):
    """stocke les information dans un fichier excel
    Entrée: nom du joueur, action, louper/réussi et la position où à été faite l'action
    Sortie: stocke toute les information dans un fichier excel"""
    positionx=str(positionx)
    positiony=str(positiony)
    nomfic= joueur + ".csv"
    envoie=[action,reussit,positionx,positiony,'\n']
    envoie=",".join(envoie)
    with open(nomfic,'a') as fic:
        fic.write(envoie)
def calculestat():
    """recupere le nombre de reussi et de gagner pour l'action demander
    renvoie le pourcentage de réussite pour l'action"""
    """fait par Alexis"""
def affichageposition():
    """Entrée:action séléctionné, joueur selectionné, tout les emplacement de l'action et si elles sont reussit ou non
    sortie:Affiche les emplacement de toute les actions en vert si elle est réussi et rouge si elle est loupé pour un joueur et une action donné"""
def affichagestat():
     """Entrée: le pourcentage de réussite, le nombre d'action réussit et louper a partir du fichier exel et le joueur séléctionner
     Affiche le pourcentage de réussite à coté de chaque action et le nombre de réussite-le nombre d'echecs acoté du pourcentage """

affichageterrain()
fenetre.mainloop()