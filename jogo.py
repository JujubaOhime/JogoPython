
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.gameobject import*
from PPlay.sprite import *
from PPlay.collision import *
import random


def jogo():
    obstaculos = []
    itens = []
    itens_nome = []
    bolsa = []
    bolsa_nome = []
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
    soldado = Sprite("imagens/soldado2.png")
    soldado.set_position(882, segundo_nivel-soldado.height)
    soldado_morto = Sprite("imagens/soldado-morto.png")
    soldado_morto.set_position(1092, terceiro_nivel-soldado_morto.height)
    joyfrente.set_position(248, segundo_nivel-soldado.height-joyfrente.height)
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
    obstaculos.append(barrada)
    obstaculos.append(caixa)
    obstaculos.append(fogo)
    itens.append(primeirossocorros)
    itens_nome.append("primeiros_socorros")
    itens.append(seringa)
    itens_nome.append("seringa")
    itens.append(chave)
    itens_nome.append("chave")
    itens.append(granada)
    itens_nome.append("granada")
    itens.append(dinamite)
    itens_nome.append("dinamite")
    print(len(itens))

    joydireita.x = joyesquerda.x = joysubindo.x = joy_play.x
    joydireita.y = joyesquerda.y = joysubindo.y = joy_play.y

    SpeedX = 300
    SpeedY = 200
    final_do_mapa_direita = 1299

    while True:
        fundo.draw()
        if(teclado.key_pressed("LEFT") or teclado.key_pressed("RIGHT")):
            joy_play.hide()
        #for i in range(len(bolsa)):
            
        for i in range(len(itens)):
            itens[i].draw()
        for i in range(len(obstaculos)):
            obstaculos[i].draw()    
        escada.draw()
        escada1.draw()
        escada2.draw()
        soldado.draw()
        soldado_morto.draw()
        mochila.draw()
        joy_play.draw()
        #joydireita.draw()
        #joydireita.update()
        #joyesquerda.draw()
        #joyesquerda.update()
        #joysubindo.draw()
        #joysubindo.update()
        #joyfrente.draw()
        if teclado.key_pressed("ESC"):
            pygame.time.wait(150)
            return
        #range da joy no segundo andar
        if((primeiro_nivel - joy_play.height - 10 < joy_play.y < primeiro_nivel - joy_play.height + 10) or (segundo_nivel -joy_play.height - 10 < joy_play.y < segundo_nivel - joy_play.height + 10)):
            if (primeiro_nivel - joy_play.height - 10 < joy_play.y < primeiro_nivel - joy_play.height + 10) and teclado.key_pressed("LEFT") and joy_play.x > 0:
                joy_play.move_x(-SpeedX * janela.delta_time())
                joyesquerda.draw()
                joyesquerda.update()
                joy_play.hide()
            elif (segundo_nivel -joy_play.height - 10 < joy_play.y < segundo_nivel -joy_play.height + 10) and teclado.key_pressed("LEFT") and joy_play.x >limite_esquerdo_segundo_nivel:
                joy_play.move_x(-SpeedX * janela.delta_time())
                joyesquerda.draw()
                joyesquerda.update()
                joy_play.hide()
            #enfermeira joy vai andar para direita só até o final do mapa
            elif teclado.key_pressed("RIGHT") and joy_play.x < (final_do_mapa_direita - joy_play.width):
                joy_play.move_x(SpeedX * janela.delta_time())
                joy_play.hide()
                joydireita.draw()
                joydireita.update()

            else:
                joy_play.unhide()

        if not(joy_play.x < (final_do_mapa_direita - joy_play.width)):
            joy_play.set_position(final_do_mapa_direita-joy_play.width - 2, joy_play.y)
        if((escada.x -15 < joy_play.x < escada.x + 15) or (escada1.x - 15 < joy_play.x < escada1.x + 15) or (escada2.x - 15 < joy_play.x < escada2.x + 15)):
            if teclado.key_pressed("UP") and joy_play.y > segundo_nivel - joy_play.height:
                joy_play.move_y(-SpeedY * janela.delta_time())
                joysubindo.draw()
                joysubindo.update()
                joy_play.hide()
            elif teclado.key_pressed("DOWN") and joy_play.y < primeiro_nivel-joy_play.height:
                joy_play.move_y(+SpeedY * janela.delta_time())
                joysubindo.draw()
                joysubindo.update()
                joy_play.hide()
            else:
                joy_play.unhide()

        # aqui é a colisão com os obstáculos
        for i in obstaculos:
            x_ant = joy_play.x
            if x_ant <= i.x:
                x_ant = x_ant - 3
            else:
                x_ant = x_ant + 3
            if (joy_play.collided(i)):
                joy_play.set_position(x_ant, joy_play.y)
        i = 0
        for x in itens:
            if joy_play.collided(x):
                if teclado.key_pressed('SPACE'):
                    bolsa.append(x)
                    bolsa_nome.append(itens_nome[i])
                    itens.remove(x)
                    itens_nome.remove(itens_nome[i])
                    print(bolsa)
                    print(bolsa_nome)
            i=+1
        
          
            
        joydireita.x = joyesquerda.x = joysubindo.x = joy_play.x
        joydireita.y = joyesquerda.y = joysubindo.y = joy_play.y
        janela.update()
