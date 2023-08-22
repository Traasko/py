nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")

if len(nom) > 5:
    nom = nom.upper()
    prenom = prenom.upper()

print("Nom:", nom)
print("Prénom:", prenom)
