import pygame
pygame.init()
largura=800
altura=600

class Personagem(pygame.sprite.Sprite):
    def __init__(self, xP, yP):
        pygame.sprite.Sprite.__init__(self)
        self.Char = pygame.image.load("Images/Personagem/bonecodefrenteparado.png").convert_alpha()
        self.rect = self.Char.get_rect()
        self.x = xP
        self.y = yP
        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.andando = 1
    def mostrar(self, tela):
        tela.blit(self.Char,self.rect)

class Coisas(pygame.sprite.Sprite):
    def __init__(self, caminho, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.Muro = pygame.image.load(caminho).convert_alpha()
        self.rect = self.Muro.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    def mostrar(self,tela):
        tela.blit(self.Muro,self.rect)