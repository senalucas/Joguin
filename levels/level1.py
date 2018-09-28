import pygame,os,objetos,char,definicoes

pygame.init()

class N1():
    def __init__(self,largura,altura):
        self.img = definicoes.Diretorios()

        self.p1 = objetos.Coisas(self.img.ps1,400,80)
        self.p2 = objetos.Coisas(self.img.ps2,84,295)
        self.p3 = objetos.Coisas(self.img.ps3,399,520)
        self.p4 = objetos.Coisas(self.img.ps4,715,294)

        self.grupo = pygame.sprite.Group()
        self.grupo.add(self.p1)
        self.grupo.add(self.p2)
        self.grupo.add(self.p3)
        self.grupo.add(self.p4)
        self.p = objetos.Coisas(self.img.porta1,largura/2,520)

    def get_grupo(self):
        return self.grupo

    def mostrarlvl(self,tela):
        self.p1.mostrar(tela)
        self.p2.mostrar(tela)
        self.p3.mostrar(tela)
        self.p4.mostrar(tela)
        self.p.mostrar(tela)
