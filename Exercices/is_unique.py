def is_unique(elements):
    unique_set = set()
    for element in elements:
        if element in unique_set:
            return False
        unique_set.add(element)
    return True

liste1 = [1, 2, 3, 4, 5]
resultat1 = is_unique(liste1)
print(f"La liste {liste1} a des éléments en doublon ? {resultat1}")

liste2 = [1, 2, 2, 3, 4, 5]
resultat2 = is_unique(liste2)
print(f"La liste {liste2} a des éléments en doublon ? {resultat2}")
