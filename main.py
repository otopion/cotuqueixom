import pygame, random
from pygame.locals import *
from scripts.player import Player
from scripts.item import Item
from scripts.inimigo import Inimigo

#inicializando variaveis
LARGURA = 800
ALTURA = 600

pygame.init()

# tamanho da janela
janela = pygame.display.set_mode((LARGURA,ALTURA))
menu = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Cotuqueixom')

#colocando o fundo do jogo em uma variavel e arrumando a imagem do tamanho da janela
FUNDO = pygame.image.load('imagens/menus/arena.jpg')
FUNDO = pygame.transform.scale(FUNDO, (LARGURA,ALTURA))
MENU = pygame.image.load('imagens/menus/menu/fundo_menu.jpg')
MENU = pygame.transform.scale(MENU, (LARGURA,ALTURA))
PLAY = pygame.image.load('imagens/menus/menu/play.jpg')
GAME_OVER = pygame.image.load('imagens/menus/game_over/game_over.jpg')
VOLTAR = pygame.image.load('imagens/menus/game_over/voltar.jpg')
GANHOU = pygame.image.load('imagens/menus/ganhar/wins.jpg')
VOLTAR_GANHOU = pygame.image.load('imagens/menus/ganhar/voltar_ganhou.jpg')
SAIR_GANHOU = pygame.image.load('imagens/menus/ganhar/sair_ganhou.jpg')
SAIR_MENU = pygame.image.load('imagens/menus/menu/sair_menu.jpg')
SAIR_GAMEOVER = pygame.image.load('imagens/menus/game_over/sair_gameover.jpg')
PLAY2 = pygame.image.load('imagens/menus/menu/2play.jpg')
CREDITOS = pygame.image.load('imagens/menus/menu/creditos.jpg')

#inicializando grupos e instanciando as classes
player_grupo2 = pygame.sprite.Group()
player_grupo1 = pygame.sprite.Group()
player = Player('imagens/players/ferro.png')
player2 = Player('imagens/players/capitao.png')
player_grupo2.add(player2)
player_grupo1.add(player)

item_grupo = pygame.sprite.Group()
item_grupo2 = pygame.sprite.Group()
item = Item('imagens/itens/gameBoy.png')
item2 = Item('imagens/itens/gameBoy2.png')
item_grupo.add(item)
item_grupo2.add(item2)

inimigo_grupo = pygame.sprite.Group()
inimigo = Inimigo('imagens/inimigos/mum.png', 5)
inimigo2 = Inimigo('imagens/inimigos/dragao.png', 3)
inimigo3 = Inimigo('imagens/inimigos/mago.png', 4)
inimigo_grupo.add(inimigo, inimigo2, inimigo3)


#fonte
pygame.font.init()
font_padrao = pygame.font.get_default_font()
pontuacao = pygame.font.SysFont(font_padrao, 45)
pontuacao2 = pygame.font.SysFont(font_padrao, 45)
wins = pygame.font.SysFont(font_padrao, 45)

#inicializando a musica de fundo e efeitos sonoros
musica = pygame.mixer.Sound('sons/musica.ogg')
musica_menu = pygame.mixer.Sound('sons/menu_music.ogg')

efeito_gameOver = pygame.mixer.Sound('sons/efeito_gameOver.ogg')
efeito = pygame.mixer.Sound('sons/efeito_gameboy.ogg')

jogar = False
ganhou = False
perdeu = False
musicaOn = True
jogadores2 = False
player1_wins = False
player2_wins = False

