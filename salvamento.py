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
                    posicao_y_draw_curativo = posicao_y_draw_curativo - 130
                    necessidade_soldados.remove(necessidade_soldados[-1])
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