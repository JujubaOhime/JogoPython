from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.mouse import *
from PPlay.sound import *

import jogo
import rank
import inventario

def menu():
    janela = Window(1300, 700)
    fundo = GameImage("imagens/safari.png")
    inicio = Sprite("imagens/jogar.png")
    inicio_hover = Sprite("imagens/jogar_h.png")    
    placar = Sprite("imagens/placar.png")   
    placar_hover = Sprite("imagens/placar_h.png")
    dificuldade = Sprite("imagens/dificuldade.png")
    dificuldade_hover = Sprite("imagens/dificuldade_h.png")
    sair = Sprite("imagens/sair.png")
    sair_hover = Sprite("imagens/sair_h.png")
    mouse = janela.get_mouse()
    x = 182
    D = 1
    mouse_timer = time.time()
    score = 0
    
    while True:
        fundo.draw ()
        inicio.draw()
        placar.draw()
        dificuldade.draw()
        inicio.set_position(janela.width / 2 - x, 294)
        placar.set_position(janela.width / 2 - x, 395)
        dificuldade.set_position(janela.width / 2 - x, 496)
        sair.set_position(janela.width / 2 - x, 597)

        inicio_hover.set_position(janela.width / 2 - x, 294)
        placar_hover.set_position(janela.width / 2 - x, 395)
        dificuldade_hover.set_position(janela.width / 2 - x, 496)
        sair_hover.set_position(janela.width / 2 - x, 597)

        if mouse.is_over_object(inicio):
            inicio_hover.draw()
            if mouse.is_button_pressed(1):
                jogo.jogo()
        else:
            inicio.draw()
        if mouse.is_over_object(placar):
            placar_hover.draw()
            if mouse.is_button_pressed(1):
                rank.placar(mouse)
        else:
            placar.draw()
        #if mouse.is_over_object(dificuldade):
        #    dificuldade_hover.draw()
        #    if mouse.is_button_pressed(1):
        #        D = dificuld.dific(mouse)
        #        pygame.time.wait(150)
        #else:
        #    dificuldade.draw()
        if mouse.is_over_object(sair):
            sair_hover.draw()
            if mouse.is_button_pressed(1):
                break
        else:
            sair.draw()

        janela.update()
menu()

