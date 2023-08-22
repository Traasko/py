def rot(lst, N):
    if not lst or N <= 0:
        return lst
    N %= len(lst)
    return lst[N:] + lst[:N]

liste = [1, 2, 3, 4, 5]
n = 2
resultat = rot(liste, n)
print(f"La liste après une rotation de {n} éléments est : {resultat}")
