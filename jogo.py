
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.gameobject import*
from PPlay.sprite import *
from PPlay.collision import *
import random
import inventario
import movimento
import draw_sprites
import time
import salvamento

def jogo():
    obstaculos = []
    itens_chao = []
    itens_nome = []
    bolsa = []
    bolsa_nome = []
    f = 0
    soldado = []
    soldado_morto = []
    curativos_no_chao = []
    curativos_disponiveis_nome = []
    curativos_no_chao_nome = []
    necessidade_soldados_nome = []
    necessidade_soldados = []

    motivacao = 20
    duracao_motivacao = motivacao

    primeiro_nivel = 594
    segundo_nivel = 400
    terceiro_nivel = 208
    limite_esquerdo_segundo_nivel = 217
    janela = Window(1300, 700)
    teclado = Window.get_keyboard()
    janela.set_title("Jogaynho")
    fundo = GameImage("imagens/fundo.png")
    joydireita = Sprite("imagens/joy-direita.png", 4)
    joyesquerda = Sprite("imagens/joy-esquerda.png", 4)
    joysubindo = Sprite("imagens/joy-subindo.png", 4)
    joyfrente = Sprite("imagens/joy-frente.png")
    joy_play = Sprite("imagens/joy-frente.png")
    fogo = Sprite("imagens/fogo.png", 9)
    granada = Sprite("imagens/granada.png")
    chave = Sprite("imagens/chave.png")
    dinamite = Sprite("imagens/dinamite.png")
    seringa = Sprite("imagens/seringa.png")
    barrada = Sprite("imagens/barrada1.png")
    mochila = Sprite("imagens/bolsa.png")
    primeirossocorros = Sprite("imagens/primeiros-socorros.png")
    joydireita.set_total_duration(400)
    joyesquerda.set_total_duration(400)
    joysubindo.set_total_duration(400)
    fogo.set_total_duration(900)
    joydireita.set_position(116, primeiro_nivel-joydireita.height)
    barrada.set_position(440,primeiro_nivel-barrada.height)
    caixa = Sprite("imagens/caixa.png")
    caixa.set_position(993, 306)
    escada = Sprite("imagens/escada1.png")
    escada.set_position(322, primeiro_nivel-escada.height)
    escada1 = Sprite("imagens/escada1.png")
    escada1.set_position(884, primeiro_nivel-escada1.height)
    escada2 = Sprite("imagens/escada1.png")
    escada2.set_position(1196, primeiro_nivel-escada2.height)
    soldado1 = Sprite("imagens/soldado2.png")
    soldado1.set_position(882, segundo_nivel-soldado1.height)
    soldado2 = Sprite("imagens/soldado2.png")
    soldado2.set_position(400, segundo_nivel-soldado1.height)
    soldado_morto1 = Sprite("imagens/soldado-morto.png")
    soldado_morto1.set_position(1092, terceiro_nivel-soldado_morto1.height)
    soldado.append(soldado1)
    soldado.append(soldado2)
    soldado_morto.append(soldado_morto1)
    joyfrente.set_position(248, segundo_nivel-soldado1.height-joyfrente.height)
    joy_play.set_position(300, 500)
    fogo.set_position(20, primeiro_nivel-fogo.height)
    joyesquerda.set_position(1168, terceiro_nivel-joyesquerda.height)
    joysubindo.set_position(325, 457)
    chave.set_position(206, primeiro_nivel-chave.height)
    dinamite.set_position(390, primeiro_nivel-dinamite.height)
    mochila.set_position(543, segundo_nivel-mochila.height)
    seringa.set_position(956, primeiro_nivel-seringa.height)
    primeirossocorros.set_position(1001, primeiro_nivel-primeirossocorros.height)
    granada.set_position(438,segundo_nivel-granada.height)
    for i in range(len(soldado)):
        necessidade_soldados_nome.append("0")
    curativos_no_chao.append(seringa)
    curativos_no_chao.append(primeirossocorros)
    curativos_no_chao_nome.append("seringa")
    curativos_no_chao_nome.append("primeirossocorros")
    curativos_disponiveis_nome.append("seringa")
    curativos_disponiveis_nome.append("primeirossocorros")
    obstaculos.append(barrada)
    obstaculos.append(caixa)
    obstaculos.append(fogo)
    itens_chao.append(primeirossocorros)
    itens_nome.append("primeiros_socorros")
    itens_chao.append(seringa)
    itens_nome.append("seringa")
    itens_chao.append(chave)
    itens_nome.append("chave")
    itens_chao.append(granada)
    itens_nome.append("granada")
    itens_chao.append(dinamite)
    itens_nome.append("dinamite")

    joydireita.x = joyesquerda.x = joysubindo.x = joy_play.x
    joydireita.y = joyesquerda.y = joysubindo.y = joy_play.y

    iniSpeedX = 300
    iniSpeedY = 200
    final_do_mapa_direita = 1299
    posicao_y_draw_curativo = -60
    posicao_y_draw_inventario = -60
    tempo_inicial = time.time()
    while True:
        if time.time() >= tempo_inicial + 1:
            tempo_inicial = tempo_inicial + 1
            motivacao = motivacao - 1

        draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa)
        
        SpeedX = iniSpeedX * motivacao/duracao_motivacao
        SpeedY = iniSpeedY * motivacao/duracao_motivacao


        #range da joy no segundo andar
        movimento.limite_mapa(primeiro_nivel, segundo_nivel, joy_play, joydireita, joyesquerda, teclado, final_do_mapa_direita, limite_esquerdo_segundo_nivel, SpeedX, janela)

        #só pode subir ou descer se tiver em alguma escada
        movimento.subir_descer_escada(joy_play, joysubindo, primeiro_nivel, segundo_nivel, escada, escada1, escada2, final_do_mapa_direita, teclado, janela, SpeedY)
        # aqui é a colisão com os obstáculos
        movimento.colisao_obstaculos(obstaculos, joy_play)

        # adicionando itens_chao na bolsa
        posicao_y_draw_inventario = inventario.adiciona_item_na_bolsa(itens_chao, itens_nome, bolsa, bolsa_nome, joy_play, posicao_y_draw_inventario, teclado)

        #removendo itens_chao da bolsa
        
        posicao_y_draw_inventario, posicao_y_draw_curativo = inventario.remove_item_da_bolsa(bolsa, bolsa_nome, itens_chao, itens_nome, joy_play, posicao_y_draw_inventario, teclado, obstaculos, soldado, necessidade_soldados_nome, necessidade_soldados, posicao_y_draw_curativo)

        #print(len(bolsa)) 
        posicao_y_draw_curativo = salvamento.saber_item_salvar_soldado(soldado, teclado, joy_play, necessidade_soldados_nome, curativos_disponiveis_nome, necessidade_soldados, posicao_y_draw_curativo)
        #posicao_y_draw_inventario = salvamento.salvamento(teclado, posicao_y_draw_inventario, bolsa, bolsa_nome, soldado,joy_play, itens_chao, itens_nome, necessidade_soldados_nome)
        joydireita.x = joyesquerda.x = joysubindo.x = joy_play.x
        joydireita.y = joyesquerda.y = joysubindo.y = joy_play.y


        if motivacao <= 0:
            janela.draw_text("A guerra ganhou dessa vez", 0, 0, 36, (255, 255, 0))
            janela.update()
            pygame.time.wait(4000)
            return


        if teclado.key_pressed("ESC"):
            pygame.time.wait(150)
            return
            
        janela.update()
