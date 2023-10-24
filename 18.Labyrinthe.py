liste_choix = ["z", "q", "s", "d"]
wall = "X"
vide = " "
player = "O"



#X|X|X| |X             #0.0|0.1|0.2|0.3|0.4
#X|X| | |X             #1.0|1.1|1.2|1.3|1.4
#X| | |X|X             #2.0|2.1|2.2|2.3|2.4
#X| |X| |X             #3.0|3.1|3.2|3.3|3.4
#X| |X| |X             #4.0|4.1|4.2|4.3|4.4

# Je définis le tableau comme vu dessus.


lab = [
    ["X", "X", "X", " ", "X"],
    ["X", "X", " ", " ", "X"],
    ["X", " ", " ", "X", "X"],
    ["X", " ", "X", " ", "X"],
    ["X", " ", "X", " ", "X"]
]

# Voici la position du base du joueur.


player_pos = [4, 1]
lab[player_pos[0]][player_pos[1]] = player

# Je crée une fonction pour afficher la carte.


def print_map():
    for i in lab:
        print(" ".join(i))



# J'arrive à afficher la carte initiale. 


print_map()

while True:
    choix = input("Veuillez bouger. z pour haut, s pour bas, q pour gauche, d pour droite : ").lower()
    if choix in liste_choix:

        #J'efface la position du jouer. 
        lab[player_pos[0]][player_pos[1]] = vide
        # Je fais la position du joueur en fonction des choix qu'il fait.
        # si Z , et que la case du dessus y'as pas de mur, alors la pos du player prend -1 en Y ( Pour monter )
        if choix == "z" and lab[player_pos[0] - 1][player_pos[1]] != wall:
            player_pos[0] -= 1
        # si S , et que la case du dessus y'as pas de mur, alors la pos du player prend +1 en Y ( Pour monter )
        elif choix == "s" and lab[player_pos[0] + 1][player_pos[1]] != wall:
            player_pos[0] += 1
        # si Q , et que la case du dessus y'as pas de mur, alors la pos du player prend -1 en X ( Pour monter )
        elif choix == "q" and lab[player_pos[0]][player_pos[1] - 1] != wall:
            player_pos[1] -= 1
        # si D , et que la case du dessus y'as pas de mur, alors la pos du player prend +1 en Y ( Pour monter )
        elif choix == "d" and lab[player_pos[0]][player_pos[1] + 1] != wall:
            player_pos[1] += 1

        # Je donne la nouvelle position du jouer sur le plateau. 
        lab[player_pos[0]][player_pos[1]] = player

        # Affichez la carte mise à jour.
        print_map()

        # Vérifiez si le joueur est sorti du labyrinthe.
        if player_pos == [0, 3]:
            print("Félicitations ! Vous avez réussi à sortir du labyrinthe.")
            break
    else:
        print("Veuillez entrer une commande valide (z, q, s, d).")