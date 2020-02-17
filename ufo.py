import pygame
from pygame.sprite import Sprite


class UFO(Sprite):

    def __init__(self, g_set, screen):
        super().__init__()
        self.screen = screen
        self.set = g_set
        self.image = pygame.image.load('img/1ufo.bmp')
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.set.ufo_speed * self.set.ufo_direct)
        self.rect.x = self.x

    def check_ends(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
