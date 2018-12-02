from PPlay.window import*
from PPlay.gameimage import* 
from PPlay.sprite import*
from PPlay.gameobject import*
from PPlay.mouse import*
from PPlay.sound import*
import random

def saber_item_salvar_soldado(soldado, teclado, joy_play, necessidade_soldados_nome, curativos_disponiveis_nome, necessidade_soldados, posicao_y_draw_curativo):
    for i in soldado:
        if teclado.key_pressed('z'):
            if joy_play.collided(i):
                posicao = soldado.index(i)
                print("necessidade_soldados_nome: {}".format(necessidade_soldados_nome[posicao]))
                print("posicao_y_draw_curativo: {}".format(posicao_y_draw_curativo))
                if necessidade_soldados_nome[posicao] == "0":
                    
                    curativo_aleatorio = random.randint(0, len(curativos_disponiveis_nome)-1)
                    if len(necessidade_soldados) == 1:
                            necessidade_soldados.remove(necessidade_soldados[-1])
                            posicao_y_draw_curativo = posicao_y_draw_curativo - 130

                    if curativos_disponiveis_nome[curativo_aleatorio] == "seringa":
                        curativos_disponiveis_nome.remove(curativos_disponiveis_nome[curativo_aleatorio])
                        necessidade_soldados_nome[posicao] = "seringa"
                        curativo_aleatorio = Sprite("imagens/seringa-grande.png")
                        print(curativo_aleatorio.height)
                        print(posicao_y_draw_curativo)
                        curativo_aleatorio.set_position(1170, curativo_aleatorio.height + posicao_y_draw_curativo )
                        necessidade_soldados.append(curativo_aleatorio)
                    elif curativos_disponiveis_nome[curativo_aleatorio] == "primeirossocorros":
                        curativos_disponiveis_nome.remove(curativos_disponiveis_nome[curativo_aleatorio])
                        necessidade_soldados_nome[posicao] = "primeirossocorros"
                        curativo_aleatorio = Sprite("imagens/primeiros-socorros-grande.png")
                        print(curativo_aleatorio.height)
                        print(posicao_y_draw_curativo)
                        curativo_aleatorio.set_position(1170, curativo_aleatorio.height + posicao_y_draw_curativo )
                        necessidade_soldados.append(curativo_aleatorio)
                elif necessidade_soldados_nome[posicao] != '0':
                    if len(necessidade_soldados) == 1:
                        necessidade_soldados.remove(necessidade_soldados[-1])
                        posicao_y_draw_curativo = posicao_y_draw_curativo - 130
                    if necessidade_soldados_nome[posicao] == "seringa":
                        curativo_aleatorio = Sprite("imagens/seringa-grande.png")
                        curativo_aleatorio.set_position(1170, curativo_aleatorio.height + posicao_y_draw_curativo )
                        necessidade_soldados.append(curativo_aleatorio)
                    elif necessidade_soldados_nome[posicao] == "primeirossocorros":
                        curativo_aleatorio = Sprite("imagens/primeiros-socorros-grande.png")
                        curativo_aleatorio.set_position(1170, curativo_aleatorio.height + posicao_y_draw_curativo )
                        necessidade_soldados.append(curativo_aleatorio)
                
                posicao_y_draw_curativo = posicao_y_draw_curativo + 130
                time.sleep(0.2)
    return posicao_y_draw_curativo

def salvamento(teclado, posicao_y_draw_inventario, bolsa, bolsa_nome, soldado,joy_play, itens_chao, itens_nome, necessidade_soldados_nome):
    if teclado.key_pressed('q'):
        passou = 0
        print('entrou')
        if len(bolsa)>=1:
            if bolsa_nome[-1] == "seringa":
                for i in soldado:
                    posicao = soldado.index(i)
                    joyplay1 = Sprite("imagens/joy-frente.png")
                    joyplay1.set_position(joy_play.x+50, joy_play.y)
                    joyplay2 = Sprite("imagens/joy-frente.png")
                    joyplay2.set_position(joy_play.x-50, joy_play.y)
                    if necessidade_soldados_nome[posicao] == "seringa":
                        if joyplay1.collided(i):
                            soldado.remove(i)
                            passou = 1
                        elif joyplay2.collided(i):
                            soldado.remove(i)
                            passou = 1
                if passou == 0:
                    seringa = Sprite("imagens/seringa.png")
                    seringa.set_position(joy_play.x, joy_play.y+joy_play.height-seringa.height)
                    itens_chao.append(seringa)
                    itens_nome.append("seringa")
            if bolsa_nome[-1] == "primeiros_socorros":
                for i in soldado:
                    posicao = soldado.index(i)
                    joyplay1 = Sprite("imagens/joy-frente.png")
                    joyplay1.set_position(joy_play.x+50, joy_play.y)
                    joyplay2 = Sprite("imagens/joy-frente.png")
                    joyplay2.set_position(joy_play.x-50, joy_play.y)
                    if necessidade_soldados_nome[posicao] == "primeirossocorros":
                        if joyplay1.collided(i):
                            soldado.remove(i)
                            passou = 1
                        elif joyplay2.collided(i):
                            soldado.remove(i)
                            passou = 1
                if passou == 0:
                    primeirossocorros = Sprite("imagens/primeiros-socorros.png")
                    primeirossocorros.set_position(joy_play.x, joy_play.y+joy_play.height-primeirossocorros.height)
                    itens_chao.append(primeirossocorros)
                    itens_nome.append("primeiros_socorros")
            bolsa.remove(bolsa[-1])
            bolsa_nome.remove(bolsa_nome[-1])
            posicao_y_draw_inventario = posicao_y_draw_inventario - 130
            print(itens_chao)
            time.sleep(0.12)
    return posicao_y_draw_inventario
