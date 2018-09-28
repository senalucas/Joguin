import pygame,sys,os,objetos,char,definicoes,levels.level1

largura=800
altura=600

def jogo():
    pygame.init()

    tela = pygame.display.set_mode([largura,altura])
    pygame.display.set_caption("Maçãs Forever 2.0")
    img = definicoes.Diretorios()
    fundo = img.fundo
    background = pygame.image.load(fundo)
    j = char.Personagem(largura/2,altura/2)
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        p1 = objetos.Coisas(img.ps1,400,80)
        p2 = objetos.Coisas(img.ps2,84,295)
        p3 = objetos.Coisas(img.ps3,399,520)
        p4 = objetos.Coisas(img.ps4,715,294)

        grupo = pygame.sprite.Group()
        grupo.add(p1)
        grupo.add(p2)
        grupo.add(p3)
        grupo.add(p4)
        # p = objetos.Coisas(img.ps1,largura/2,520)
        

        j.movimentacao()

        tela.blit(background,(0,0))
        p1.mostrar(tela)
        p2.mostrar(tela)
        p3.mostrar(tela)
        p4.mostrar(tela)
        # p.mostrar(tela)
        j.mostrar(tela)
        pygame.display.update()

jogo()
