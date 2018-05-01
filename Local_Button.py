import pygame
from Button import Button
import random
from Constant import *
from Mob import *
from Player import *


class ButtonAddDemon(Button):
    def __init__(self, x, y, button_text, game):
        Button.__init__(self, x, y, button_text)
        self.game = game

    def use(self):
        self.game.add_demon(random.randint(0, SCREEN_WIDTH - 64), random.randint(0, SCREEN_HEIGHT - 64))