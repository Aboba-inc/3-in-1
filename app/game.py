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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill(background)
        weak_tower = towers.WeakTower()
        weak_tower.draw(surface, 100, 200)
        pygame.display.flip()


if __name__ == "__main__":
    main()
