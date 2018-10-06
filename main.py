import pygame,sys,os,objetos,char,definicoes,levels.level1

largura=800
altura=600

def menu():
    pygame.init()

    tela = pygame.display.set_mode([largura,altura])
    images = definicoes.Diretorios()        
    pygame.display.set_caption("Maçãs Forever 2.0")
    background = pygame.image.load(images.fundoInicial)
    portao = objetos.Coisas(images.porta1,(largura/2)-15,altura-225)
    t = objetos.Textos("Maçãs Forever 2.0",42,255,255,255)
    iniciar = objetos.Textos("Iniciar",30,255,255,255)  
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for x in range(320,448):
                for y in range(420,451):
                    if ((pygame.mouse.get_pos()[0] == x) and (pygame.mouse.get_pos()[1] == y)):
                        if pygame.mouse.get_pressed()[0]:
                            jogo()                
            

        tela.blit(background,(0,0))
        iniciar.mostrarTextoNaTela(tela,320,420)
        t.mostrarTextoNaTela(tela,((largura/4)),((altura)-altura*0.9))
        portao.mostrar(tela)
        
        pygame.display.update()


def jogo():
    pygame.init()


    tela = pygame.display.set_mode([largura,altura])
    pygame.display.set_caption("Maçãs Forever 2.0")
    img = definicoes.Diretorios()
    fundo = img.fundo
    background = pygame.image.load(fundo)
    j = char.Personagem(largura/2,altura/2)
    nivel1 = levels.level1.N1(largura,altura)
    titulo = objetos.Textos("Maçãs Forever 2.0",25,255,255,255)
    pontuacao = objetos.Textos("Pontuação: ",25,255,255,255)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.blit(background,(0,0))
        titulo.mostrarTextoNaTela(tela,((largura/3)),10)
        pontuacao.mostrarTextoNaTela(tela,550,560)

        pontos = objetos.Textos(str(nivel1.get_pontuacao()),25,255,255,255)
        pontos.mostrarTextoNaTela(tela,700,560)

        j.movimentacao(j,nivel1.p1,nivel1.p2,nivel1.p3,nivel1.p4)
        nivel1.mostrarlvl(tela)
        listam = nivel1.get_maca()
        j.mostrar(tela)
        nivel1.movimaca(j,tela)
        pygame.display.update()

menu()
