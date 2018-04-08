import pygame

from Arrow import Arrow, Projective
from Constant import *


class Mob():

    def __init__(self, game, name, x_start, y_start, dir, image_pack):
        self.game = game
        self.state = ALIVE
        self.direction = dir
        self.x = x_start
        self.y = y_start
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = image_pack
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


class Demon(Mob):
    def __init__(self, game, x_start, y_start, dir):
        self.image_pack = ['pic/demonr.png', 'pic/demond.png', 'pic/demonl.png', 'pic/demonu.png']
        self.speed = 5
        Mob.__init__(self, game, 'Demon', x_start, y_start, LEFT, self.image_pack)
