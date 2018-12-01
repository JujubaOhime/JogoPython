from PPlay.window import*
from PPlay.gameimage import* 
from PPlay.sprite import*
from PPlay.gameobject import*
from PPlay.mouse import*
from PPlay.sound import*
import random


def bolsa_draw(bolsa):
	for i in range(len(bolsa)):
		bolsa[i].draw()
	return

def remove_itens(bolsa, bolsa_nome, itens, itens_nome, joy_play, posicao_y_draw_inventario, teclado):
	if teclado.key_pressed('z'):
		f = 1
		print(posicao_y_draw_inventario)
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
			posicao_y_draw_inventario = posicao_y_draw_inventario - 130
			print(itens)
			pygame.time.wait(200)
	return posicao_y_draw_inventario

def adicionando_itens(itens, itens_nome, bolsa, bolsa_nome, joy_play, posicao_y_draw_inventario, teclado):
	for i in itens:
		if teclado.key_pressed('SPACE'):
			if joy_play.collided(i):
				posicao = itens.index(i)
				if(itens_nome[posicao] == "primeiros_socorros"):
					primeiros_socorros_grande = Sprite("imagens/primeiros-socorros-grande.png")
					primeiros_socorros_grande.set_position(20, primeiros_socorros_grande.height + posicao_y_draw_inventario )
					bolsa.append(primeiros_socorros_grande)
					bolsa_nome.append("primeiros_socorros")
				if(itens_nome[posicao] == "seringa"):
					seringa_grande = Sprite("imagens/seringa-grande.png")
					seringa_grande.set_position(20, seringa_grande.height + posicao_y_draw_inventario )
					bolsa.append(seringa_grande)
					bolsa_nome.append("seringa")
				if(itens_nome[posicao] == "chave"):
					chave_grande = Sprite("imagens/chave-grande.png")
					chave_grande.set_position(20, chave_grande.height + posicao_y_draw_inventario )
					bolsa.append(chave_grande)
					bolsa_nome.append("chave")
				if(itens_nome[posicao] == "granada"):
					granada_grande = Sprite("imagens/granada-grande.png")
					granada_grande.set_position(20, granada_grande.height + posicao_y_draw_inventario)
					bolsa.append(granada_grande)
					bolsa_nome.append("granada")
				if(itens_nome[posicao] == "dinamite"):
					dinamite_grande = Sprite("imagens/dinamite-grande.png")
					dinamite_grande.set_position(20, dinamite_grande.height + posicao_y_draw_inventario)
					bolsa_nome.append("dinamite")
					bolsa.append(dinamite_grande)
				itens.remove(i)
				itens_nome.remove(itens_nome[posicao])
				print(bolsa)
				print(bolsa_nome)
				posicao_y_draw_inventario = posicao_y_draw_inventario + 130
				break
				pygame.time.wait(150)
				posicao_y_draw_inventario = posicao_y_draw_inventario + 130
	return posicao_y_draw_inventario
			
