liste_choix = ["z", "q", "s", "d"]
wall = "X"
vide = " "
player = "O"
list_found = [wall,vide]


#X|X|X| |X             #0.0|0.1|0.2|0.3|0.4
#X|X| | |X             #1.0|1.1|1.2|1.3|1.4
#X| | |X|X             #2.0|2.1|2.2|2.3|2.4
#X| |X| |X             #3.0|3.1|3.2|3.3|3.4
#X| |X| |X             #4.0|4.1|4.2|4.3|4.4

# aide mémoire
import random

# je fais en sorte de générer aléatoirement avec mes valeurs Wall et Vide de manière aléatoire dans un 
# tableau de 5x5.
# Problème à gérer : Il y aura forcément des générations ou l'on ne pourra pas passer car trop de mur. Comment faire?
def print_map(lab):
    for row in lab:
        print(" ".join(row))

lab = [[random.choice(list_found) for _ in range(5)] for _ in range(5)]

# La position de commencement du joueur
player_pos = [0, 0]

# Traduction : le "PLAYER" prend comme position [index0,index1] donc la player = [pos0,pos1]
lab[player_pos[0]][player_pos[1]] = player

# Je print mon tableau ( Pour chaque valeur dans le tableau, les afficher.)
print_map(lab)

# C'est ici que je fais les commandes de mon joueur.
while True:
    choix = input("Veuillez rentrer un déplacement. (Z pour aller en haut, S bas, D droite, Q gauche.)").lower()
    if choix in liste_choix:

        # J'efface la précédente position de mon joueur.
        lab[player_pos[0]][player_pos[1]] = vide

        if choix == "z" and player_pos[0] > 0 and lab[player_pos[0] - 1][player_pos[1]] != wall:
            player_pos[0] -= 1
        elif choix == "s" and player_pos[0] < 4 and lab[player_pos[0] + 1][player_pos[1]] != wall:
            player_pos[0] += 1
        elif choix == "q" and player_pos[1] > 0 and lab[player_pos[0]][player_pos[1] - 1] != wall:
            player_pos[1] -= 1
        elif choix == "d" and player_pos[1] < 4 and lab[player_pos[0]][player_pos[1] + 1] != wall:
            player_pos[1] += 1

        # Maintenant il faut que je donne la nouvelle position à mon joueur.
        lab[player_pos[0]][player_pos[1]] = player

        # Je dois print le nouveau tableau
        print_map(lab)

        if player_pos == [4, 4]:
            print("Félicitations ! Vous avez réussi à sortir du labyrinthe.")
            break
    else:
        print("Veuillez suivre la consigne !")