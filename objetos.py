import pygame,os, random

pygame.init()

class Coisas(pygame.sprite.Sprite):
    def __init__(self, caminho, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.Coisa = pygame.image.load(caminho).convert_alpha()
        self.rect = self.Coisa.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def mostrar(self,tela):
        tela.blit(self.Coisa,self.rect)

class Massan(pygame.sprite.Sprite):
    def __init__(self, caminho, x,y,v,d):
        pygame.sprite.Sprite.__init__(self)
        self.Maca = pygame.image.load(caminho).convert_alpha()
        self.rect = self.Maca.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.comeu = False
        self.vermelha = v
        self.dourada = d

    def mostrar(self,tela):
        tela.blit(self.Maca,self.rect)

class Textos():
    def __init__(self, texto,tam,r,g,b):
        self.caminho = os.path.join("fontes","VCR_OSD_MONO.ttf")
        self.texto = pygame.font.Font(self.caminho,tam)
        self.cor = (r,g,b)
        self.mostrarTexto = self.texto.render(texto,True,self.cor)
    def mostrarTextoNaTela(self,tela,x,y):
        tela.blit(self.mostrarTexto,(x,y))
