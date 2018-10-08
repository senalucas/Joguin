import pygame,sys,os,objetos,char,definicoes,levels.level1,levels.level2, time

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
        #portao.mostrar(tela)

        pygame.display.update()


def jogo():
    pygame.init()

    tela = pygame.display.set_mode([largura,altura])
    pygame.display.set_caption("Maçãs Forever 2.0")
    img = definicoes.Diretorios()
    fundo = img.fundo
    background = pygame.image.load(fundo)
    j = char.Personagem(largura/2,450)

    nivel1 = levels.level1.N1(largura,altura)

    titulo = objetos.Textos("Maçãs Forever 2.0",25,255,255,255)
    pontuacao = objetos.Textos("Pontuação: ",25,255,255,255)
    tempo = objetos.Textos("Tempo: ", 20, 255, 255, 255)

    ff = False
    aux = False
    start = pygame.time.get_ticks()
    time4 = 0
    start2 = pygame.time.get_ticks()
    catch = False

    while True:
        time1 = nivel1.temporizador(start)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.blit(background,(0,0))
        titulo.mostrarTextoNaTela(tela,((largura/3)),10)
        pontuacao.mostrarTextoNaTela(tela,550,560)
        tempo.mostrarTextoNaTela(tela, 655, 2)

        pontos = objetos.Textos(str(nivel1.get_pontuacao()),25,255,255,255)
        pontos.mostrarTextoNaTela(tela,700,560)

        if(aux == False):
            time2 = objetos.Textos(str(time1), 20, 255, 255, 255)
        else:
            time2 = objetos.Textos("20.0", 20, 255, 255, 255)
        time2.mostrarTextoNaTela(tela, 730, 2)

        if(aux == False) and ff == False:
            j.movimentacao(j,nivel1.p1,nivel1.p2,nivel1.p3,nivel1.p4)

        nivel1.mostrarlvl(tela)
        nivel1.mostrarFantasma(tela,j)
        j.mostrar(tela)
        nivel1.movimaca(j,tela)
        vin = False

        perdeu = objetos.Textos("PERDEU",60,255,255,255)

        if nivel1.pegouFantasma2() and catch == False:
            perdeu.mostrarTextoNaTela(tela,(largura/3),altura/2)
            time4 = pygame.time.get_ticks()/1000
            ff = True
            catch = True
            aux = True

        if ff == True:
            perdeu.mostrarTextoNaTela(tela,(largura/3),altura/2)

        if (time1-time4) > 2 and ff == True:
            ff = False
            break

        if nivel1.ganhou(j):
            nivel1.vitoria(tela)
            aux = True
            vin = True

        perdeu = objetos.Textos("TEMPO ESGOTADO!", 60, 255, 255, 255)

        if(time1 > 20 and vin == False):
            perdeu.mostrarTextoNaTela(tela, 100, 260)
            aux = True

        if(time1 >= 21 and aux == True and vin == False):
            aux = False
            break

        if(time1 >= 22 and aux == True and vin == True):
            aux = False
            break


        # # Aqui começa o 2 nível7
        # if(time1 >= 12 and aux == True and vin == True):
        #     nivel1 = 0
        #     aux = False

        #     while True:
        #         print("começou aqui meu brotha")
        #         start1 = pygame.time.get_ticks()

        #         nivel2 = levels.level2.N2(largura,altura)
        #         time1 = nivel2.temporizador(start1)

        #         pontos = objetos.Textos(str(nivel2.get_pontuacao()),25,255,255,255)
        #         pontos.mostrarTextoNaTela(tela,700,560)

        #         if(aux == False):
        #             time2 = objetos.Textos(str(time1), 20, 255, 255, 255)
        #         else:
        #             time2 = objetos.Textos("10.0", 20, 255, 255, 255)
        #         time2.mostrarTextoNaTela(tela, 730, 2)

        #         if(aux == True):
        #             j.movimentacao(j,nivel2.p1,nivel2.p2,nivel2.p3,nivel2.p4)

        #         tela.blit(background,(0,0))
        #         titulo.mostrarTextoNaTela(tela,((largura/3)),10)
        #         pontuacao.mostrarTextoNaTela(tela,550,560)
        #         tempo.mostrarTextoNaTela(tela, 655, 2)
        #         nivel2.mostrarlvl(tela)
        #         j.mostrar(tela)
        #         nivel2.movimaca(j,tela)
        #         print("PASSOU AQUI OH MEU PARÇA")
        #         vin = False

        #         if nivel2.ganhou(j):
        #             nivel2.vitoria(tela)
        #             aux = True
        #             vin = True


        #         perdeu = objetos.Textos("TEMPO ESGOTADO!", 60, 255, 255, 255)
        #         loser = False
        #         if(time1 > 10 and vin == False):
        #             perdeu.mostrarTextoNaTela(tela, 100, 260)
        #             aux = True
        #             loser = True

        #         if(time1 > 12 and aux == True and vin == False):
        #             aux = True
        #             break

        #         print(aux)
        #         print(vin)

        #         if(time1 > 12 and aux == True and vin == True):
        #             aux = False
        #             break

        #         pygame.display.update()

        #     #while termina AQUI
        #     if (aux == True):
        #         break

        pygame.display.update()

menu()
