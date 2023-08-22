mots = []
while True:
    mot = input("Entrez un mot (ou appuyez sur Entrée pour terminer) : ")
    if mot == "":
        break
    mots.append(mot)

print("La suite de mots dans l'ordre inverse de saisie est :")
for mot in reversed(mots):
    print(mot)
