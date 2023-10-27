#Test PACMAN

import random

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
score = '0'

list_choice = ["z", "q", "s", "d"]

list_choice_qsd = ["q","s","d"]
list_choice_sd = ["s","d"]
list_choice_qd = ["q","d"]
list_choice_sq = ["s","q"]

list_choice_zsd = ["z","s","d"]
list_choice_zqd = ["z","q","d"]
list_choice_zd = ["z","d"]
list_choice_zq = ["z","q"]
list_choice_zs = ["z","s"]



murs = [mur_vertical,mur_horizontal,coin_haut_gauche,coin_haut_droite,coin_bas_gauche,coin_bas_droite,coin_vers_bas,coin_vers_droite,coin_vers_gauche,coin_vers_haut]
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
    [vide, coin_bas_gauche, mur_horizontal, mur_horizontal, mur_horizontal, pac_gomme, coin_haut_gauche, vide, mur_horizontal, vide, coin_haut_droite, pac_gomme, mur_horizontal, mur_horizontal, mur_horizontal, coin_bas_droite, vide, vide, vide, vide],
    [vide, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, mur_vertical, vide, vide, vide, mur_vertical, pac_gomme, pac_gomme, pac_gomme, pac_gomme, pac_gomme, vide, vide, vide, vide],
    [vide, coin_haut_gauche, mur_horizontal, mur_horizontal, mur_horizontal, pac_gomme, coin_bas_gauche, mur_horizontal, mur_horizontal, mur_horizontal, coin_bas_droite, pac_gomme, mur_horizontal, mur_horizontal, mur_horizontal, coin_haut_droite, vide, vide, vide, vide],
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
        i_str = "".join(ii)
        print(i_str)

def ghost_move(var):
    if var == "z" :
        if lab[ghost_pos[0] - 1][ghost_pos[1]] not in murs :
            ghost_pos[0] -= 1
        if lab[ghost_pos[0] - 1][ghost_pos[1]] in murs :
            second_var = random.choice(list_choice_qsd)   # SECONDE VAR


            if second_var == "q" :
                if lab[ghost_pos[0]][ghost_pos[1] -1] not in murs:
                    ghost_pos[1] -= 1
                elif lab[ghost_pos[0]][ghost_pos[1] -1] in murs :
                    third_var = random.choice(list_choice_sd)   #TROISIEME VAR


                    if third_var == "s" :
                        if lab[ghost_pos[0] + 1][ghost_pos[1]] not in murs :
                            ghost_pos[0] += 1
                        elif lab[ghost_pos[0] + 1][ghost_pos[1]] in murs :
                            #Comme s'il avait choisit D
                            if lab[ghost_pos[0]][ghost_pos[1] + 1] not in murs :
                                ghost_pos[1] += 1
                            else:
                                print("Je n'ai pas reussi à bouger")   
                            # Finit pour Z - Q - S - D

                    if third_var == "d":
                        if lab[ghost_pos[0]][ghost_pos[1] + 1] not in murs :
                            ghost_pos[1] += 1
                    elif lab[ghost_pos[0]][ghost_pos[1] + 1] in murs :   
                        if lab[ghost_pos[0] + 1][ghost_pos[1]] not in murs :
                            ghost_pos[0] += 1
                        else :
                            print("Je n'ai pas reussi à bouger")
                            #Finit pour Z - Q - D - S            

            elif second_var == "s":
                if lab[ghost_pos[0] + 1][ghost_pos[1]] not in murs :
                    ghost_pos[0] += 1
                elif lab[ghost_pos[0] + 1][ghost_pos[1]] in murs :
                    third_var = random.choice(list_choice_qd)    #TROISIEME VAR


                    if third_var == "q":
                        if lab[ghost_pos[0]][ghost_pos[1] -1] not in murs :
                            ghost_pos[1] -= 1
                        elif lab[ghost_pos[0]][ghost_pos[1] -1] in murs :
                            if lab[ghost_pos[0]][ghost_pos[1] + 1] not in murs :
                                ghost_pos[1] += 1
                            else:
                                print("Je n'ai pas reussi à bouger") 
                            # Finit pour Z - S - Q - D 
                    elif third_var == "d":
                        if lab[ghost_pos[0]][ghost_pos[1] + 1] not in murs :
                            ghost_pos[1] += 1
                        elif lab[ghost_pos[0]][ghost_pos[1] + 1] in murs :
                            if lab[ghost_pos[0]][ghost_pos[1] -1] not in murs :
                                ghost_pos[1] -= 1
                            else:
                                print("Je n'ai pas reussi à bouger")
                            # Finit pour Z - S - D - Q

            elif second_var == "d" :
                if lab[ghost_pos[0]][ghost_pos[1] + 1] not in murs :
                    ghost_pos[1] += 1
                elif lab[ghost_pos[0]][ghost_pos[1] + 1] in murs :
                    third_var = random.choice(list_choice_sq)    #TROISIEME VAR


                    if third_var == "s":
                        if lab[ghost_pos[0] + 1][ghost_pos[1]] not in murs :
                            ghost_pos[0] += 1
                        elif lab[ghost_pos[0] + 1][ghost_pos[1]] in murs :
                            if lab[ghost_pos[0]][ghost_pos[1] -1] not in murs :
                                ghost_pos[1] -= 1
                            else : 
                                print("Je n'ai pas reussi à bouger")
                            #Finit pour Z - D - S - Q

                    if third_var == "q" :
                        if lab[ghost_pos[0]][ghost_pos[1] -1] not in murs :
                            ghost_pos[1] -= 1
                        elif lab[ghost_pos[0]][ghost_pos[1] -1] in murs :
                            if lab[ghost_pos[0] + 1][ghost_pos[1]] not in murs :
                                ghost_pos[0] += 1
                            else:
                                print("Je n'ai pas reussi à bouger")
                            #Finit pour Z - D - Q - S

    if var == "q" and lab[ghost_pos[0]][ghost_pos[1] -1] not in murs :
        ghost_pos[1] -= 1
    if var == "s" and lab[ghost_pos[0] + 1][ghost_pos[1]] not in murs :
        ghost_pos[0] += 1
    if var == "d" and lab[ghost_pos[0]][ghost_pos[1] + 1] not in murs :
        ghost_pos[1] += 1
        
