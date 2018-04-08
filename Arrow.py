import pygame
from Constant import *

class Projective():
    def __init__(self, game, x_start, y_start, dir, image_pack):
        self.game = game
        self.x = x_start
        self.y = y_start
        self.direction = dir
        self.image = pygame.image.load(image_pack).convert_alpha()
        self.images = []
        self.images.append(self.image.subsurface(0, 0, 64, 64))
        self.images.append(self.image.subsurface(64, 0, 64, 64))
        self.images.append(self.image.subsurface(128, 0, 64, 64))
        self.images.append(self.image.subsurface(192, 0, 64, 64))

    def render(self, screen):
        screen.blit(self.images[self.direction], (self.x, self.y))

    def moove(self):
        if self.direction == RIGHT:
            self.x += self.speed
        elif self.direction == DOWN:
            self.y += self.speed
        elif self.direction == LEFT:
            self.x -= self.speed
        else:
            self.y -= self.speed

        if self.x > SCREEN_WIDTH or self.x < -32 or self.y > SCREEN_HEIGHT or self.y < -32:
            self.remove()

    def remove(self):
        self.game.projective.remove(self)


class Arrow(Projective):

    def __init__(self, game, x_start, y_start, dir):
        self.image = 'pic/arrow.png'
        self.speed = 5
        Projective.__init__(self, game, x_start, y_start, dir, self.image)
