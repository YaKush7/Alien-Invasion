import pygame
from settings import Settings
from ship import Ship
import game_fuct as gf
from pygame.sprite import Group
from stats import Stats
from button import Button
from points import Points


def main():
    pygame.init()
    g_set = Settings()
    stats = Stats(g_set)
    screen = pygame.display.set_mode((g_set.width, g_set.height))
    points = Points(g_set, screen, stats)
    pygame.display.set_caption(g_set.title)
    s_ship = Ship(screen)
    shoots = Group()
    ufos = Group()
    play_but = Button(g_set, screen, "Play")
    gf.ufo_fleet(g_set, screen, ufos, s_ship)

    while 1:
        gf.check_event(s_ship, g_set, screen, shoots, stats, play_but, ufos, points)

        if stats.game_on:
            s_ship.update(g_set)
            gf.update_shoot(shoots, ufos, g_set, screen, s_ship, points, stats)
            gf.update_ufo(g_set, ufos, s_ship, stats, screen, shoots, points)

        gf.update_screen(screen, g_set, s_ship, shoots, ufos, play_but, stats, points)


main()
