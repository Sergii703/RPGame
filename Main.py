import pygame
from Constant import *
from Mob import Demon
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
                        self.player.die()
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
        self.mobs.append(Demon(self, x, y, LEFT))

    def render(self):  # прорисовка
        self.screen.blit(self.background, (0, 0))
        self.player.render(screen)
        self.player.render_ui(screen)
        for i in self.projective:
            i.render(screen)
        for i in self.mobs:
            i.render(screen)
        pygame.display.flip()

    def main_loop(self):  # основной цикл программ
        pygame.time.set_timer(USEREVENT+1, 100)
        self.add_demon(300, 200)
        while self.running == True:
            self.timer.tick(66)
            if self.player.state != DEAD:
                self.player.moove()
            for i in self.projective:
                i.moove()
            # print(self.projective)
            self.render()
            self.handle_events()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)