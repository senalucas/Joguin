import pygame,os,objetos, random,char,definicoes

pygame.init()


class N1():
    def __init__(self,largura,altura):
        self.img = definicoes.Diretorios()
        self.macad = self.img.macad
        self.macav = self.img.macav

        self.p1 = objetos.Coisas(self.img.ps1,400,60)
        self.p2 = objetos.Coisas(self.img.ps2,66,300)
        self.p3 = objetos.Coisas(self.img.ps3,400,540)
        self.p4 = objetos.Coisas(self.img.ps4,734,300)

        self.listaDeMacas = []

        for i in range(0,10):
            x = random.randint(135,700)
            y = random.randint(100,500)
            self.maca = objetos.Coisas(self.macav,x,y)
            self.listaDeMacas.append(self.maca)

        self.grupo = pygame.sprite.Group()
        self.grupo.add(self.p1)
        self.grupo.add(self.p2)
        self.grupo.add(self.p3)
        self.grupo.add(self.p4)
        self.p = objetos.Coisas(self.img.porta1,largura/2,55)

    def get_grupo(self):
        return self.grupo

    def mostrarlvl(self,tela):
        self.p1.mostrar(tela)
        self.p2.mostrar(tela)
        self.p3.mostrar(tela)
        self.p4.mostrar(tela)
        self.p.mostrar(tela)
        for i in self.listaDeMacas:
            i.mostrar(tela)

