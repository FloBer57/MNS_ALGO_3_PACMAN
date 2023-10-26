#Test PACMAN

mur_vertical = "║"
mur_horizontal = "═"
coin_haut_gauche = "╔"
coin_haut_droite = "╗"
coin_bas_gauche = "╚"
coin_bas_droite = "╝"
coin_vers_bas = "╦"
vide = " "
pacman = "█"


#Voici mon tableau, je viens de voir qu'on peux utiliser des *
lab = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,]
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,]
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,]
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,]
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,]
    [0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,]
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 3, 0,]
    [0, 2.5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2.5, 0, 0, 0, 0,]
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,]
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0,]
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,]
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,]
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,]
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,]
]

#X|X|X| |X             #0.0|0.1|0.2|0.3|0.4
#X|X| | |X             #1.0|1.1|1.2|1.3|1.4
#X| | |X|X             #2.0|2.1|2.2|2.3|2.4
#X| |X| |X             #3.0|3.1|3.2|3.3|3.4
#X| |X| |X             #4.0|4.1|4.2|4.3|4.4



player_pos = [1, 1]
lab[player_pos[0]][player_pos[1]] = player


def printmap():
    for ii in lab:
        i_str = "".join(ii)
        print(i_str)

printmap()

print("Voici la map, le but est de manger tout les petits rond. Bonne chance.")


list_choice = ["z","q","s","d"]

while True:
    choice = input("Veuillez rentrer une lettre pour bouger. Z pour haut, S pour bas, Q pour gauche, D pour droite.").lower()
    if choice in list_choice :

        player = int(player)

        lab[player_pos[0]][player_pos[1]] = vide

        if choice == "z" and lab[player_pos[0] - 1][player_pos[1]] != wall :
            if lab[player_pos[0] - 1][player_pos[1]] == jeton :
                player = player +1
                player_pos[0] -= 1
            else : 
                player_pos[0] -= 1

        elif choice == "q" and lab[player_pos[0]][player_pos[1] - 1] != wall : 
            if lab[player_pos[0]][player_pos[1] - 1] == jeton:
                player = player + 1
                player_pos[1] -= 1
            else : 
                player_pos[1] -= 1

        elif choice == "s" and lab[player_pos[0] + 1][player_pos[1]] != wall : 
            if lab[player_pos[0] + 1][player_pos[1]] == jeton :
                player = player + 1
                player_pos[0] += 1
            else : 
                player_pos[0] += 1

        elif choice == "d" and lab[player_pos[0]][player_pos[1] + 1] != wall : 
            if lab[player_pos[0]][player_pos[1] + 1] == jeton :
                player = player +1
                player_pos[1] += 1
            else : 
                player_pos[1] += 1

        player = str(player)

        lab[player_pos[0]][player_pos[1]] = player

        printmap()
    elif player == "30" :
        print("Bravo vous avez gagné!")
        break


    else:
        print("Veuillez choisir un bon input m'enfin !! ")
    
