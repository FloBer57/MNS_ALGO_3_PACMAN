# print("10 11 12 13 14 15")
# print("20 21 22 23 24 25")
# print("30 31 32 33 34 35")
# print("40 41 42 43 44 45")
# print("50 51 52 53 54 55")

# FINIT 


def ma_list(x,y):
    list = [i for i in range(x, y)]
    return list

print(ma_list(10,16))
print(ma_list(20,26))
print(ma_list(30,36))
print(ma_list(40,46))
print(ma_list(50,56))

# Il faut utiliser le mot-clé return pour renvoyer la liste
# Sinon, la fonction ne renvoie rien. Cela permet ma variable ma_liste de récupérer les données de ma liste avec x,y