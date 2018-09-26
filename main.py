import pygame,sys,os,objetos

largura=800
altura=600

def jogo():
    pygame.init()

    tela = pygame.display.set_mode([largura,altura])
    pygame.display.set_caption("Maçãs Forever 2.0")
    background = pygame.image.load("Images/Fundo/fundo.png")

    caminhoDaFonte = os.path.join("fontes","VCR_OSD_MONO.ttf")
    branco = (255,255,255)
    placar = pygame.font.Font(caminhoDaFonte,25)
    mostrarPlacar = placar.render("Pontuação: ",True,branco)

    p1 = objetos.Parede1()
    p2 = objetos.Parede2()
    p3 = objetos.Parede3()
    p4 = objetos.Parede4()
    p = objetos.Portao()
    j = objetos.Personagem()
    muro = pygame.sprite.Group()
    muro.add(p1)
    muro.add(p2)
    muro.add(p3)
    muro.add(p4)
    jogo = True

    while jogo:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
            clock = pygame.time.get_ticks()
            if keys[pygame.K_w]:
                if clock % 2 == 0:
                    j.Char = pygame.image.load("Images/Personagem/bonecodecostas1.png")
                else:
                    j.Char = pygame.image.load("Images/Personagem/bonecodecostas2.png")
                j.rect = j.rect.move(0,-(j.andando))
            if keys[pygame.K_s]:
                if clock % 2 == 0:
                    j.Char = pygame.image.load("Images/Personagem/bonecodefrente1.png")
                else:
                    j.Char = pygame.image.load("Images/Personagem/bonecodefrente2.png")
                j.rect = j.rect.move(0,+(j.andando))
            if keys[pygame.K_a]:
                if clock % 2 == 0:
                    j.Char = pygame.image.load("Images/Personagem/bonecopraesquerda1.png")
                else:
                    j.Char = pygame.image.load("Images/Personagem/bonecopraesquerda2.png")
                j.rect = j.rect.move(-(j.andando),0)
            if keys[pygame.K_d]:
                if clock % 2 == 0:
                    j.Char = pygame.image.load("Images/Personagem/bonecopradireita1.png")
                else:
                    j.Char = pygame.image.load("Images/Personagem/bonecopradireita2.png")
                j.rect = j.rect.move(+(j.andando),0)

        tela.blit(background,(0,0))
        p1.mostrar(tela)
        p2.mostrar(tela)
        p3.mostrar(tela)
        p4.mostrar(tela)
        p.mostrar(tela)
        j.mostrar(tela)
        pygame.display.update()

jogo()
