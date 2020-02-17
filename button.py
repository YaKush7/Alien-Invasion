import pygame.font


class Button:
    def __init__(self, g_set, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.b_color = (0, 255, 0)
        self.t_color = (255,255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.make_msg(msg)

    def make_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.t_color, self.b_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.b_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
