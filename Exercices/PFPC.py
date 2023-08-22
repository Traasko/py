def jouer_manche(joueur1, joueur2):
    if joueur1 == joueur2:
        return "match nul"

    if (joueur1 == "PI" and joueur2 == "CI") or \
       (joueur1 == "FE" and joueur2 == "PI") or \
       (joueur1 == "PA" and joueur2 == "FE") or \
       (joueur1 == "CI" and joueur2 == "PA"):
        return "joueur 1"

    return "joueur 2"

def main():
    score_joueur1 = 0
    score_joueur2 = 0

    for manche in range(1, 4):
        print(f"Manche {manche}")
        joueur1 = input("Joueur 1, entrez votre choix (PI, FE, PA, CI) : ").upper()
        joueur2 = input("Joueur 2, entrez votre choix (PI, FE, PA, CI) : ").upper()

        gagnant_manche = jouer_manche(joueur1, joueur2)
        if gagnant_manche == "joueur 1":
            score_joueur1 += 1
        elif gagnant_manche == "joueur 2":
            score_joueur2 += 1

        print(f"Le gagnant de la manche {manche} est : {gagnant_manche}\n")

    if score_joueur1 > score_joueur2:
        gagnant_partie = "joueur 1"
    elif score_joueur2 > score_joueur1:
        gagnant_partie = "joueur 2"
    else:
        gagnant_partie = "match nul"

    print(f"Le gagnant de la partie est : {gagnant_partie}")

if __name__ == "__main__":
    main()
