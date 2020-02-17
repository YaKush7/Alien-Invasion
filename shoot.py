import pygame
from pygame.sprite import Sprite


class Shoot(Sprite):

    def __init__(self, g_set, screen, s_ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, g_set.shoot_width, g_set.shoot_height)
        self.rect.centerx = s_ship.rect.centerx
        self.rect.top = s_ship.rect.top
        self.y = float(self.rect.y)
        self.color = g_set.shoot_color
        self.speed = g_set.shoot_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def shoot_draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
