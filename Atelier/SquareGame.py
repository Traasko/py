import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 800

# Couleurs
rouge = (255, 0, 0)
blanc = (255, 255, 255)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Square")

# Dimensions du rectangle
rect_largeur = 50
rect_hauteur = 50

# Position initiale du rectangle
rect_x = (largeur - rect_largeur) // 2
rect_y = (hauteur - rect_hauteur) // 2

# Vitesse de déplacement
vitesse = 5

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des touches
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] and rect_y > 0:
        rect_y -= vitesse
    if keys[pygame.K_s] and rect_y < hauteur - rect_hauteur:
        rect_y += vitesse
    if keys[pygame.K_q] and rect_x > 0:
        rect_x -= vitesse
    if keys[pygame.K_d] and rect_x < largeur - rect_largeur:
        rect_x += vitesse

    # Effacement de l'écran
    fenetre.fill(blanc)

    # Dessin du rectangle
    pygame.draw.rect(fenetre, rouge, (rect_x, rect_y, rect_largeur, rect_hauteur))

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
