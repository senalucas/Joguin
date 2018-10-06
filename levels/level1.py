import pygame,os,objetos, random,char,definicoes

pygame.init()


class N1():
    def __init__(self,largura,altura):
        self.img = definicoes.Diretorios()
        self.macad = self.img.macad
        self.macav = self.img.macav
        self.pontuacao = 0

        self.p1 = objetos.Coisas(self.img.ps1,400,60)
        self.p2 = objetos.Coisas(self.img.ps2,66,300)
        self.p3 = objetos.Coisas(self.img.ps3,400,540)
        self.p4 = objetos.Coisas(self.img.ps4,734,300)
        self.p = objetos.Coisas(self.img.porta1,largura/2,55)

        self.listaDeMacas = []

    def criarmassan(self):
        count = 1
        for i in range(0,10):
            j = random.randint (1, 10)
            if (j <= 3 and count <= 3):
                x = random.randint(135,700)
                y = random.randint(100,500)
                self.maca = objetos.Massan(self.macad,x,y,False,True)
                self.listaDeMacas.append(self.maca)
                count+=1
            else:
                x = random.randint(135,700)
                y = random.randint(100,500)
                self.maca = objetos.Massan(self.macav,x,y,True,False)
                self.listaDeMacas.append(self.maca)


    def get_maca(self):
        return self.listaDeMacas

    def movimaca(self,j,tela):
        x = len(self.listaDeMacas)
        i = 0
        self.pontuacao = 0
        while i < x:
            z = self.listaDeMacas[i]
            z.mostrar(tela)
            if(pygame.sprite.collide_rect(j,self.listaDeMacas[i])):
                if self.listaDeMacas[i].vermelha == True:
                    self.maca = objetos.Massan(self.macav,770,570,True,False)
                    self.listaDeMacas[i] = self.maca
                elif self.listaDeMacas[i].dourada == True:
                    self.maca = objetos.Massan(self.macav,770,570,False,True)
                    self.listaDeMacas[i] = self.maca
                self.listaDeMacas[i].comeu = True
            #break
            i+=1

        for i in self.listaDeMacas:
            if i.comeu == True:
                if i.vermelha == True:
                    self.pontuacao +=1
                elif i.dourada == True:
                    self.pontuacao +=3
        contador = 0
        for i in self.listaDeMacas:
            if i.comeu == True:
                contador +=1
        if contador == len(self.listaDeMacas):
            self.criarmassan()

    def get_pontuacao(self):
        return self.pontuacao

    def mostrarlvl(self,tela):
        self.p1.mostrar(tela)
        self.p2.mostrar(tela)
        self.p3.mostrar(tela)
        self.p4.mostrar(tela)
        self.p.mostrar(tela)
