# Je réessai sans liste. 

while True :
    try:
        max_number = int(input(f"Veuillez rentrer un nombre entier concernant le nombre maximum d'utilisateur veuillez faire une rentrée.. "))
        break
    except ValueError:
        print("Veuillez suivre la consigne.")


dif = 0


for i in range(0,max_number):
    while True :
        try:
            number = float(input(f"Veuillez rentrer un nombre. "))
            if number > dif :
                dif = number 
            print(dif)
            break
        except ValueError:
            print("Veuillez suivre la consigne.")

print(f"Le plus grand nombre rentrer parmis les {max_number} entrée de l'utilisateur est {dif}.")


#Puisque l'on cherche la plus grande rentrée, je demande à ce que chaque 
#Nouvelle valeur soit comparée à l'ancienne. 
#Du coup, si la nouvelle valeur est supérieure, elle écrase l'ancienne. Si elle est inférieur
#Elle n'est pas pris en compte. Donc ca nous affichera forcément la plus grande valeur.


