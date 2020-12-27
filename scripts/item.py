import pygame, random

class Item(pygame.sprite.Sprite):
    def __init__(self, nome):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(nome).convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, 600)
        self.y = random.randint(0, 400)

        self.rect[0] = self.x
        self.rect[1] = self.y

        self.pontuacao = 0

    def update(self):
        self.rect[0] = self.x
        self.rect[1] = self.y

    #atualiza o item para uma posicao aleatoria
    def atualiza(self):
        self.x = random.randint(0, 750)
        self.y = random.randint(0, 550)
        self.pontuacao += 1

    def getPontuacao(self):
        return self.pontuacao

    def rec(self):
        self.pontuacao = 0