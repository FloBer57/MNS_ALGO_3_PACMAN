while True :
    try :
        number = int(input("Veuillez rentrer un entier en base 10. "))
        break
    except ValueError :
        print("Veuillez suivre la consigne.")


accumulation = ""
div = None

# je précise div = none pour que je puisse utiliser la variable dans mon while. 

# Sachant qu'en divisant j'arriverai forcément au bout d'un moment à 0, division entière bien évidemment.
# Je cherche à savoir le quotient du chiffre. 
# Je cherche ç savoir le modulo pour l'écrire ( Il sera toujours équivalent à 0 ou 1)
# Ensuite je demande à ce qu'il m'écrire ligne par ligne en reprenant l'ancien.

while div != 0 : 
    div = number // 2
    modulo = number % 2
    number = div
    accumulation = str(modulo) + " " + accumulation
    print(accumulation)
