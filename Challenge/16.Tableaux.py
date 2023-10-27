#Pour les tableaux : 

# tab = [1,4,2]

#Pour l'ajout d'une valeur : tab.append(4)


#Mofidier une valeur : tab[1] = 1 --> [1,1,2]


#Supprimer une valeur ---> tab.remove(3) 

# del(tab[2]) Pour supprimer par INDEX

# print(tab)

tab_name = []
tab_surname = []

# Permet de demander x fois de rerentrer une valeur

for i in range(5) :
    name = input("Veuillez rentrer un prénom en chaine de caractère :")
    tab_name.append(name)
    surname = input("Veuillez rentrer un nom de famille en chaine de caractère : ")
    tab_surname.append(surname)

for i in range(5):
    print(f"Voici le prénom :  {tab_name[i]}")
    print(f"Voici le nom de famille : {tab_surname[i]}")
