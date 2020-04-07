from tkinter import *
fenetre = Tk()
def affichageterrain():
    """affiche le terrain"""
    canvas = Canvas(fenetre, width=800, height=400, background='white')
    canvas.bind("<Button-1>", emplacementdonner)
    terrain = canvas.create_rectangle(0,0,800,400)
    zone = canvas.create_oval(-200,20,200,380, fill="blue")
    zone = canvas.create_arc(600,20,1000,380, fill="yellow",start=90,extent=180)
    rondcentre= canvas.create_oval(340,140,460,260)
    milieu= canvas.create_line(400,0,400,400)
    but=canvas.create_rectangle(0,160,40,240)
    but=canvas.create_rectangle(760,160,800,240)
    texte=canvas.create_text(27,7,text="coté allier")
    canvas.grid(row = 0,column = 0,columnspan=20)

def selectionnomjoueur():
    """demande le nom des joueurs et les mets dans une liste"""

def affichagejoueur():
    """affiche la liste des joueur"""
    """fait par Serkan"""
def selectionjoueur():
    """recupere le nom du joueur séléctionner
    Crée une variable global avec le joueur"""
    """fait par Alexis"""

def affichageaction():
    """affiche la liste d'action"""
    """fait par Serkan"""
def selectionaction():
    """recupere l'action séléctionner
    Crée une variable global avec l'action"""
    """fait par Serkan"""

def affichagelouperreussi():
    """affiche l'option reussit ou louper"""
    """fait par Alexis"""
def selectionlouperreussi():
    """recupere si l'action est reussit ou louper
    Crée une variable global avec le résultat"""
    """fait par Alexis"""

def affichageresultat():
    """affiche un bouton résultat"""
def selectionresultat():
    """recupere si l'utilisateur appuye sur résultat
    renvoie une variable pour voir les résultats"""

def emplacementdonner(event):
    """recupere l'endroit où l'utilisateur à cliquer et le stocke dans une variable"""
    global posx,posy
    posx = event.x
    posy = event.y


def validation():
    """bouton qui valide les résultat rentré et fait enregistrer les valeur"""
    bouton=Button(fenetre,text='Validé',command=enregistrerfichier).grid(row=1,column=19)

def enregistrerfichier():
    """stocke les information dans un fichier excel
    Entrée:les variables globales contenant le nom du joueur, action, louper/réussi et la position où à été faite l'action
    Sortie: stocke toute les information dans un fichier excel"""
    global posx, posy
    posx=str(posx)
    posy=str(posy)
    nomfic= joueur + ".csv"
    envoie=[action,reussit,posx,posy,'\n']
    envoie=",".join(envoie)
    with open(nomfic,'a') as fic:
        fic.write(envoie)
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


affichageterrain()
validation()

fenetre.mainloop()