from Character import *


class Player(Character):

    def __init__(self, game, name):
        Character.__init__(self, game, name, START_X, START_Y, RIGHT, PLAYER_IMAGE_PACK, PLAYER_SPEED)

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
                self.kill()

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