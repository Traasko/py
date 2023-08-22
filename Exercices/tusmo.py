import random
import termcolor

mots = ["PYTHON", "BANANE", "ORDINATEUR", "PROGRAMME", "ALGORITHME", "DEVELOPPEUR"]

def choisir_mot():
    return random.choice(mots)

def afficher_mot_partiel(mot_devine, mot_a_deviner):
    mot_partiel = ""
    for lettre_devinee, lettre_a_deviner in zip(mot_devine, mot_a_deviner):
        if lettre_devinee == lettre_a_deviner:
            mot_partiel += termcolor.colored(lettre_devinee, 'red')
        elif lettre_devinee in mot_a_deviner:
            mot_partiel += termcolor.colored(lettre_devinee, 'yellow')
        else:
            mot_partiel += lettre_devinee
    return mot_partiel

def jouer_motus():
    mot_a_deviner = choisir_mot()
    mot_partiel = mot_a_deviner[0] + "-" * (len(mot_a_deviner) - 1)
    essais = 5

    print("Bienvenue dans le jeu du Motus !")
    print(f"Vous devez deviner un mot de {len(mot_a_deviner)} lettres.")
    print(f"Vous avez {essais} essais par manche.\n")

    for manche in range(1, 6):
        print(f"Manche {manche} - Mot partiel : {mot_partiel}")

        mot_devine = input("Entrez votre proposition : ").upper()

        if mot_devine == mot_a_deviner:
            print("Bravo, vous avez trouvé le mot !")
            break
        elif len(mot_devine) != len(mot_a_deviner):
            print("Le mot doit contenir le même nombre de lettres que le mot à deviner.")
        else:
            mot_partiel = afficher_mot_partiel(mot_devine, mot_a_deviner)
            essais -= 1
            print(f"Essais restants : {essais}\n")

        if essais == 0:
            print(f"Vous avez utilisé tous vos essais. Le mot à deviner était : {mot_a_deviner}")

if __name__ == "__main__":
    jouer_motus()
