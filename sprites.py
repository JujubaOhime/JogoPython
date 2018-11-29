
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.gameobject import*
from PPlay.sprite import *
from PPlay.collision import *
import random




janela = Window(1079, 555)
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
bolsa = Sprite("imagens/bolsa.png")
primeirossocorros = Sprite("imagens/primeiros-socorros.png")
joydireita.set_total_duration(400)
joyesquerda.set_total_duration(400)
joysubindo.set_total_duration(400)
fogo.set_total_duration(900)
joydireita.set_position(89, 410)
barrada.set_position(349,388)
caixa = Sprite("imagens/caixa.png")
caixa.set_position(803, 247)
escada = Sprite("imagens/escada1.png")
escada.set_position(260, 326)
escada1 = Sprite("imagens/escada1.png")
escada1.set_position(705, 326)
escada2 = Sprite("imagens/escada1.png")
escada2.set_position(955, 326)
soldado = Sprite("imagens/soldado2.png")
soldado.set_position(882, 267)
soldado_morto = Sprite("imagens/soldado-morto.png")
soldado_morto.set_position(515, 120)
joyfrente.set_position(195, 250)
joy_play.set_position(300, 410)
fogo.set_position(12, 407)
joyesquerda.set_position(928, 90)
joysubindo.set_position(257, 371)
chave.set_position(161, 462)
dinamite.set_position(309, 449)
bolsa.set_position(543, 276)
seringa.set_position(763, 454)
primeirossocorros.set_position(799, 454)
granada.set_position(349,296)

joydireita.x = joyesquerda.x = joysubindo.x = joy_play.x
joydireita.y = joyesquerda.y = joysubindo.y = joy_play.y

SpeedX = 300
SpeedY = 200
final_do_mapa = 1079

while True:
    fundo.draw()
    escada.draw()
    escada1.draw()
    escada2.draw()
    chave.draw()
    dinamite.draw()
    seringa.draw()
    bolsa.draw()
    barrada.draw()
    granada.draw()
    fogo.draw()
    fogo.update()
    caixa.draw()
    primeirossocorros.draw()
    soldado.draw()
    soldado_morto.draw()

    #joydireita.draw()
    #joydireita.update()
    #joyesquerda.draw()
    #joyesquerda.update()
    #joysubindo.draw()
    #joysubindo.update()
    #joyfrente.draw()
    
    #range da joy no segundo andar
    if((408 < joy_play.y < 412) or (248 < joy_play.y < 252)):
        if (408 < joy_play.y < 412) and teclado.key_pressed("LEFT") and joy_play.x > 0:
            joy_play.move_x(-SpeedX * janela.delta_time())
            joyesquerda.draw()
            joyesquerda.update()
        elif (248 < joy_play.y < 252) and teclado.key_pressed("LEFT") and joy_play.x > 181:
            joy_play.move_x(-SpeedX * janela.delta_time())
            joyesquerda.draw()
            joyesquerda.update()

        #enfermeira joy vai andar para direita só até o final do mapa
        elif teclado.key_pressed("RIGHT") and joy_play.x < (final_do_mapa - 54):
            joy_play.move_x(SpeedX * janela.delta_time())
            joydireita.draw()
            joydireita.update()

        else:
            joy_play.draw()

    if((260 -15 < joy_play.x < 260 + 15) or (705 - 15 < joy_play.x < 705 + 15) or (955 - 15 < joy_play.x < 955 + 15)):
        if teclado.key_pressed("UP") and joy_play.y > 250:
            joy_play.move_y(-SpeedY * janela.delta_time())
            joysubindo.draw()
            joysubindo.update()
        elif teclado.key_pressed("DOWN") and joy_play.y < 410:
            joy_play.move_y(+SpeedY * janela.delta_time())
            joysubindo.draw()
            joysubindo.update()
        else:
            joysubindo.draw()


    joydireita.x = joyesquerda.x = joysubindo.x = joy_play.x
    joydireita.y = joyesquerda.y = joysubindo.y = joy_play.y

    janela.update()
