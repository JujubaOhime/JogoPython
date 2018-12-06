from PPlay.window import*
from PPlay.gameimage import* 
from PPlay.sprite import*
from PPlay.gameobject import*
from PPlay.mouse import*
from PPlay.sound import*
import random

def colisao_obstaculos(obstaculos, joy_play):
	for i in obstaculos:
		x_ant = joy_play.x
		if x_ant <= i.x:
			x_ant = x_ant - 3
		else:
			x_ant = x_ant + 3
		if (joy_play.collided(i)):
			joy_play.set_position(x_ant, joy_play.y)

def limite_mapa(primeiro_nivel, segundo_nivel, joy_play, joydireita, joyesquerda, teclado, final_do_mapa_direita, limite_esquerdo_segundo_nivel, SpeedX, janela, terceiro_nivel):
	if((primeiro_nivel - joy_play.height - 10 < joy_play.y < primeiro_nivel - joy_play.height + 10) or (segundo_nivel -joy_play.height - 10 < joy_play.y < segundo_nivel - joy_play.height + 10)) or (terceiro_nivel - joy_play.height - 10 < joy_play.y < terceiro_nivel -joy_play.height + 10):
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
		elif (terceiro_nivel - joy_play.height - 10 < joy_play.y < terceiro_nivel -joy_play.height + 10) and teclado.key_pressed("LEFT") and joy_play.x > 592:
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

def subir_descer_escada(joy_play, joysubindo, primeiro_nivel, segundo_nivel, escada, escada1, escada2, final_do_mapa_direita, teclado, janela, SpeedY, terceiro_nivel):
	if not(joy_play.x < (final_do_mapa_direita - joy_play.width)):
		joy_play.set_position(final_do_mapa_direita-joy_play.width - 2, joy_play.y)
	if((escada.x -15 < joy_play.x < escada.x + 15) or (escada1.x - 15 < joy_play.x < escada1.x + 15)):
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
	elif (escada2.x - 15 < joy_play.x < escada2.x + 15):
		if teclado.key_pressed("UP") and joy_play.y > terceiro_nivel - joy_play.height:
			joy_play.move_y(-SpeedY * janela.delta_time())
			joysubindo.draw()
			joysubindo.update()
			joy_play.hide()
		elif teclado.key_pressed("DOWN") and joy_play.y < segundo_nivel-joy_play.height:
			joy_play.move_y(+SpeedY * janela.delta_time())
			joysubindo.draw()
			joysubindo.update()
			joy_play.hide()
		else:
			joy_play.unhide()
