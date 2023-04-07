import pygame


class Tower:
    
    type = "Tower"

    color = (0, 0, 0)
    width = height = 1
    rect = pygame.Rect(0, 0, width, height)

    is_drawn = False

    def set_rect(self, x, y):
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, surface, x, y):

        if self.is_drawn:

            pygame.draw.rect(surface, (0, 0, 0), self.rect)
            self.set_rect(x, y)
            pygame.draw.rect(surface, self.color, self.rect)

        else:

            self.is_drawn = True
            self.set_rect(x, y)
            pygame.draw.rect(surface, self.color, self.rect)


class WeakTower(Tower):

    type = "Weak tower"
    color = pygame.Color(255, 255, 255)
    width = height = 35
