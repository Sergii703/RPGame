import pygame

from Arrow import Arrow
from Constant import *


class Player():

    def __init__(self, game, name):
        self.game = game
        self.state = ALIVE
        self.direction = UP
        self.x = START_X
        self.y = START_Y
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.size = 48
        self.blocked = [0, 0, 0, 0]
        self.mooving = [0, 0, 0, 0]
        self.image_pack = ['pic/archerr.png', 'pic/archerd.png', 'pic/archerl.png', 'pic/archeru.png']
        self.images = []
        self.spell_casted = 0
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0, 0, 64, 64))
            i.append(temp.subsurface(64, 0, 64, 64))
            i.append(temp.subsurface(128, 0, 64, 64))
            self.images.append(i)

    def moove(self):
        self.block_check()
        if self.mooving[RIGHT] == 1 and self.blocked[RIGHT] == 0:
            self.direction = RIGHT
            self.x += PLAYER_SPEED
        if self.mooving[DOWN] == 1 and self.blocked[DOWN] == 0:
            self.direction = DOWN
            self.y += PLAYER_SPEED
        if self.mooving[LEFT] == 1 and self.blocked[LEFT] == 0:
            self.direction = LEFT
            self.x -= PLAYER_SPEED
        if self.mooving[UP] == 1 and self.blocked[UP] == 0:
            self.direction = UP
            self.y -= PLAYER_SPEED

    def block_check(self):
        self.blocked = [0, 0, 0, 0]
        for i in self.game.mobs:
            self.contact_check(i)
        if self.x <= 0: self.blocked[LEFT] = 1
        if self.y <= 0: self.blocked[UP] = 1
        if self.x >= SCREEN_WIDTH - 60: self.blocked[RIGHT] = 1
        if self.y >= SCREEN_HEIGHT - 64: self.blocked[DOWN] = 1

    def contact_check(self, obj):
        if self.x >= obj.x - self.size and self.y <= obj.y + obj.size-SIZE_DIF and self.y >= obj.y - obj.size+SIZE_DIF and self.x <= obj.x + SIZE_DIF*2:
            self.blocked[RIGHT] = 1
        if self.x <= obj.x + obj.size + SIZE_DIF and self.y <= obj.y + obj.size-SIZE_DIF and self.y >= obj.y - obj.size+SIZE_DIF and self.x >= obj.x + obj.size - SIZE_DIF*2:
            self.blocked[LEFT] = 1
        if self.y >= obj.y - self.size and self.x <= obj.x + obj.size-SIZE_DIF and self.x >= obj.x - obj.size+SIZE_DIF and self.y <= obj.y + SIZE_DIF*2:
            self.blocked[DOWN] = 1
        if self.y <= obj.y + obj.size + SIZE_DIF and self.x <= obj.x + obj.size-SIZE_DIF and self.x >= obj.x - obj.size+SIZE_DIF and self.y >= obj.y + obj.size - SIZE_DIF*2:
            self.blocked[UP] = 1

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):
        screen.blit(pygame.image.load('pic/hpframe.png'),(self.x+12, self.y+58))
        screen.blit(pygame.image.load('pic/mpframe.png'), (self.x + 12, self.y + 63))
        m = 1
        z = self.hp // 5
        while m <= z:
            screen.blit(pygame.image.load('pic/hptick.png'), (self.x + 11+m*2, self.y + 59))
            m += 1
        m = 1
        z = self.mp // 5
        while m <= z:
            screen.blit(pygame.image.load('pic/mptick.png'), (self.x + 11 + m * 2, self.y + 64))
            m += 1

    def die(self):
        self.hp = 0
        self.mp = 0
        self.state = DEAD

    def tick(self):
        if self.state != DEAD:
            self.mp += MP_REG
            self.hp += HP_REG
            if self.mp > MAX_MP:
                self.mp = MAX_MP
            if self.hp > MAX_HP:
                self.hp = MAX_HP
            if pygame.time.get_ticks() > self.spell_casted + 1000:
                self.state = ALIVE
            if self.hp <= 0:
                self.die()

    def shoot_z(self):
        if self.mp >= SKILL1_COST and self.state != SHOOT:
            self.mp -= SKILL1_COST
            self.state = SHOOT
            self.spell_casted = pygame.time.get_ticks()
            if self.direction ==RIGHT:
                self.__shoot__(12, 0)
            elif self.direction == DOWN:
                self.__shoot__(0, 12)
            elif self.direction == LEFT:
                self.__shoot__(-12, 0)
            else:
                self.__shoot__(0, -12)

    def __shoot__(self, x, y):
        self.game.projective.append(Arrow(self.game, self.x+x, self.y+y, self.direction))