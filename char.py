import pygame,os,levels.level1,objetos,random,definicoes

pygame.init()

class Personagem(pygame.sprite.Sprite):
    def __init__(self, xP, yP):
        pygame.sprite.Sprite.__init__(self)
        self.Char = pygame.image.load("Images/Personagem/bonecodefrenteparado.png").convert_alpha()
        self.rect = self.Char.get_rect()
        self.x = xP
        self.y = yP
        self.rect.centerx = self.x
        self.rect.centery = self.y

        self.andando = 2

    def mostrar(self, tela):
        tela.blit(self.Char,self.rect)


    def movimentacao(self,j,p1,p2,p3,p4):
        clock = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        if(pygame.sprite.collide_rect(j,p1)) :
            j.rect = j.rect.move(0,+(j.andando))
        elif(pygame.sprite.collide_rect(j,p2)):
            j.rect = j.rect.move(+(j.andando),0)
        elif(pygame.sprite.collide_rect(j,p3)):
            j.rect = j.rect.move(0,-(j.andando))
        elif(pygame.sprite.collide_rect(j,p4)):
            j.rect = j.rect.move(-(j.andando),0)
        else:
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                if clock % 2 == 0:
                    self.Char = pygame.image.load("Images/Personagem/bonecodecostas1.png")
                else:
                    self.Char = pygame.image.load("Images/Personagem/bonecodecostas2.png")
                self.rect = self.rect.move(0,-(self.andando))
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                if clock % 2 == 0:
                    self.Char = pygame.image.load("Images/Personagem/bonecodefrente1.png")
                else:
                    self.Char = pygame.image.load("Images/Personagem/bonecodefrente2.png")
                self.rect = self.rect.move(0,+(self.andando))
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if clock % 2 == 0:
                    self.Char = pygame.image.load("Images/Personagem/bonecopraesquerda1.png")
                else:
                    self.Char = pygame.image.load("Images/Personagem/bonecopraesquerda2.png")
                self.rect = self.rect.move(-(self.andando),0)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if clock % 2 == 0:
                    self.Char = pygame.image.load("Images/Personagem/bonecopradireita1.png")
                else:
                    self.Char = pygame.image.load("Images/Personagem/bonecopradireita2.png")
                self.rect = self.rect.move(+(self.andando),0)

class Fantasma(pygame.sprite.Sprite):
    def __init__(self,x,y,tipo):
        self.dir = definicoes.Diretorios()
        pygame.sprite.Sprite.__init__(self)
        self.Fantasma = pygame.image.load(self.dir.ghostd).convert_alpha()
        
        self.rect = self.Fantasma.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.tipo = tipo
        self.andando = 3
        self.p = False
    def mostrar(self,tela):
        tela.blit(self.Fantasma,self.rect)

    def movimentar(self,p1,p2,p3,p4,j):
        perdeu = objetos.Textos("Morreu",25,255,255,255)
        if self.tipo <= 10:
            if not pygame.sprite.collide_rect(self,p3):
                self.rect = self.rect.move(0,self.andando)
                if pygame.sprite.collide_rect(self,p3):
                    x =  random.randint(135,700)
                    y = random.randint(100,500)
                    self.rect.centerx = x
                    self.rect.centery = y
        if self.tipo > 10 and self.tipo <= 20:
            if not pygame.sprite.collide_rect(self,p4):
                self.rect = self.rect.move(self.andando,0)
                if pygame.sprite.collide_rect(self,p4):
                    x = random.randint(135,700)
                    y = random.randint(100,500)
                    self.rect.centerx = x
                    self.rect.centery = y
        if self.tipo > 20 and self.tipo <= 30:
            if not pygame.sprite.collide_rect(self,p1):
                self.rect = self.rect.move(0,-self.andando)
                if pygame.sprite.collide_rect(self,p1):
                    x = random.randint(135,700)
                    y = random.randint(100,500)
                    self.rect.centerx = x
                    self.rect.centery = y
        if self.tipo > 30:
            if not pygame.sprite.collide_rect(self,p2):
                self.rect = self.rect.move(-self.andando,0)
                if pygame.sprite.collide_rect(self,p2):
                    x = random.randint(135,700)
                    y = random.randint(100,500)
                    self.rect.centerx = x
                    self.rect.centery = y

        if pygame.sprite.collide_rect(self,j):
            self.p = True

    def pegouFantasma(self):
        return self.p
