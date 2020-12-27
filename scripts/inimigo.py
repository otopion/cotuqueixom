import pygame, random
from pygame.locals import *

class Inimigo(pygame.sprite.Sprite):

    def __init__(self, nome, velocidade):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(nome).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect[0] = random.randint(10, 700)
        self.rect[1] = 0

        self.velocidade = velocidade
        self.velocidadeInicial = velocidade

    def update(self):
        self.rect[1] += self.velocidade
        if (self.rect[1] >= 600):
            self.rect[0] = random.randint(10, 700)
            self.rect[1] = 0
            if self.velocidade != 11:
                self.velocidade += 1

    def atualiza(self):
        self.rect[0] = random.randint(10, 700)
        self.rect[1] = 0

        self.velocidade = self.velocidadeInicial