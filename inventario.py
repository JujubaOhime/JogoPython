from PPlay.window import*
from PPlay.gameimage import* 
from PPlay.sprite import*
from PPlay.gameobject import*
from PPlay.mouse import*
from PPlay.sound import*
import random
import time



def remove_item_da_bolsa(bolsa, bolsa_nome, itens_chao, itens_chao_nome, joy_play, posicao_y_draw_inventario, teclado, obstaculos, soldado, necessidade_soldados_nome, necessidade_soldados, posicao_y_draw_curativo, motivacao, duracao_motivacao):
	if teclado.key_pressed('q'):
		passou = 0
		if len(bolsa)>=1:
			if bolsa_nome[-1] == "dinamite":
				dinamite = Sprite("imagens/dinamite.png")
				dinamite.set_position(joy_play.x, joy_play.y+joy_play.height-dinamite.height)
				for i in obstaculos:
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if joyplay1.collided(i):
						obstaculos.remove(i)
						passou = 1
					elif joyplay2.collided(i):
						obstaculos.remove(i)
						passou = 1
				if passou == 0:
					itens_chao.append(dinamite)
					itens_chao_nome.append("dinamite")
			elif bolsa_nome[-1] == "chave":
				chave = Sprite("imagens/chave.png")
				chave.set_position(joy_play.x, joy_play.y+joy_play.height-chave.height)
				itens_chao.append(chave)
				itens_chao_nome.append("chave")
			elif bolsa_nome[-1] == "granada":
				granada = Sprite("imagens/granada.png")
				granada.set_position(joy_play.x, joy_play.y+joy_play.height-granada.height)
				for i in obstaculos:
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if joyplay1.collided(i):
						obstaculos.remove(i)
						passou = 1
					elif joyplay2.collided(i):
						obstaculos.remove(i)
						passou = 1
				if passou == 0:
					itens_chao.append(granada)
					itens_chao_nome.append("granada")
			elif bolsa_nome[-1] == "seringa":
				for i in soldado:
					posicao = soldado.index(i)
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if necessidade_soldados_nome[posicao] == "seringa":
						if joyplay1.collided(i):
							soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							necessidade_soldados_nome.remove(necessidade_soldados_nome[posicao])
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
						elif joyplay2.collided(i):
							soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
				if passou == 0:
					seringa = Sprite("imagens/seringa.png")
					seringa.set_position(joy_play.x, joy_play.y+joy_play.height-seringa.height)
					itens_chao.append(seringa)
					itens_chao_nome.append("seringa")
			elif bolsa_nome[-1] == "atadura":
				for i in soldado:
					posicao = soldado.index(i)
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if necessidade_soldados_nome[posicao] == "atadura":
						if joyplay1.collided(i):
							soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							necessidade_soldados_nome.remove(necessidade_soldados_nome[posicao])
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
						elif joyplay2.collided(i):
							soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
				if passou == 0:
					atadura = Sprite("imagens/atadura.png")
					atadura.set_position(joy_play.x, joy_play.y+joy_play.height-atadura.height)
					itens_chao.append(atadura)
					itens_chao_nome.append("atadura")
			elif bolsa_nome[-1] == "pilula":
				for i in soldado:
					posicao = soldado.index(i)
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if necessidade_soldados_nome[posicao] == "pilula":
						if joyplay1.collided(i):
							soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							necessidade_soldados_nome.remove(necessidade_soldados_nome[posicao])
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
						elif joyplay2.collided(i):
							soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
				if passou == 0:
					pilula = Sprite("imagens/pilula.png")
					pilula.set_position(joy_play.x, joy_play.y+joy_play.height-pilula.height)
					itens_chao.append(pilula)
					itens_chao_nome.append("pilula")
			elif bolsa_nome[-1] == "primeiros_socorros":
				for i in soldado:
					posicao = soldado.index(i)
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if necessidade_soldados_nome[posicao] == "primeirossocorros":
						if joyplay1.collided(i):
							soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							passou = 1
							necessidade_soldados_nome.remove(necessidade_soldados_nome[posicao])
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
						elif joyplay2.collided(i):
							soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
				if passou == 0:
					primeirossocorros = Sprite("imagens/primeiros-socorros.png")
					primeirossocorros.set_position(joy_play.x, joy_play.y+joy_play.height-primeirossocorros.height)
					itens_chao.append(primeirossocorros)
					itens_chao_nome.append("primeiros_socorros")
			bolsa.remove(bolsa[-1])
			bolsa_nome.remove(bolsa_nome[-1])
			posicao_y_draw_inventario = posicao_y_draw_inventario - 130
			time.sleep(0.12)
	return posicao_y_draw_inventario, posicao_y_draw_curativo, motivacao

