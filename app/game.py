import pygame
import sys

def main():
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
