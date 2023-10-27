#L’élève placé au fond de la classe, près du radiateur, est le meilleur de la classe. Pour tuer le temps,
#il décide de plier une feuille en deux puis en deux, puis… en deux, puis… Écrivez un algorithme
#qui calcule l’épaisseur du pliage final à partir du nombre de plis et de l’épaisseur initiale de lafeuille. 


print("L'élève Théo Gamory souhaite plier une feuille en deux pour tuer le temps.")

while True :
    try :
        mm = float(input("Veuillez rentrer l'épaisseur initiale en mm : "))
        break
    except ValueError :
        print("Veuillez suivre la consigne.")

base = mm
max_pliage = 8

for i in range(max_pliage) :
    mm=mm*2
    print(mm)

print(f"Le maximum de pliage étant de {max_pliage}, l'épaisseur maximum après {max_pliage} est de {mm}")
