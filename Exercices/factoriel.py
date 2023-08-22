def calculer_factoriel(n):
    if n == 0:
        return 1
    else:
        return n * calculer_factoriel(n - 1)

nombre = int(input("Entrez un nombre : "))

factoriel = calculer_factoriel(nombre)

print(f"Le factoriel de {nombre} est : {factoriel}")
