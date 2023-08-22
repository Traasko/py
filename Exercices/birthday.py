from datetime import datetime

def trier_contacts_par_anniversaire(contacts):
    return sorted(contacts, key=lambda contact: contact['anniversaire'], reverse=True)

def main():
    contacts = []

    while True:
        nom = input("Entrez le nom du contact : ")
        prenom = input("Entrez le prénom du contact : ")
        date_str = input("Entrez la date d'anniversaire au format JJ/MM/AAAA : ")

        try:
            anniversaire = datetime.strptime(date_str, '%d/%m/%Y')
            contacts.append({'nom': nom, 'prenom': prenom, 'anniversaire': anniversaire})
        except ValueError:
            print("Format de date invalide. Veuillez utiliser le format JJ/MM/AAAA.")

        continuer = input("Voulez-vous ajouter un autre contact ? (Y/n) ").lower()
        if continuer != 'y':
            break

    contacts = trier_contacts_par_anniversaire(contacts)

    print("\nContacts triés par date d'anniversaire décroissante :")
    for contact in contacts:
        print(f"{contact['prenom']} {contact['nom']} - Anniversaire : {contact['anniversaire'].strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    main()
