from PPlay.window import*
from PPlay.gameimage import* 
from PPlay.sprite import*
from PPlay.gameobject import*
from PPlay.mouse import*
from PPlay.sound import*
import random

def draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao):
    fundo.draw()
    if(teclado.key_pressed("LEFT") or teclado.key_pressed("RIGHT")):
        joy_play.hide()
    for i in range(len(itens_chao)):
        itens_chao[i].draw()
    for i in range(len(obstaculos)):
        obstaculos[i].draw()
    for i in range(len(soldado)):
        if not (soldado[i] == "-1"):
            soldado[i].draw()
    #for i in range(len(soldado_morto)):
        #soldado_morto[i].draw()
    for i in range(len(necessidade_soldados)):
        necessidade_soldados[i].draw()
    for i in range(len(bolsa)):
        bolsa[i].draw()
    escada.draw()
    escada1.draw()
    escada2.draw()
    joy_play.draw()

    for i in range(5):
        if duracao_motivacao/5 * i >= motivacao:
            motiv_interface[2 * i + 1].draw()
        else:
            motiv_interface[2 * i].draw()