#inicializando a janela
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    #MENU
    while(jogar==False):
        mouse = pygame.mouse.get_pos()

        menu.blit(MENU, (0, 0))
        menu.blit(PLAY, (255, 100))
        menu.blit(PLAY2, (255, 200))
        menu.blit(CREDITOS, (255, 300))
        menu.blit(SAIR_MENU, (255, 400))

        if musicaOn==True:
            musica_menu.play(-1)
            musicaOn = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if(255<mouse[0]<255 + 250 and 100<mouse[1]<100 + 70):
                    jogar = True
                    jogadores2 = False
                    musicaOn = True
                    musica_menu.stop()
                if(255<mouse[0]<255 + 250 and 400<mouse[1]<400 + 70):
                    QUIT()
                if(255<mouse[0]<255 + 250 and 200<mouse[1]<200 + 70):
                    jogadores2 = True
                    jogar = True
                    musicaOn = True
                    musica_menu.stop()


        pygame.display.update()

    #JOGAR
    while(jogar==True):

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        pygame.time.delay(30)

        #musica
        if musicaOn==True:
            musica.play(-1)
            musicaOn = False

        #comandos para movimentar o personagem
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.mover(-2, 0)
        if key[pygame.K_RIGHT]:
            player.mover(2, 0)
        if key[pygame.K_UP]:
            player.mover(0, -2)
        if key[pygame.K_DOWN]:
            player.mover(0, 2)

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            player2.mover(-2, 0)
        if key[pygame.K_d]:
            player2.mover(2, 0)
        if key[pygame.K_w]:
            player2.mover(0, -2)
        if key[pygame.K_s]:
            player2.mover(0, 2)

        #instancia o texto
        text = pontuacao.render("Pontuação: " + str(item.getPontuacao()), 1, (0, 0, 0))

        #coloca o texto e o fundo na tela
        janela.blit(FUNDO, (0, 0))
        janela.blit(text, (20, 20))
        

        player_grupo1.update()
        item_grupo.update()
        inimigo_grupo.update()

        #colocando os objetos na tela
        player_grupo1.draw(janela)
        item_grupo.draw(janela)
        inimigo_grupo.draw(janela)

        #caso clicar em 2 jogadores o segundo jogador e colocado no jogo
        if(jogadores2==True):
            player_grupo2.update()
            player_grupo2.draw(janela)
            item_grupo2.update()
            item_grupo2.draw(janela)

            text2 = pontuacao.render("Pontuação: " + str(item2.getPontuacao()), 1, (0, 0, 0))
            janela.blit(text2, (580, 20))

        #colisão para pegar o item
        if (pygame.sprite.groupcollide(player_grupo1, item_grupo, False, False, pygame.sprite.collide_mask)):
            item.atualiza()
            efeito.play()

        #colisão para pegar o item
        if (pygame.sprite.groupcollide(player_grupo2, item_grupo2, False, False, pygame.sprite.collide_mask)):
            item2.atualiza()
            efeito.play()

        #faz com que tudo reinicie quando o jogo acaba
        def AcabaJogo():

            player.atualiza()
            player2.atualiza()
            item.rec()
            item2.rec()
            inimigo.atualiza()
            inimigo2.atualiza()
            inimigo3.atualiza()
            musica.stop()
            musicaOn = True

        #colisão entre os inimigos
        if (pygame.sprite.groupcollide(player_grupo1, inimigo_grupo, False, False, pygame.sprite.collide_mask)):

            efeito_gameOver.play()

            if(jogadores2==False):
                perdeu = True
            else:
                player2_wins = True

            jogar = False
            AcabaJogo()

        #colisão entre os inimigos
        if (pygame.sprite.groupcollide(player_grupo2, inimigo_grupo, False, False, pygame.sprite.collide_mask)):

            efeito_gameOver.play()
            player1_wins = True
            jogar = False
            AcabaJogo()


        # caso pegue os 20 gameboys ganha o jogo
        if item.getPontuacao() == 20 or item2.getPontuacao() == 20:

            if(item.getPontuacao() == 20 and jogadores2==False):
                ganhou = True;
                    
            if(item.getPontuacao() == 20 and jogadores2==True):
                player1_wins = True;

            if(item2.getPontuacao() == 20 and jogadores2==True):
                player2_wins = True;
                    
            jogar = False
            AcabaJogo()

        pygame.display.update()

    #PAGINA DE GAMEOVER
    while perdeu==True:
        mouse = pygame.mouse.get_pos()
        menu.blit(GAME_OVER, (0, 0))
        menu.blit(VOLTAR, (255, 100))
        menu.blit(SAIR_GAMEOVER, (255, 400))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if(255<mouse[0]<255 + 250 and 100<mouse[1]<100 + 70):
                    perdeu = False
                if(255<mouse[0]<255 + 250 and 400<mouse[1]<400 + 70):
                    QUIT()

        pygame.time.delay(100)


        pygame.display.update()

    #PAGINA DE GANHOU
    while ganhou==True:
        mouse = pygame.mouse.get_pos()
        menu.blit(GANHOU, (0, 0))
        menu.blit(VOLTAR_GANHOU, (255, 300))
        menu.blit(SAIR_GANHOU, (255, 400))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if(255<mouse[0]<255 + 250 and 300<mouse[1]<300 + 70):
                    ganhou = False
                if(255<mouse[0]<255 + 250 and 400<mouse[1]<400 + 70):
                    QUIT()

        pygame.time.delay(100)


        pygame.display.update()

    #PAGINA GANHOU INDIVIDUAL
    while player1_wins==True or player2_wins==True:
        mouse = pygame.mouse.get_pos()
        menu.blit(GANHOU, (0, 0))
        menu.blit(VOLTAR_GANHOU, (255, 300))
        menu.blit(SAIR_GANHOU, (255, 400))

        if(player2_wins==True):
            text = wins.render("PLAYER 2 WINS!", 1, (0, 0, 255))
        else:
            text = wins.render("PLAYER 1 WINS!", 1, (0, 0, 255))

        menu.blit(text, (255, 250))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if(255<mouse[0]<255 + 250 and 300<mouse[1]<300 + 70):
                    player1_wins = False
                    player2_wins = False
                if(255<mouse[0]<255 + 250 and 400<mouse[1]<400 + 70):
                    QUIT()

        pygame.time.delay(100)


        pygame.display.update()


    pygame.display.update()


pygame.quit()
