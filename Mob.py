import random

import pygame

from Arrow import Arrow, Projective
from Constant import *
from Arrow import *


class Mob():

    def __init__(self, game, name, x_start, y_start, dir, image_pack):
        self.game = game
        self.state = ALIVE
        self.direction = dir
        self.x = x_start
        self.y = y_start
        self.size = 48
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.blocked = [0, 0, 0, 0]
        self.mooving = [0, 0, 0, 0]
        self.image_pack = image_pack
        self.images = []
        self.spell_casted = 0
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0, 0, 64, 64))
            i.append(temp.subsurface(64, 0, 64, 64))
            i.append(temp.subsurface(128, 0, 64, 64))
            self.images.append(i)

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def moove(self):
        self.block_check()
        if self.mooving[RIGHT] == 1 and self.blocked[RIGHT] == 0:
            self.direction = RIGHT
            self.x += self.speed
        if self.mooving[DOWN] == 1 and self.blocked[DOWN] == 0:
            self.direction = DOWN
            self.y += self.speed
        if self.mooving[LEFT] == 1 and self.blocked[LEFT] == 0:
            self.direction = LEFT
            self.x -= self.speed
        if self.mooving[UP] == 1 and self.blocked[UP] == 0:
            self.direction = UP
            self.y -= self.speed

    def block_check(self):
        self.blocked = [0, 0, 0, 0]
        if self.x <= 0: self.blocked[LEFT] = 1
        if self.y <= 0: self.blocked[UP] = 1
        if self.x >= SCREEN_WIDTH - 60: self.blocked[RIGHT] = 1
        if self.y >= SCREEN_HEIGHT - 64: self.blocked[DOWN] = 1

    def random_moove(self):
        self.mooving = [0, 0, 0, 0]
        self.mooving[random.randint(0, 3)] = 1

class Demon(Mob):
    def __init__(self, game, x_start, y_start, dir):
        self.image_pack = ['pic/demonr.png', 'pic/demond.png', 'pic/demonl.png', 'pic/demonu.png']
        self.speed = 1
        Mob.__init__(self, game, 'Demon', x_start, y_start, dir, self.image_pack)
