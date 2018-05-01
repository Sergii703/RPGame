import pygame
from Constant import *

CORNERSTONE = 'pic/Cornerstone.ttf'
WHITE = (200, 30, 30)


class Button():
    def __init__(self, x, y, button_text, font_style=CORNERSTONE, font_color=WHITE, font_size=20):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.button_text = button_text
        self.font_style = font_style
        self.font_color = font_color
        self.active = True

        pygame.font.init()

        self.font = pygame.font.Font(font_style, font_size)

    def render(self, screen):
        screen.blit(self.font.render(self.button_text, 0, self.font_color), (self.x, self.y))

    def click_check(self, click_x, click_y):
        width = len(self.button_text) * self.font_size * 0.6
        height = self.font_size
        if click_x >= self.x and click_y <= self.y + height and click_y >= self.y and click_x <= self.x + width and self.active == True:
            self.use()

    def use(self):
        print('OOOOO')

