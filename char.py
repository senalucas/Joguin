import pygame,os,levels.level1

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
            if keys[pygame.K_w]:
                if clock % 2 == 0:
                    self.Char = pygame.image.load("Images/Personagem/bonecodecostas1.png")
                else:
                    self.Char = pygame.image.load("Images/Personagem/bonecodecostas2.png")
                self.rect = self.rect.move(0,-(self.andando))
            if keys[pygame.K_s]:
                if clock % 2 == 0:
                    self.Char = pygame.image.load("Images/Personagem/bonecodefrente1.png")
                else:
                    self.Char = pygame.image.load("Images/Personagem/bonecodefrente2.png")
                self.rect = self.rect.move(0,+(self.andando))
            if keys[pygame.K_a]:
                if clock % 2 == 0:
                    self.Char = pygame.image.load("Images/Personagem/bonecopraesquerda1.png")
                else:
                    self.Char = pygame.image.load("Images/Personagem/bonecopraesquerda2.png")
                self.rect = self.rect.move(-(self.andando),0)
            if keys[pygame.K_d]:
                if clock % 2 == 0:
                    self.Char = pygame.image.load("Images/Personagem/bonecopradireita1.png")
                else:
                    self.Char = pygame.image.load("Images/Personagem/bonecopradireita2.png")
                self.rect = self.rect.move(+(self.andando),0)
