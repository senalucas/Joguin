import pygame
pygame.init()
largura=800
altura=600

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Char = pygame.image.load("Images/Personagem/bonecodefrenteparado.png").convert_alpha()
        self.rect = self.Char.get_rect()
        self.x = largura/2
        self.y = altura-300
        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.andando = 2
    def mostrar(self, tela):
        tela.blit(self.Char,self.rect)

class Portao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Portao = pygame.image.load("Images/Elementos/portao1.png").convert_alpha()
        self.rect = self.Portao.get_rect()
        self.rect.centerx = 400
        self.rect.centery = altura-70
    def mostrar(self,tela):
        tela.blit(self.Portao,self.rect)

class Parede1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Muro = pygame.image.load("Images/Elementos/parede1.png").convert_alpha()
        self.rect = self.Muro.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 100
    def mostrar(self,tela):
        tela.blit(self.Muro,self.rect)

class Parede2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Muro = pygame.image.load("Images/Elementos/parede2.png").convert_alpha()
        self.rect = self.Muro.get_rect()
        self.rect.centerx = 84
        self.rect.centery = 316
    def mostrar(self,tela):
        tela.blit(self.Muro,self.rect)

class Parede3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Muro = pygame.image.load("Images/Elementos/parede3.png").convert_alpha()
        self.rect = self.Muro.get_rect()
        self.rect.centerx = largura-401
        self.rect.centery = altura-69
    def mostrar(self,tela):
        tela.blit(self.Muro,self.rect)

class Parede4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Muro = pygame.image.load("Images/Elementos/parede4.png").convert_alpha()
        self.rect = self.Muro.get_rect()
        self.rect.centerx = largura-84
        self.rect.centery = altura-284
    def mostrar(self,tela):
        tela.blit(self.Muro,self.rect)
