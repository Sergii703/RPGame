import pygame
import _random
from Constant import *
from Mob import *
from Player import *
from pygame.locals import *
from Arrow import *


class Main():
    def __init__(self, screen):
        # self.name = name
        self.screen = screen
        self.player = Player(self, 'Geroes')
        self.projective = []
        self.mobs = []
        self.corpses = []
        self.background = pygame.image.load('pic/black.jpg')
        self.timer = pygame.time.Clock()
        self.running = True
        self.main_loop()
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            # Передвижение игрока, при нажатии клавиши
            elif event.type == USEREVENT+1:
                self.player.tick()
            elif event.type == USEREVENT+2:
                for i in self.mobs:
                    i.random_moove()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.mooving = [1, 0, 0, 0]
                if event.key == K_DOWN:
                    self.player.mooving = [0, 1, 0, 0]
                if event.key == K_LEFT:
                    self.player.mooving = [0, 0, 1, 0]
                if event.key == K_UP:
                    self.player.mooving = [0, 0, 0, 1]

            # Другие действия игрока
                if event.key == K_SPACE:
                    if self.player.state != DEAD:
                        self.player.kill()
                    else:
                        self.player.state = ALIVE
                if event.key == K_z:
                    self.player.shoot_z()

            # При отжатии клавиши
            elif event.type == KEYUP:
                if event.key == K_UP:
                    self.player.mooving[UP] = 0
                if event.key == K_DOWN:
                    self.player.mooving[DOWN] = 0
                if event.key == K_RIGHT:
                    self.player.mooving[RIGHT] = 0
                if event.key == K_LEFT:
                    self.player.mooving[LEFT] = 0

    def add_demon(self, x, y):
        self.mobs.append(Demon(self, x, y, UP))  # добаление демонов
        self.mobs[-1].mooving = [0, 0, 0, 1]  # движение демонов

    def render(self):  # прорисовк
        self.screen.blit(self.background, (0, 0))
        for i in self.corpses:
            i.render(screen)
        self.player.render(screen)
        self.player.render_ui(screen)
        for i in self.projective:
            i.render(screen)
        for i in self.mobs:
            i.render(screen)
        pygame.display.flip()

    def moove(self):
        # moove of all objects
        if self.player.state != DEAD:
            self.player.moove()
        for i in self.projective:
            i.moove()
        for i in self.mobs:
            if i.state != DEAD:
                i.moove()


    def main_loop(self):  # основной цикл программ
        pygame.time.set_timer(USEREVENT + 1, 100)
        pygame.time.set_timer(USEREVENT + 2, 1000)
        for i in range(5):
            self.add_demon(random.randint(0, SCREEN_WIDTH - 64), random.randint(0, SCREEN_HEIGHT - 64))
        while self.running == True:
            self.timer.tick(66)
            self.moove()
            self.render()
            self.handle_events()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)