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
<<<<<<< HEAD
    titulo = objetos.Textos("Maçãs Forever 2.0",25,255,255,255)
    pontuacao = objetos.Textos("Pontuação: ",25,255,255,255)
=======
>>>>>>> master
    nivel1 = levels.level1.N1(largura,altura)
    grupo = nivel1.get_grupo()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.blit(background,(0,0))
<<<<<<< HEAD
        titulo.mostrarTextoNaTela(tela,((largura/3)),10)
        pontuacao.mostrarTextoNaTela(tela,550,560)
=======
        #print(pygame.sprite.Group.Sprites(grupo))
>>>>>>> master
        j.movimentacao(j,nivel1.p1,nivel1.p2,nivel1.p3,nivel1.p4)
        nivel1.mostrarlvl(tela)
        j.mostrar(tela)
        pygame.display.update()
    
jogo()
