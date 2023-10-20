#Ci-joint un petit programme pour obtenir immédiatement l'appréciation d'un élève en fonction de sa note. 

print("Petit programme permettant d'obtenir une appréciation d'un élève en fonction de sa moyenne.")

#Je me crée une liste de notes possible à pouvoir rentrer dans mon code. Les autres valeurs ne seront pas acceptées. 

# Créer une liste à partir de l'objet range
notes_valides = list(range(21))

# Ajouter un élément à la fin de la liste
notes_valides.append(0)



coeff_valides = [ i for i in range (1,11)]

#Dans la liste de range 21, il y a tout les nombre possible entre 0 et 20 ( 0 exclu, d'ou le append qui est une fonction qui permet d'ajouter dans une liste des éléments. )

while True : 
    try : 
        note_fr = float(input("Veuillez rentrer la note de français/20 "))
        if note_fr in notes_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 0 et 20 pour chaqu'une des notes.")
    except ValueError : 
        print("Veuillez suivre la consigne")

while True : 
    try : 
        coeff_fr = int(input("Veuillez rentrer le coeff de français/10 "))
        if coeff_fr in coeff_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 1 et 10 pour chaqu'une des notes.")
    except ValueError : 
        print("Veuillez suivre la consigne")

while True : 
    try : 
        note_math = float(input("Veuillez rentrer la note de math/20 "))
        if note_math in notes_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 0 et 20 pour chaqu'une des notes.")
    except ValueError : 
        print("Veuillez suivre la consigne")

while True : 
    try : 
        coeff_math = int(input("Veuillez rentrer le coeff de math/10 "))
        if coeff_math in coeff_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 1 et 10 pour chaqu'une des notes.")
    except ValueError : 
        print("Veuillez suivre la consigne")

while True : 
    try : 
        note_geo = float(input("Veuillez rentrer la note de géographie/20 "))
        if note_geo in notes_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 0 et 20 pour chaqu'une des notes.")
    except ValueError : 
        print("Veuillez suivre la consigne")

while True : 
    try : 
        coeff_geo = int(input("Veuillez rentrer le coeff de géographie/10 "))
        if coeff_geo in coeff_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 1 et 10 pour chaqu'une des notes.")
    except ValueError : 
        print("Veuillez suivre la consigne")


while True : 
    try : 
        note_histoire = float(input("Veuillez rentrer la note d'histoire/20 "))
        if note_histoire in notes_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 0 et 20 pour chaqu'une des notes.")
    except ValueError : 
        print("Veuillez suivre la consigne")

while True : 
    try : 
        coeff_histoire = int(input("Veuillez rentrer le coeff d'histoire/10 "))
        if coeff_histoire in coeff_valides :
            break
        else : 
            print("Veuillez bien rentrer un nombre entre 1 et 10 pour chaqu'une des notes.")
    except ValueError : 
        print("Veuillez suivre la consigne")

coeff_total = coeff_fr + coeff_math + coeff_geo + coeff_histoire

moyenne_eleve = ((note_fr*coeff_fr) + (note_math*coeff_math) + (note_geo*coeff_geo) + (note_histoire*coeff_histoire)) / coeff_total

if 20 >= moyenne_eleve >= 16 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Très bien.>>")
elif 16 > moyenne_eleve >= 12 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Bien.>>")
elif 12 > moyenne_eleve >= 8 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Assez bien.>>")
elif 8 > moyenne_eleve >= 4 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Insufisant.>>")
elif 4 > moyenne_eleve >= 0 : 
    print(f"La mention de l'élève pour une moyenne de {moyenne_eleve} est <<Nul.>>")