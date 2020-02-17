import sys
import pygame
from shoot import Shoot
from ufo import UFO
from time import sleep


# check for events
def check_event(s_ship, g_set, screen, shoots, stats, play_but, ufos, points):
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            sys.exit()

        elif eve.type == pygame.KEYDOWN:
            key_down(eve, s_ship, g_set, screen, shoots, stats)

        elif eve.type == pygame.KEYUP:
            key_up(eve, s_ship)

        elif eve.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            check_play_but(stats, play_but, m_x, m_y, screen, g_set, s_ship, ufos, shoots, points)


def check_play_but(stats, play_but, m_x, m_y, screen, g_set, s_ship, ufos, shoots, points):
    if play_but.rect.collidepoint(m_x, m_y) and not stats.game_on:
        g_set.reset_speed()
        stats.reset_stat()
        stats.game_on = True

        points.prep_points()
        points.prep_h_points()
        points.prep_level()
        points.prep_ship()
        ufos.empty()
        shoots.empty()
        pygame.mouse.set_visible(False)

        ufo_fleet(g_set, screen, ufos, s_ship)
        s_ship.center_ship()


# sets back color, ship, shoots
def update_screen(screen, g_set, s_ship, shoots, ufos, play_but, stats, points):
    screen.fill(g_set.bgc)
    for shoot in shoots.sprites():
        shoot.shoot_draw()

    s_ship.blitme()
    ufos.draw(screen)
    points.show_points()

    if not stats.game_on:
        play_but.draw_button()

    pygame.display.flip()


# key up event
def key_up(eve, s_ship):
    if eve.key == pygame.K_RIGHT:
        s_ship.right = False

    elif eve.key == pygame.K_LEFT:
        s_ship.left = False


# key down events
def key_down(eve, s_ship, g_set, screen, shoots, stats):
    if eve.key == pygame.K_RIGHT:
        s_ship.right = True

    elif eve.key == pygame.K_LEFT:
        s_ship.left = True

    elif eve.key == pygame.K_SPACE:
        fire(shoots, g_set, screen, s_ship)

    elif eve.key == pygame.K_q:
        sys.exit()

    elif eve.key == pygame.K_p:
        stats.game_on = False





# updates bullet, ht check, removes bullet, re enables fleet
def update_shoot(shoots, ufos, g_set, screen, s_ship, points, stats):
    shoots.update()
    hit_check(shoots, ufos, points, stats, g_set)
    re_fleet(shoots, g_set, screen, ufos, s_ship, stats, points)
    for shoot in shoots.copy():
        if shoot.rect.bottom <= 0:
            shoots.remove(shoot)


# re enables fleet
def re_fleet(shoots, g_set, screen, ufos, s_ship, stats, points):
    if len(ufos) == 0:
        shoots.empty()
        stats.level += 1
        points.prep_level()
        g_set.inc_speed()
        ufo_fleet(g_set, screen, ufos, s_ship)


# hit check
def hit_check(shoots, ufos, points, stats, g_set):
    hit = pygame.sprite.groupcollide(shoots, ufos, True, True)
    if hit:
        for ufo in hit.values():
            stats.points += g_set.ufo_points * len(ufo)
            points.prep_points()
            check_high(stats, points)


# check max shoot limit
def fire(shoots, g_set, screen, s_ship):
    if len(shoots) < g_set.shoot_limit:
        new_shoot = Shoot(g_set, screen, s_ship)
        shoots.add(new_shoot)


# number of ufo in a row
def get_ufo(g_set, ufo_width):
    avail_space = g_set.width - 2 * ufo_width
    no_ufo = int(avail_space / (2 * ufo_width))
    return no_ufo


# creates individual ufo
def create_ufo(g_set, screen, ufos, no_ufo, row_no):
    for ufo_no in range(no_ufo):
        ufo = UFO(g_set, screen)
        ufo.x = ufo.rect.width + 2 * ufo.rect.width * ufo_no
        ufo.rect.x = ufo.x
        ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_no
        ufos.add(ufo)


# creates fleet
def ufo_fleet(g_set, screen, ufos, s_ship):
    ufo = UFO(g_set, screen)
    no_ufo = get_ufo(g_set, ufo.rect.width)
    no_row = get_ufo_row(g_set, s_ship.rect.height, ufo.rect.height)
    for row_no in range(no_row):
        create_ufo(g_set, screen, ufos, no_ufo, row_no)


# number of ufo rows
def get_ufo_row(g_set, ship_h, ufo_h):
    avail_space = g_set.height - (3 * ufo_h) - ship_h
    no_row = int(avail_space / (2 * ufo_h))
    return no_row


def ship_hit(g_set, stats, screen, s_ship, ufos, shoots, points):
    if stats.s_left > 0:
        stats.s_left -= 1

        ufos.empty()
        shoots.empty()
        points.prep_ship()

        ufo_fleet(g_set, screen, ufos, s_ship)
        s_ship.center_ship()

        sleep(0.5)
    else:
        pygame.mouse.set_visible(True)
        stats.game_on = False


def ufo_bottom(g_set, stats, screen, s_ship, ufos, shoots, points):
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            ship_hit(g_set, stats, screen, s_ship, ufos, shoots, points)
            break


# checks for display ends
def update_ufo(g_set, ufos, s_ship, stats, screen, shoots, points):
    check_fleet_ends(g_set, ufos)
    ufos.update()

    if pygame.sprite.spritecollideany(s_ship, ufos):
        ship_hit(g_set, stats, screen, s_ship, ufos, shoots, points)

    ufo_bottom(g_set, stats, screen, s_ship, ufos, shoots, points)


# check ends of fleet
def check_fleet_ends(g_set, ufos):
    for ufo in ufos.sprites():
        if ufo.check_ends():
            change_ufo_dir(g_set, ufos)
            break


# change ufo dir
def change_ufo_dir(g_set, ufos):
    for ufo in ufos.sprites():
        ufo.rect.y += g_set.ufo_drop
    g_set.ufo_direct *= -1


def check_high(stats, points):
    if stats.points > stats.h_points:
        stats.h_points = stats.points
        points.prep_h_points()
