list_year = [i for i in range(0, 10000)]
list_month = [i for i in range(1, 13)]
list_day = [i for i in range(1, 32)]

while True :
    try : 
        A = int(input("Veuillez saisir une année au format (AAAA) \n"))
        if A in list_year :
            break
    except ValueError : 
        print("Veuillez suivre la consigne.")

while True :
    try : 
        M = int(input("Veuillez saisir un mois au format (MM) \n"))
        if M in list_month :
            break
    except ValueError : 
        print("Veuillez suivre la consigne.")

while True :
    try : 
        J = int(input("Veuillez saisir un jour au format (JJ) \n"))
        if M in list_day :
            break
    except ValueError : 
        print("Veuillez suivre la consigne.")      

annee = A
mois = M
jour = J

print(f"Vous avez rentrer le {J} {M} {A}. Souhaitez vous savoir quel jour c'était? \n")

while True :
    try : 
        reponse = str(input('Veuillez rentrer oui ou non en majuscule. \n'))
        if reponse == "oui" :
            break
    except ValueError : 
        print("Veuillez suivre la consigne.")

if M == 1 or M == 2 : 
    A = A-1
    M = M+12

N = J + int(((13*M+3)/5)) + int(5*A/4) - int(A/100)+int(A/400)
N = N % 7

if N == 0 :
    print(f"Pour la date du {jour} {mois} {annee}, nous étions un {N}, donc un lundi.")
elif N == 1 :
    print(f"Pour la date du {jour} {mois} {annee}, nous étions un {N}, donc un mardi.")
elif N == 2 :
    print(f"Pour la date du {jour} {mois} {annee}, nous étions un {N}, donc un mercredi.")
elif N == 3 :
    print(f"Pour la date du {jour} {mois} {annee}, nous étions un {N}, donc un jeudi.")
elif N == 4 :
    print(f"Pour la date du {jour} {mois} {annee}, nous étions un {N}, donc un vendredi.")
elif N == 5 :
    print(f"Pour la date du {jour} {mois} {annee}, nous étions un {N}, donc un samedi.")
elif N == 6 :
    print(f"Pour la date du {jour} {mois} {annee}, nous étions un {N}, donc un dimanche.")
