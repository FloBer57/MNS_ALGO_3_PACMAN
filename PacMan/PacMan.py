#Test PACMAN

import random
import os 



mur_vertical = "║"
mur_horizontal = "═"
coin_haut_gauche = "╔"
coin_haut_droite = "╗"
coin_bas_gauche = "╚"
coin_bas_droite = "╝"
coin_vers_bas = "╦"
coin_vers_droite = "╠"
coin_vers_gauche ="╣"
coin_vers_haut = "╩"
vide = " "
playerG = "ᗤ"
playerD = "ᗧ"
player = "ᗧ"
ghost = "ᗣ"
ghost_un = "๑"
ghost_deux = "ʘ" 
pac_gomme = '●'
list_choice = ["z", "q", "s", "d"]
score = '0'
dead = '☠'
tp = 'v'
tp_deux = 'p'

murs = [mur_vertical,mur_horizontal,coin_haut_gauche,coin_haut_droite,coin_bas_gauche,coin_bas_droite,coin_vers_bas,coin_vers_droite,coin_vers_gauche,coin_vers_haut,tp]
#Voici mon tableau, je viens de voir qu'on peux utiliser des *
lab = [
    [vide, coin_haut_gauche, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, coin_haut_droite, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, mur_horizontal, coin_haut_droite, pac_gomme, mur_horizontal, mur_horizontal, coin_vers_bas, mur_horizontal, mur_horizontal, pac_gomme, coin_haut_gauche, mur_horizontal, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, coin_vers_droite, mur_horizontal, pac_gomme, mur_vertical, pac_gomme, mur_horizontal, mur_horizontal, coin_vers_haut, mur_horizontal, mur_horizontal, pac_gomme, mur_vertical, pac_gomme, mur_horizontal, coin_vers_gauche, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme,pac_gomme, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, mur_horizontal, coin_bas_droite, pac_gomme, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, pac_gomme, coin_bas_gauche, mur_horizontal, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [mur_horizontal, coin_vers_haut, mur_horizontal, mur_horizontal, mur_horizontal, pac_gomme, coin_haut_gauche, vide, mur_horizontal, vide, coin_haut_droite, pac_gomme, mur_horizontal, mur_horizontal, mur_horizontal, coin_vers_haut, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal],
    [vide, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, vide, vide, vide, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, vide,vide,vide,vide],
    [mur_horizontal, coin_vers_bas, mur_horizontal, mur_horizontal, mur_horizontal, pac_gomme, coin_bas_gauche, mur_horizontal, mur_horizontal, mur_horizontal, coin_bas_droite, pac_gomme, mur_horizontal, mur_horizontal, mur_horizontal, coin_vers_bas, mur_horizontal, mur_horizontal,mur_horizontal,mur_horizontal],
    [vide, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, mur_horizontal, coin_haut_droite, pac_gomme, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, pac_gomme, coin_haut_gauche, mur_horizontal, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme,pac_gomme, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, coin_vers_droite, mur_horizontal, pac_gomme, mur_vertical, pac_gomme, mur_horizontal, mur_horizontal, coin_vers_bas, mur_horizontal, mur_horizontal, pac_gomme, mur_vertical, pac_gomme, mur_horizontal, coin_vers_gauche, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, pac_gomme, mur_vertical, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, mur_horizontal, coin_bas_droite, pac_gomme, mur_horizontal, mur_horizontal, coin_vers_haut, mur_horizontal, mur_horizontal, pac_gomme, coin_bas_gauche, mur_horizontal, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, vide],
    [vide, coin_bas_gauche, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, mur_horizontal, coin_bas_droite, vide, vide, vide, vide],
]

#    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,]
#    [0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,]
#    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 3, 0,]
#    [0, 2.5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2.5, 0, 0, 0, 0,]
#    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,]
#    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,]

player_pos = [1, 2]
lab[player_pos[0]][player_pos[1]] = player

ghost_pos = [9,8]
lab[ghost_pos[0]][ghost_pos[1]] = ghost

ghost_pos_un = [9,9]
lab[ghost_pos_un[0]][ghost_pos_un[1]] = ghost_un

ghost_pos_deux = [9,7]
lab[ghost_pos_deux[0]][ghost_pos_deux[1]] = ghost_deux

score_pos = [6,18]
lab[score_pos[0]][score_pos[1]] = score


def printmap():
    for ii in lab:
        i_str = " ".join(ii)
        print(i_str)


def ghost_move(var):
    while True :
        var = random.choice(list_choice)
        if var == "z" and lab[ghost_pos[0] - 1][ghost_pos[1]] not in murs :
            ghost_pos[0] -= 1
            break
        if var == "q" and lab[ghost_pos[0]][ghost_pos[1] -1] not in murs :
            ghost_pos[1] -= 1
            break
        if var == "s" and lab[ghost_pos[0] + 1][ghost_pos[1]] not in murs :
            ghost_pos[0] += 1
            break
        if var == "d" and lab[ghost_pos[0]][ghost_pos[1] + 1] not in murs :
            ghost_pos[1] += 1
            break

def ghost_un_move(var):
    while True :
        var = random.choice(list_choice)
        if var == "z" and lab[ghost_pos_un[0] - 1][ghost_pos_un[1]] not in murs :
            ghost_pos_un[0] -= 1
            break
        if var == "q" and lab[ghost_pos_un[0]][ghost_pos_un[1] -1] not in murs :
            ghost_pos_un[1] -= 1
            break
        if var == "s" and lab[ghost_pos_un[0] + 1][ghost_pos_un[1]] not in murs :
            ghost_pos_un[0] += 1
            break
        if var == "d" and lab[ghost_pos_un[0]][ghost_pos_un[1] + 1] not in murs :
            ghost_pos_un[1] += 1
            break

def ghost_deux_move(var):
    while True:
        var = random.choice(list_choice)
        if var == "z" and lab[ghost_pos_deux[0] - 1][ghost_pos_deux[1]] not in murs :
            ghost_pos_deux[0] -= 1
            break
        if var == "q" and lab[ghost_pos_deux[0]][ghost_pos_deux[1] -1] not in murs :
            ghost_pos_deux[1] -= 1
            break
        if var == "s" and lab[ghost_pos_deux[0] + 1][ghost_pos_deux[1]] not in murs :
            ghost_pos_deux[0] += 1
            break
        if var == "d" and lab[ghost_pos_deux[0]][ghost_pos_deux[1] + 1] not in murs :
            ghost_pos_deux[1] += 1
            break

def moveit():
    ghost_move(var)
    ghost_un_move(var)
    ghost_deux_move(var)
    

printmap()

print("Voici la map, le but est de manger tout les petits rond. Bonne chance.")

while True:
    choice = input("Veuillez rentrer une lettre pour bouger. Z pour haut, S pour bas, Q pour gauche, D pour droite.").lower()
    if choice in list_choice :


        var = "a"

        # A MODIFIER, NE FONCTIONNE PAS COMME PREVU .
        if lab[ghost_pos_deux[0]][ghost_pos_deux[1]] == pac_gomme:
            lab[ghost_pos_deux[0]][ghost_pos_deux[1]] = pac_gomme
        else :
            lab[ghost_pos_deux[0]][ghost_pos_deux[1]] = vide
        
        if lab[ghost_pos_un[0]][ghost_pos_un[1]] == pac_gomme :
            lab[ghost_pos_un[0]][ghost_pos_un[1]] = pac_gomme
        else:
            lab[ghost_pos_un[0]][ghost_pos_un[1]] = vide

        if lab[ghost_pos[0]][ghost_pos[1]] == pac_gomme:
            lab[ghost_pos[0]][ghost_pos[1]] = pac_gomme
        else:
            lab[ghost_pos[0]][ghost_pos[1]] = vide
        #Jusqu'ici.

        lab[player_pos[0]][player_pos[1]] = vide

        score = int(score)

        if choice == "z" and lab[player_pos[0] - 1][player_pos[1]] not in murs :
            if lab[player_pos[0] - 1][player_pos[1]] == pac_gomme :
                score = score + 1
                player_pos[0] -= 1
                moveit()
            else : 
                player_pos[0] -= 1
                moveit()

        elif choice == "q" and lab[player_pos[0]][player_pos[1] - 1] not in murs : 
            if lab[player_pos[0]][player_pos[1] - 1] == pac_gomme:
                score = score + 1
                player_pos[1] -= 1
                moveit()
            else : 
                player_pos[1] -= 1
                moveit()

        elif choice == "s" and lab[player_pos[0] + 1][player_pos[1]] not in murs : 
            if lab[player_pos[0] + 1][player_pos[1]] == pac_gomme :
                score = score + 1
                player_pos[0] += 1
                moveit()            
            else : 
                player_pos[0] += 1
                moveit()        

        elif choice == "d" and lab[player_pos[0]][player_pos[1] + 1] not in murs : 
            if lab[player_pos[0]][player_pos[1] + 1] == pac_gomme :
                score = score + 1
                player_pos[1] += 1
                moveit()             
            else : 
                player_pos[1] += 1
                moveit()
        score = str(score)
        
        #Il faut rajouter une condition quand les joueurs/fantôme arrive sur les bords pour se tp de l'autre coté


        lab[ghost_pos_deux[0]][ghost_pos_deux[1]] = ghost_deux
        lab[ghost_pos_un[0]][ghost_pos_un[1]] = ghost_un
        lab[ghost_pos[0]][ghost_pos[1]] = ghost
        lab[player_pos[0]][player_pos[1]] = player
        lab[score_pos[0]][score_pos[1]] = score
        os.system("cls")

        printmap()
    if score == '60' :
        print("Bravo vous avez gagné!")
        break

    if lab[player_pos[0]][player_pos[1]] == lab[ghost_pos[0]][ghost_pos[1]] or lab[player_pos[0]][player_pos[1]] == lab[ghost_pos_un[0]][ghost_pos_un[1]] or lab[player_pos[0]][player_pos[1]] == lab[ghost_pos_deux[0]][ghost_pos_deux[1]] :
        lab[player_pos[0]][player_pos[1]] = dead
        printmap()
        print("Vous avez perdu vous vous êtes fait bouffé !")
        break
    
    else:
        print("Veuillez choisir un bon input m'enfin !! ")
    
#OUAIOUAIOUAI