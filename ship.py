import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen, img_l=80):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('img/sh.bmp')
        self.image = pygame.transform.scale(self.image, (img_l, img_l))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.right = False
        self.left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, g_set):
        if self.right and self.rect.right < self.screen_rect.right:
            self.center += g_set.ship_speed
        elif self.left and self.rect.left > self.screen_rect.left:
            self.center -= g_set.ship_speed

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
