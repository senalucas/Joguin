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


        self.grupo = pygame.sprite.Group()
        self.grupo.add(self.p1)
        self.grupo.add(self.p2)
        self.grupo.add(self.p3)
        self.grupo.add(self.p4)
        self.p = objetos.Coisas(self.img.porta1,largura/2,55)

    def get_maca(self):
        return self.listaDeMacas

    def movimaca(self,j,tela):
        x = len(self.listaDeMacas)
        i = 0
        pontuacao = 0
        while i < x:
            z = self.listaDeMacas[i]
            z.mostrar(tela)
            if(pygame.sprite.collide_rect(j,self.listaDeMacas[i])):
                if self.listaDeMacas[i].vermelha == True:
                    self.maca = objetos.Massan(self.macav,770,570,True,False)
                    self.listaDeMacas[i] = self.maca
                elif self.listaDeMacas[i].dourada == True:
                    self.maca = objetos.Massan(self.macad,770,570,True,False)
                    self.listaDeMacas[i] = self.maca
                self.listaDeMacas[i].comeu = True

            #break
            i+=1

    def mostrarlvl(self,tela):
        self.p1.mostrar(tela)
        self.p2.mostrar(tela)
        self.p3.mostrar(tela)
        self.p4.mostrar(tela)
        self.p.mostrar(tela)
