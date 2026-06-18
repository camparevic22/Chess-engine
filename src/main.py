import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
rect = pygame.draw.rect(screen, (0, 0, 0), (100, 100, 50, 50))
running = True
pygame.display.set_caption("Šahovska tabla")

VELICINA_POLJA = 600 // 8
SVETLA_BOJA = (240, 217, 181)
TAMNA_BOJA = (181, 136, 99)

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                boja = SVETLA_BOJA
            else:
                boja = TAMNA_BOJA
            screen.fill(boja, (i * VELICINA_POLJA, j * VELICINA_POLJA, VELICINA_POLJA, VELICINA_POLJA))
    pygame.display.flip()
    