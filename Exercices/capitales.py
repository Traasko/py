import random

pays_capitales = {
    "France": "Paris",
    "Allemagne": "Berlin",
    "Italie": "Rome",
    "Espagne": "Madrid",
    "Royaume-Uni": "Londres",
    "États-Unis": "Washington",
    "Canada": "Ottawa",
    "Japon": "Tokyo",
    "Australie": "Canberra",
    "Brésil": "Brasilia"
}

def jouer_jeu():
    points = 0
    while True:
        pays = random.choice(list(pays_capitales.keys()))
        capitale_correcte = pays_capitales[pays]
        
        print(f"Devinez la capitale de {pays}: ")
        reponse = input()
        
        if reponse.lower() == capitale_correcte.lower():
            points += 1
            print(f"Correct ! Vous avez {points} point(s).")
        else:
            print(f"Faux ! Votre score final est de {points} point(s).")
            break

if __name__ == "__main__":
    jouer_jeu()
