import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 800

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Ping-Pong")

# Paramètres de jeu
barre_largeur = 15
barre_hauteur = 100
balle_diametre = 20
vitesse_balle = 5
vitesse_joueur = 5

# Initialisation des positions
barre_joueur1_x = 0
barre_joueur1_y = hauteur // 2 - barre_hauteur // 2
barre_joueur2_x = largeur - barre_largeur
barre_joueur2_y = hauteur // 2 - barre_hauteur // 2

balle_x = largeur // 2 - balle_diametre // 2
balle_y = hauteur // 2 - balle_diametre // 2

balle_dx = random.choice([-1, 1]) * vitesse_balle
balle_dy = random.choice([-1, 1]) * vitesse_balle

joueur1_score = 0
joueur2_score = 0
font = pygame.font.Font(None, 36)

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvement des joueurs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and barre_joueur1_y > 0:
        barre_joueur1_y -= vitesse_joueur
    if keys[pygame.K_s] and barre_joueur1_y < hauteur - barre_hauteur:
        barre_joueur1_y += vitesse_joueur
    if keys[pygame.K_UP] and barre_joueur2_y > 0:
        barre_joueur2_y -= vitesse_joueur
    if keys[pygame.K_DOWN] and barre_joueur2_y < hauteur - barre_hauteur:
        barre_joueur2_y += vitesse_joueur

    # Mouvement de la balle
    balle_x += balle_dx
    balle_y += balle_dy

    # Rebond de la balle sur les murs
    if balle_y <= 0 or balle_y >= hauteur - balle_diametre:
        balle_dy = -balle_dy

    # Rebond de la balle sur les raquettes
    if (barre_joueur1_x + barre_largeur >= balle_x >= barre_joueur1_x and
            barre_joueur1_y + barre_hauteur >= balle_y >= barre_joueur1_y):
        balle_dx = -balle_dx
    if (barre_joueur2_x <= balle_x + balle_diametre <= barre_joueur2_x + barre_largeur and
            barre_joueur2_y + barre_hauteur >= balle_y >= barre_joueur2_y):
        balle_dx = -balle_dx

    # Gestion des scores et fin de partie
    if balle_x <= 0:
        joueur2_score += 1
        if joueur2_score >= 6:
            running = False
        balle_x = largeur // 2 - balle_diametre // 2
        balle_y = hauteur // 2 - balle_diametre // 2
        balle_dx = random.choice([-1, 1]) * vitesse_balle
        balle_dy = random.choice([-1, 1]) * vitesse_balle

    if balle_x >= largeur - balle_diametre:
        joueur1_score += 1
        if joueur1_score >= 6:
            running = False
        balle_x = largeur // 2 - balle_diametre // 2
        balle_y = hauteur // 2 - balle_diametre // 2
        balle_dx = random.choice([-1, 1]) * vitesse_balle
        balle_dy = random.choice([-1, 1]) * vitesse_balle

    # Effacement de l'écran
    fenetre.fill(noir)

    # Dessin des éléments du jeu
    pygame.draw.rect(fenetre, blanc, (largeur // 2 - 2, 0, 4, hauteur))
    pygame.draw.rect(fenetre, blanc, (barre_joueur1_x, barre_joueur1_y, barre_largeur, barre_hauteur))
    pygame.draw.rect(fenetre, blanc, (barre_joueur2_x, barre_joueur2_y, barre_largeur, barre_hauteur))
    pygame.draw.circle(fenetre, blanc, (balle_x, balle_y), balle_diametre // 2)

    # Affichage des scores
    score_texte = font.render(f"Joueur 1: {joueur1_score}   Joueur 2: {joueur2_score}", True, blanc)
    fenetre.blit(score_texte, (20, 20))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limite de vitesse
    pygame.time.Clock().tick(60)

# Fermeture de Pygame
pygame.quit()