def adiciona_item_na_bolsa(itens_chao, itens_chao_nome, bolsa, bolsa_nome, joy_play, posicao_y_draw_inventario, teclado, motivacao, duracao_motivacao):
	for i in itens_chao:
		if teclado.key_pressed('SPACE'):
			if joy_play.collided(i):
				posicao = itens_chao.index(i)
				if(itens_chao_nome[posicao] == "primeiros_socorros"):
					if motivacao <= duracao_motivacao*5/6:
						motivacao = motivacao + duracao_motivacao/6
					else:
						motivacao = duracao_motivacao
					primeiros_socorros_grande = Sprite("imagens/primeiros-socorros-grande.png")
					primeiros_socorros_grande.set_position(20, primeiros_socorros_grande.height + posicao_y_draw_inventario )
					bolsa.append(primeiros_socorros_grande)
					bolsa_nome.append("primeiros_socorros")
				if(itens_chao_nome[posicao] == "seringa"):
					if motivacao <= duracao_motivacao*5/6:
						motivacao = motivacao + duracao_motivacao/6
					else:
						motivacao = duracao_motivacao
					seringa_grande = Sprite("imagens/seringa-grande.png")
					seringa_grande.set_position(20, seringa_grande.height + posicao_y_draw_inventario )
					bolsa.append(seringa_grande)
					bolsa_nome.append("seringa")
				if(itens_chao_nome[posicao] == "atadura"):
					if motivacao <= duracao_motivacao*5/6:
						motivacao = motivacao + duracao_motivacao/6
					else:
						motivacao = duracao_motivacao
					atadura_grande = Sprite("imagens/atadura-grande.png")
					atadura_grande.set_position(20, atadura_grande.height + posicao_y_draw_inventario )
					bolsa.append(atadura_grande)
					bolsa_nome.append("atadura")
				if(itens_chao_nome[posicao] == "pilula"):
					if motivacao <= duracao_motivacao*5/6:
						motivacao = motivacao + duracao_motivacao/6
					else:
						motivacao = duracao_motivacao
					pilula_grande = Sprite("imagens/pilula-grande.png")
					pilula_grande.set_position(20, pilula_grande.height + posicao_y_draw_inventario )
					bolsa.append(pilula_grande)
					bolsa_nome.append("pilula")
				if(itens_chao_nome[posicao] == "chave"):
					chave_grande = Sprite("imagens/chave-grande.png")
					chave_grande.set_position(20, chave_grande.height + posicao_y_draw_inventario )
					bolsa.append(chave_grande)
					bolsa_nome.append("chave")
				if(itens_chao_nome[posicao] == "granada"):
					granada_grande = Sprite("imagens/granada-grande.png")
					granada_grande.set_position(20, granada_grande.height + posicao_y_draw_inventario)
					bolsa.append(granada_grande)
					bolsa_nome.append("granada")
				if(itens_chao_nome[posicao] == "dinamite"):
					dinamite_grande = Sprite("imagens/dinamite-grande.png")
					dinamite_grande.set_position(20, dinamite_grande.height + posicao_y_draw_inventario)
					bolsa_nome.append("dinamite")
					bolsa.append(dinamite_grande)
				itens_chao.remove(i)
				itens_chao_nome.remove(itens_chao_nome[posicao])
				posicao_y_draw_inventario = posicao_y_draw_inventario + 130
				break
				time.sleep(0.2)
				posicao_y_draw_inventario = posicao_y_draw_inventario + 130
	return posicao_y_draw_inventario, motivacao

