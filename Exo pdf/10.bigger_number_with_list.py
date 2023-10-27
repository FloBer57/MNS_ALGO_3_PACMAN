
#Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite
#quel était le plus grand parmi ces 20 nombres.


list = []

while True :
    try:
        max_number = int(input(f"Veuillez rentrer un nombre entier concernant le nombre maximum d'utilisateur veuillez faire une rentrée.. "))
        break
    except ValueError:
        print("Veuillez suivre la consigne.")


while len(list) < max_number :
    while True :
        try:
            number = float(input(f"Veuillez rentrer un nombre. "))
            list.append(number)
            print(list)
            break
        except ValueError:
            print("Veuillez suivre la consigne.")

print(f"Le plus grand nombre de toutes les entrées est {max(list)}")

# Je crois utiliser un "tableau" au vu de l'utilisation de la liste. 

