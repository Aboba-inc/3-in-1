import pygame

background = (0, 0, 0)
(width, height) = (900, 800)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3in1")

running = True
while running:

    screen.fill(background)
    pygame.display.flip()