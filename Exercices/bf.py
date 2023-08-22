from itertools import permutations

suite = input("Entrez une suite de nombres (séparés par des virgules) : ")
nombres = suite.split(",")

combinaisons = permutations(nombres)

print("Les combinaisons possibles sont :")
for combinaison in combinaisons:
    print("".join(combinaison), end=" ")

total_combinaisons = len(list(permutations(nombres)))
print("\nLe nombre total de combinaisons possibles est :", total_combinaisons)
