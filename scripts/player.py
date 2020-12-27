import pygame, random
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self, nome):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(nome).convert_alpha()
        self.rect = self.image.get_rect()

        self.x = 400
        self.y = 300

        self.rect[0] = self.x
        self.rect[1] = self.y

    def update(self):
        self.rect[0] = self.x
        self.rect[1] = self.y

    def mover(self, x, y):

        velocidade_player = 10

        if x > 0 and self.rect[0] != 750:
            self.x += velocidade_player
        if x < 0 and self.rect[0] != 0:
            self.x -= velocidade_player
        if y > 0 and self.rect[1] != 550:
            self.y += velocidade_player
        if y < 0 and self.rect[1] != 0:
            self.y -= velocidade_player

    def atualiza(self):
        self.x = 400
        self.y = 300

        self.rect[0] = self.x
        self.rect[1] = self.y