def draw_pyramid(etages):
    base_largeur = etages * 2 + 1
    hauteur = etages * 3
    for etage in range(1, etages + 1):
        for ligne in range(hauteur):
            espaces = hauteur - ligne
            caracteres = base_largeur - espaces * 2
            print(" " * espaces, end="")
            print("/" + "-" * (caracteres - 2) + "\\", end="")
            print(" " * espaces)
        base_largeur += 2
        hauteur -= 1

etages = int(input("Entrez le nombre d'étages de la pyramide : "))

draw_pyramid(etages)
    
