import statistics as stats

# demander le nombre de matières à saisir

print("Première étape \n \n")
while True :
    try :
        nombre_matiere = int(input("Veuillez rentrer le nombre de matière. : "))
        break
    except ValueError :
        print("Veuillez suivre la consigne. ")

tab_matiere = []

print("Deuxième étape \n \n")
# stocker le nom des matières
for i in range (nombre_matiere):
    matiere_name = str(input(f"Veuillez rentrer le nom de la matière numéro {i+1} : "))
    tab_matiere.append(matiere_name)

# demander le nombre d'élève à ajouter et stocker leur nom et prénom

tab_note = []
tab_name = []
tab_surname = []


print("Troisème étape \n \n")


while True :
    try :
        nombre_eleve = int(input("Veuillez rentrer le nombre d'élève : "))
        break
    except ValueError : 
        ("Veuillez suivre la consigne ")

for i in range (nombre_eleve) : 
    while True : 
        try:
            name = str(input(f"Veuilez rentrer un prénom pour l'élève numéro {i+1}: " ))
            break
        except ValueError:
            ("Veuillez suivre la consigne.")
    tab_name.append(name)
    while True : 
        try:
            surname = str(input(f"Veuilez rentrer un nom pour l'élève s'appelant {tab_name[i]}: "))
            break
        except ValueError:
            ("Veuillez suivre la consigne.")
    tab_surname.append(surname)

# pour chaque élève saisir la note par matière

print("4ème étape \n \n")

    
for i_mat in range (nombre_matiere):
    for i in range(nombre_eleve):
        while True:
            try:
                note_eleve = float(input(f"Veuillez rentrer le note de l'élève {tab_name[i]} {tab_surname[i]} pour la matière de {tab_matiere[i_mat]} : "))
                if 0 <= note_eleve <= 20:
                    break
                else:
                    print("Veuillez rentrer une note sur 20 maximum.")
            except ValueError:
                ("Veuillez suivre la consigne")
        tab_note.append(note_eleve)
        
# afficher tous les élèves avec leur moyenne générales et leurs notes par matières


print("5ième étape \n \n")
print("Voici toutes les notes des élèves par matière. \n")

note_par_eleve = len(tab_note)
tab_moyenne = []
tab_moyenne_eleve = []
tab_moyenne_eleve_no_mean = []


for i in range(nombre_eleve):
    for i in range (i,note_par_eleve,nombre_eleve):
        moyenne = tab_note[i]
        tab_moyenne_eleve.append(moyenne)
    tab_moyenne_eleve_no_mean.append(tab_moyenne_eleve)
    tab_moyenne.append(stats.mean(tab_moyenne_eleve))
    tab_moyenne_eleve = []


for i in range(nombre_eleve):
    print(f"La moyenne générale de {tab_name[i]} {tab_surname[i]} est de {tab_moyenne[i]} avec les notes de {tab_moyenne_eleve_no_mean[i]} \n \n ")


# afficher la moyenne de la classe par matière

print(f"La moyenne globale est de {stats.mean(tab_moyenne):.2f}  \n \n ")

 
eleve = tab_name[i]
nom_eleve = tab_surname[i]
moy_eleve = tab_moyenne[i]

# donner le nom du meilleur élève

for i in range(nombre_eleve - 1):
    if tab_moyenne[i+1] > tab_moyenne[i]:
        eleve = tab_name[i+1]
        nom_eleve = tab_surname[i+1]
        moy_eleve = tab_moyenne[i+1]
       
print(f"Le meilleur eleve est {eleve} {nom_eleve} avec une moyenne de {moy_eleve} \n ")

#Reset des valeurs 


eleve = tab_name[i]
nom_eleve = tab_surname[i]
moy_eleve = tab_moyenne[i]


# donner le nom du pire élève


for i in range(nombre_eleve - 1):
    if tab_moyenne[i] < tab_moyenne[i+1] and tab_moyenne[i] < moy_eleve:
        eleve = tab_name[i]
        nom_eleve = tab_surname[i]
        moy_eleve = tab_moyenne[i]


print(f"Le plus mauvais est {eleve} {nom_eleve} avec une moyenne de {moy_eleve}")    