list_promo = ["RAN1", "RAN2", "RAN3", "RAN4"]
stagiaires = []

nb_stagiaires = int(input("Veuillez rentrer le nombre de stagiaires à MNS "))

for i in range(nb_stagiaires):
    eleve = []
    surname = input(f"Veuillez rentrer le nom de famille de l'élève numéro {i + 1} : ")
    eleve.append(surname)
    name = input(f"Veuillez rentrer le prénom de l'élève numéro {i + 1} nommé {surname} : ")
    eleve.append(name)
    
    while True:
        try:
            promotion = input(f"Veuillez rentrer la promotion de l'élève numéro {i + 1} nommé {surname} {name} : ").upper()
            if promotion in list_promo:
                break
        except ValueError:
            print("Suis la consigne boubou")

    eleve.append(promotion)
    stagiaires.append(eleve)

for i in range (nb_stagiaires):
    print(f"-----{stagiaires[i]}-----")

