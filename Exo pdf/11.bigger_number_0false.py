import sys

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
            elif number == 0 :
                sys.exit("Programme finit, vous avez rentrer le chiffre maudit.")
            print(dif)
            break
        except ValueError:
            print("Veuillez suivre la consigne.")

print(f"Le plus grand nombre rentrer parmis les {max_number} entrée de l'utilisateur est {dif}.")

#Je rajoute une simple condition qui dit que si le nombre rentré est == à 0
#Le programme s'arrête grace à import sys - sys.exit.