printmap()

print("Voici la map, le but est de manger tout les petits rond. Bonne chance.")

while True:
    choice = input("Veuillez rentrer une lettre pour bouger. Z pour haut, S pour bas, Q pour gauche, D pour droite.").lower()
    if choice in list_choice :

        rand = random.choice(list_choice)
        rand_un = random.choice(list_choice)
        rand_deux = random.choice(list_choice)

        lab[ghost_pos[0]][ghost_pos[1]] = vide
        lab[player_pos[0]][player_pos[1]] = vide

        score = int(score)

        if choice == "z" and lab[player_pos[0] - 1][player_pos[1]] not in murs :
            if lab[player_pos[0] - 1][player_pos[1]] == pac_gomme :
                score = score + 1
                player_pos[0] -= 1
                ghost_move(rand)
                ghost_un_move(rand_un)
                ghost_deux_move(rand_deux)
            else : 
                player_pos[0] -= 1
                ghost_move(rand)
                ghost_un_move(rand_un)
                ghost_deux_move(rand_deux)

        elif choice == "q" and lab[player_pos[0]][player_pos[1] - 1] not in murs : 
            if lab[player_pos[0]][player_pos[1] - 1] == pac_gomme:
                score = score + 1
                player_pos[1] -= 1
                ghost_move(rand)
                ghost_un_move(rand_un)
                ghost_deux_move(rand_deux)
            else : 
                player_pos[1] -= 1
                ghost_move(rand)
                ghost_un_move(rand_un)
                ghost_deux_move(rand_deux)

        elif choice == "s" and lab[player_pos[0] + 1][player_pos[1]] not in murs : 
            if lab[player_pos[0] + 1][player_pos[1]] == pac_gomme :
                score = score + 1
                player_pos[0] += 1
                ghost_move(rand)
                ghost_un_move(rand_un)
                ghost_deux_move(rand_deux)                
            else : 
                player_pos[0] += 1
                ghost_move(rand)
                ghost_un_move(rand_un)
                ghost_deux_move(rand_deux)                

        elif choice == "d" and lab[player_pos[0]][player_pos[1] + 1] not in murs : 
            if lab[player_pos[0]][player_pos[1] + 1] == pac_gomme :
                score = score + 1
                player_pos[1] += 1
                ghost_move(rand)
                ghost_un_move(rand_un)
                ghost_deux_move(rand_deux)                
            else : 
                player_pos[1] += 1
                ghost_move(rand)
                ghost_un_move(rand_un)
                ghost_deux_move(rand_deux)
        score = str(score)
        
        lab[ghost_pos[0]][ghost_pos[1]] = ghost
        lab[player_pos[0]][player_pos[1]] = player
        lab[score_pos[0]][score_pos[1]] = score

        printmap()
    elif player == "30" :
        print("Bravo vous avez gagné!")
        break


    else:
        print("Veuillez choisir un bon input m'enfin !! ")
    
#OUAIOUAIOUAI