import pygame,sys,os,objetos,char

largura=800
altura=600

def jogo():
    pygame.init()

    tela = pygame.display.set_mode([largura,altura])
    pygame.display.set_caption("Maçãs Forever 2.0")
    background = pygame.image.load("Images/Fundo/fundo.png")

    p1 = objetos.Coisas("Images/Elementos/parede1.png",400,80)
    p2 = objetos.Coisas("Images/Elementos/parede2.png",84,295)
    p3 = objetos.Coisas("Images/Elementos/parede3.png",399,520)
    p4 = objetos.Coisas("Images/Elementos/parede4.png",715,294)

    grupo = pygame.sprite.Group()
    grupo.add(p1)
    grupo.add(p2)
    grupo.add(p3)
    grupo.add(p4)
    p = objetos.Coisas("Images/Elementos/portao1.png",largura/2,520)
    j = char.Personagem(largura/2,altura/2)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        j.movimentacao()

        tela.blit(background,(0,0))
        p1.mostrar(tela)
        p2.mostrar(tela)
        p3.mostrar(tela)
        p4.mostrar(tela)
        p.mostrar(tela)
        j.mostrar(tela)
        pygame.display.update()

jogo()
