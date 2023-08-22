def get_last_n_index(L, N):
    if N < 1 or N > len(L):
        raise ValueError("L'index N doit être compris entre 1 et la longueur de la liste.")
    return L[-N]

liste = [10, 20, 30, 40, 50]
n = 3
resultat = get_last_n_index(liste, n)
print(f"L'élément {n}-ième en partant de la fin de la liste est : {resultat}")
