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
    nivel1 = levels.level1.N1(largura,altura)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.blit(background,(0,0))

        j.movimentacao()
        nivel1.mostrarlvl(tela)
        j.mostrar(tela)
        pygame.display.update()

jogo()
