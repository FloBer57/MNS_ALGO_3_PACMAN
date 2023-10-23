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
    matiere_name = str(input("Veuillez rentrer le nom de la matière "))
    tab_matiere.append(matiere_name)

# demander le nombre d'élève à ajouter et stocker leur nom et prénom

tab_note = []
tab_name = []
tab_surname = []


print("Troisème étape \n \n")


while True :
    try :
        nombre_eleve = int(input("Veuillez rentrer le nombre d'élève :"))
        break
    except ValueError : 
        ("Veuillez suivre la consigne ")

for i in range (nombre_eleve) : 
    name = str(input("Veuilez rentrer un prénom : " ))
    tab_name.append(name)
    surname = str(input("Veuilez rentrer un nom : "))
    tab_surname.append(surname)

# pour chaque élève saisir la note par matière

print("4ème étape \n \n")


for i_mat in range (nombre_matiere):
    for i in range(nombre_eleve):
        note_eleve = float(input(f"Veuillez rentrer le note de l'élève {tab_name[i]} {tab_surname[i]} pour la matière de {tab_matiere[i_mat]}"))
        tab_note.append(note_eleve)
        

# afficher tous les élèves avec leur moyenne générales et leurs notes par matières



print("5ième étape \n \n")
print("Voici toutes les notes des élèves par matière. \n")

note_par_eleve = len(tab_note) / nombre_matiere
tab_moyenne = []
tab_moyenne_eleve = []

for i in range (nombre_matiere):
    for i in range(nombre_eleve):
        for i in range (i,note_par_eleve,nombre_eleve):
            moyenne = tab_note[i]
            tab_moyenne_eleve.append(moyenne)
            print(tab_note[i])
            print(i)

# afficher la moyenne de la classe par matière

print("6ième étape \n \n")

# donner le nom du meilleur élève


# donner le nom du pire élève