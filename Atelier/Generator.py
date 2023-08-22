import pygame
from a_star_generator import a_star_generator

# Initialisation de Pygame
pygame.init()

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
vert = (0, 255, 0)
taille_case = 30

# Générer la grille
grid_data = a_star_generator(max_size=10, max_obstacles=20)

# Dimensions de la fenêtre
largeur = grid_data["grid_size"][0] * taille_case
hauteur = grid_data["grid_size"][1] * taille_case

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("A* Grid Visualizer")

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenetre.fill(blanc)

    # Afficher la grille
    for x in range(grid_data["grid_size"][0]):
        for y in range(grid_data["grid_size"][1]):
            rect = pygame.Rect(x * taille_case, y * taille_case, taille_case, taille_case)
            if [x, y] == grid_data["start"]:
                pygame.draw.circle(fenetre, rouge, rect.center, taille_case // 2)
            elif [x, y] == grid_data["end"]:
                pygame.draw.circle(fenetre, vert, rect.center, taille_case // 2)
            elif [x, y] in grid_data["obstacles"]:
                pygame.draw.rect(fenetre, noir, rect)
            else:
                pygame.draw.rect(fenetre, blanc, rect, 1)

    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
