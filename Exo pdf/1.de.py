#Réalisez un jeu de dés utilisant les aiguillages conditionnels. Au démarrage du programme, il calcule au hasard un nombre entre 1 à 6 (utilisez la fonction suivante : randint() de la librairie random). 
#Le programme affiche « Vous avez fait un cinq» et il affiche la face du dé, sur 3 lignes, par exemple :
#«0 0»
#« 0 »
#«0 0»
import random

a = random.randint(1,6)

print(f"Vous avez fait un {a} \n")

if a == 1 :
    print("   ")
    print(" 0 ")
    print("   ")

elif a == 2 :
    print("0  ")
    print("   ")
    print("  0")

elif a == 3 :
    print("0  ")
    print(" 0 ")
    print("  0")

elif a == 4 :
    print("0 0")
    print("   ")
    print("0 0")

elif a == 5 :
    print("0 0")
    print(" 0 ")
    print("0 0")

elif a == 6 :
    print("0 0")
    print("0 0")
    print("0 0")