import pygame
import towers


def main():
    background = (0, 0, 0)
    (width, height) = (900, 800)

    pygame.init()
    pygame.display.set_caption("Tower Defense")
    surface = pygame.display.set_mode((width, height))

    surface.fill(background)
    running = True

    weak_tower = towers.WeakTower()

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                weak_tower.draw(surface, x, y)

        pygame.display.flip()


if __name__ == "__main__":
    main()
