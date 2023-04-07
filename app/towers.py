import pygame


class Tower:
    type = "Tower"
    color = (0, 0, 0)
    width = 1
    height = 1

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, self.color, pygame.Rect(x, y, self.width, self.height))


class WeakTower(Tower):
    type = "Weak tower"
    color = (255, 255, 255)
    width = 35
    height = 35
