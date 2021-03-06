import random
from Arrow import *


class Character():

    def __init__(self, game, name, x_start, y_start, dir, image_pack, speed):
        self.game = game
        self.state = ALIVE
        self.direction = dir
        self.x = x_start
        self.y = y_start
        self.speed = speed
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
        for i in self.game.mobs:
            if self.x != i.x and self.y != i.y:  # при ударении между собой демонов, чтобы дальше двигались
                self.contact_check(i)
        if self in self.game.mobs:
            self.contact_check(self.game.player)
        if self.x <= 0: self.blocked[LEFT] = 1
        if self.y <= 0: self.blocked[UP] = 1
        if self.x >= SCREEN_WIDTH - 60: self.blocked[RIGHT] = 1
        if self.y >= SCREEN_HEIGHT - 64: self.blocked[DOWN] = 1

    def contact_check(self, obj):  # что бы не было застревания
        if self.x >= obj.x - self.size and self.y <= obj.y + obj.size-SIZE_DIF and self.y >= obj.y - obj.size+SIZE_DIF and self.x <= obj.x + SIZE_DIF and obj.state != DEAD:
            self.blocked[RIGHT] = 1
        if self.x <= obj.x + obj.size + SIZE_DIF and self.y <= obj.y + obj.size-SIZE_DIF and self.y >= obj.y - obj.size+SIZE_DIF and self.x >= obj.x + obj.size - SIZE_DIF and obj.state != DEAD:
            self.blocked[LEFT] = 1
        if self.y >= obj.y - self.size and self.x <= obj.x + obj.size-SIZE_DIF and self.x >= obj.x - obj.size+SIZE_DIF and self.y <= obj.y + SIZE_DIF and obj.state != DEAD:
            self.blocked[DOWN] = 1
        if self.y <= obj.y + obj.size + SIZE_DIF and self.x <= obj.x + obj.size-SIZE_DIF and self.x >= obj.x - obj.size+SIZE_DIF and self.y >= obj.y + obj.size - SIZE_DIF and obj.state != DEAD:
            self.blocked[UP] = 1

    def random_moove(self):
        if self.blocked != [0, 0, 0, 0]:
            self.change_moove(random.randint(0, 3))

    def change_moove(self, direction):
        self.mooving = [0, 0,  0, 0]
        if 0 <= direction <= 3:
            self.mooving[direction] = 1

    def kill(self):
        self.hp = 0
        self.mp = 0
        self.state = DEAD
        self.game.corpses.append(self)  # добавояем труп демона
        if self in self.game.mobs:
            self.game.mobs.remove(self)  # удаляем уьитого демона