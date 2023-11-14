while True :
    try :
        depart = int(input("Veuillez rentrer un entier de la borne de départ. "))
        break
    except ValueError :
        print("Veuillez suivre la consigne.")

while True :
    try :
        arrivee = int(input("Veuillez rentrer un entier concernant la borne d'arrivée "))
        if arrivee > depart :
            break
    except ValueError :
        print("Veuillez suivre la consigne.")

while True :
    try :
        pas = int(input("Veuillez rentrer un entier qui détermine le pas à adopter. "))
        break
    except ValueError :
        print("Veuillez suivre la consigne.")


list = [i for i in range(depart, arrivee +1, pas)]

print(f"Voici le compteur. : {list}")
