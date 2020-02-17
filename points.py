import pygame.font
from pygame.sprite import Group
from ship import Ship


class Points:
    def __init__(self,g_set, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.g_set = g_set
        self.stats = stats

        self.t_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_points()
        self.prep_h_points()
        self.prep_level()
        self.prep_ship()

    def prep_points(self):
        round_points = int(round(self.stats.points, -1))
        points_str = "{:,}".format(round_points)
        self.points_img = self.font.render(points_str, True, self.t_color, self.g_set.bgc)
        self.points_rect = self.points_img.get_rect()
        self.points_rect.right = self.screen_rect.right - 20
        self.points_rect.top = 5

    def prep_h_points(self):
        round_h_points = int(round(self.stats.h_points, -1))
        points_str = "{:,}".format(round_h_points)
        self.points_h_img = self.font.render(points_str, True, self.t_color, self.g_set.bgc)
        self.points_h_rect = self.points_img.get_rect()
        self.points_h_rect.centerx = self.screen_rect.centerx
        self.points_h_rect.top = 5

    def prep_level(self):
        level_str = str(self.stats.level)
        self.l_img = self.font.render(level_str, True, self.t_color, self.g_set.bgc)
        self.l_rect = self.l_img.get_rect()
        self.l_rect.right = self.screen_rect.right - 20
        self.l_rect.top = 38

    def prep_ship(self):
        self.ships = Group()
        for ship_n in range(self.stats.s_left):
            ship = Ship(self.screen, 40)
            ship.rect.x = 10 + ship_n * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_points(self):
        self.screen.blit(self.points_img, self.points_rect)
        self.screen.blit(self.points_h_img, self.points_h_rect)
        self.screen.blit(self.l_img, self.l_rect)
        self.ships.draw(self.screen)

