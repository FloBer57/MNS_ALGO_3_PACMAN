import random
import sys


list = [i for i in range(1, 11)]
print(f"{list} Voici la liste des nombres possible. \n")
while True :   
    try :
        number = int(input("Veuillez rentrer un nombre entre 1 et 10 ENTIER. Ne trichez pas. \n"))
        if number in list :
            break
    except ValueError : 
            print("Je vous ai dit de pas tricher!! Suivez la consigne! \n")

rand = random.randint(1,10)

print(f"Le nombre magique est {rand} \n")


if number == rand :
    print(f"Sachant que le numéro magique est {rand} et le vôtre est {number}, ce sont les mêmes, vous avez gagné! Bravo! \n")
    sys.exit("Programme finit")
elif number > rand : 
    print(f"Sachant que le numéro magique est {rand} et le vôtre est {number}, votre nombre est trop grand. Perdu! \n")

elif number < rand : 
    print(f"Sachant que le numéro magique est {rand} et le vôtre est {number}, votre nombre est trop petit. Perdu! \n")
