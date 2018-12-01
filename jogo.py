
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.gameobject import*
from PPlay.sprite import *
from PPlay.collision import *
import random
import inventario

def jogo():
    obstaculos = []
    itens = []
    itens_nome = []
    bolsa = []
    bolsa_nome = []
    f = 0
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

    joydireita.x = joyesquerda.x = joysubindo.x = joy_play.x
    joydireita.y = joyesquerda.y = joysubindo.y = joy_play.y

    SpeedX = 300
    SpeedY = 200
    final_do_mapa_direita = 1299
    y = 0
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

        #for i in range(len(bolsa)):
        #    if(bolsa_nome[i] == "seringa"):
        #        seringa_grande = Sprite("imagens/seringa-grande.png")
        #        seringa_grande.set_position(17, y)
        #        seringa_grande.draw()
        #        y = y + seringa_grande.height
        #    if(bolsa_nome[i] == "dinamite"):
        #        dinamite_grande = Sprite("imagens/dinamite-grande.png")
        #        dinamite_grande.set_position(17, y)
        #        dinamite.draw()
        #        y = y + dinamite_grande.height
        #    y = y+55 

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

        #só pode subir ou descer se tiver em alguma escada
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

        # adicionando itens na bolsa
        for i in itens:
            if teclado.key_pressed('SPACE'):
                if joy_play.collided(i):
                    posicao = itens.index(i)
                    if(itens_nome[posicao] == "primeiros_socorros"):
                        primeiros_socorros_grande = Sprite("imagens/primeiros-socorros-grande.png")
                        primeiros_socorros_grande.set_position(20, primeiros_socorros_grande.height + y )
                        bolsa.append(primeiros_socorros_grande)
                        bolsa_nome.append("primeiros_socorros")
                    if(itens_nome[posicao] == "seringa"):
                        seringa_grande = Sprite("imagens/seringa-grande.png")
                        seringa_grande.set_position(20, seringa_grande.height + y )
                        bolsa.append(seringa_grande)
                        bolsa_nome.append("seringa")
                    if(itens_nome[posicao] == "chave"):
                        chave_grande = Sprite("imagens/chave-grande.png")
                        chave_grande.set_position(20, chave_grande.height + y )
                        bolsa.append(chave_grande)
                        bolsa_nome.append("chave")
                    if(itens_nome[posicao] == "granada"):
                        granada_grande = Sprite("imagens/granada-grande.png")
                        granada_grande.set_position(20, granada_grande.height + y)
                        bolsa.append(granada_grande)
                        bolsa_nome.append("granada")
                    if(itens_nome[posicao] == "dinamite"):
                        dinamite_grande = Sprite("imagens/dinamite-grande.png")
                        dinamite_grande.set_position(20, dinamite_grande.height + y)
                        bolsa_nome.append("dinamite")
                        bolsa.append(dinamite_grande)
                    itens.remove(i)
                    itens_nome.remove(itens_nome[posicao])
                    print(bolsa)
                    print(bolsa_nome)
                    pygame.time.wait(150)
                    y = y + 130
                    #itens.bolsa_draw(bolsa)
        
        #removendo itens da bolsa
        if teclado.key_pressed('z'):
            f=1
            print(y)
            if len(bolsa)>=1 and f==1:
                if bolsa_nome[-1] == "seringa":
                    seringa = Sprite("imagens/seringa.png")
                    seringa.set_position(joy_play.x, joy_play.y+joy_play.height-seringa.height)
                    itens.append(seringa)
                    itens_nome.append("seringa")
                if bolsa_nome[-1] == "dinamite":
                    dinamite = Sprite("imagens/dinamite.png")
                    dinamite.set_position(joy_play.x, joy_play.y+joy_play.height-dinamite.height)
                    itens.append(dinamite)
                    itens_nome.append("dinamite")
                if bolsa_nome[-1] == "primeiros_socorros":
                    primeirossocorros = Sprite("imagens/primeiros-socorros.png")
                    primeirossocorros.set_position(joy_play.x, joy_play.y+joy_play.height-primeirossocorros.height)
                    itens.append(primeirossocorros)
                    itens_nome.append("primeiros_socorros")
                if bolsa_nome[-1] == "chave":
                    chave = Sprite("imagens/chave.png")
                    chave.set_position(joy_play.x, joy_play.y+joy_play.height-chave.height)
                    itens.append(chave)
                    itens_nome.append("chave")
                if bolsa_nome[-1] == "granada":
                    granada = Sprite("imagens/granada.png")
                    granada.set_position(joy_play.x, joy_play.y+joy_play.height-granada.height)
                    itens.append(granada)
                    itens_nome.append("granada")
                bolsa.remove(bolsa[-1])
                bolsa_nome.remove(bolsa_nome[-1])
                y = y - 130
                print(itens)
                pygame.time.wait(200)
                f = 0
                #print(len(itens))
        #print(len(bolsa))
        inventario.bolsa_draw(bolsa) 

        #imprime os itens da bolsa  
        #for i in range(len(bolsa)):
        #    bolsa[i].draw() 
        
        joydireita.x = joyesquerda.x = joysubindo.x = joy_play.x
        joydireita.y = joyesquerda.y = joysubindo.y = joy_play.y
        janela.update()
