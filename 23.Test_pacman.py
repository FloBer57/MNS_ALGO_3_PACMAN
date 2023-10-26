mur_droit = "║"
mur_bas = "═"
coin_haut_gauche = "╔"
coin_haut_droite = "╗"
coin_bas_gauche = "╚"
coin_bas_droite = "╝"
coin_vers_bas = "╦"
V = " "
P = "█"


lvl = [
    [coin_haut_gauche] + [mur_bas] * 22 + [coin_haut_droite],  # Ligne 1
    [mur_droit, V, V, V, V, mur_droit, mur_droit, V, V, V, V, V, mur_droit, mur_droit, V, V, V, V, V, V, mur_droit],  # Ligne 2
    [mur_droit, V, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit],  # Ligne 3
    [mur_droit, V, mur_droit, V, V, mur_droit, V, V, V, V, mur_droit, V, mur_droit, V, mur_droit, V, V, V, V, V],  # Ligne 4
    [mur_droit, V, V, V, V, V, V, V, V, mur_droit, V, V, V, mur_droit, V, V, V, V, V, V],  # Ligne 5
    [mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit],  # Ligne 6
    [mur_droit, mur_droit, V, V, V, mur_droit, V, V, V, V, V, V, V, V, V, V, V, V, V, V],  # Ligne 7
    [mur_droit, V, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit],  # Ligne 8
    [mur_droit, V, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit],  # Ligne 9
    [mur_droit, V, V, V, V, mur_droit, V, V, V, V, V, V, V, V, V, V, V, V, V, mur_droit],  # Ligne 10
    [mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit],  # Ligne 11
    [mur_droit, mur_droit, V, V, V, mur_droit, V, V, V, V, V, V, V, V, V, V, V, V, V, mur_droit],  # Ligne 12
    [mur_droit, V, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit],  # Ligne 13
    [mur_droit, V, V, V, V, V, V, V, V, mur_droit, V, V, V, mur_droit, V, V, V, V, V, V],  # Ligne 14
    [mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, V, mur_droit, mur_droit, V, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit, mur_droit],  # Ligne 15
    [coin_bas_gauche] + [mur_bas] * 22 + [coin_bas_droite],  # Ligne 16
]

def printmap():
    for i in lvl:
        print(i)

printmap()