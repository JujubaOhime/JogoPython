from PPlay.window import*
from PPlay.gameimage import* 
from PPlay.sprite import*
from PPlay.gameobject import*
from PPlay.mouse import*
from PPlay.sound import*
import random

def draw(fundo, itens, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, joy_play, teclado):
    fundo.draw()
    if(teclado.key_pressed("LEFT") or teclado.key_pressed("RIGHT")):
        joy_play.hide()
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