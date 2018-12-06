from PPlay.window import*
from PPlay.gameimage import* 
from PPlay.sprite import*
from PPlay.gameobject import*
from PPlay.mouse import*
from PPlay.sound import*
from PPlay.keyboard import*
import random
import time
import draw_sprites


def remove_item_da_bolsa(bolsa, bolsa_nome, itens_chao, itens_chao_nome, joy_play, posicao_y_draw_inventario, teclado, obstaculos, soldado, necessidade_soldados_nome, necessidade_soldados, posicao_y_draw_curativo, motivacao, duracao_motivacao, janela, fundo, escada, escada1, escada2, soldado_morto, mochila, motiv_interface):
	if teclado.key_pressed('q'):
		passou = 0
		animacao = 0
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
						explosao_som = Sound("sons/explosao.ogg")
						explosao_som.play()
						explosao_som.set_repeat(False)
						posicaox = i.x 
						posicaoy = i.y
						explosao = Sprite("imagens/explosion.png", 10)
						explosao.set_total_duration(1200)
						explosao.set_position(posicaox, posicaoy);
						tempo_inicio = time.time()
						while(1):
							draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
							explosao.draw()
							explosao.update()
							
							if (time.time() > tempo_inicio + 1):
								break
							janela.update()
						explosao.set_loop(False)
						passou = 1
						animacao = 1
					elif joyplay2.collided(i):
						obstaculos.remove(i)
						explosao_som = Sound("sons/explosao.ogg")
						explosao_som.play()
						explosao_som.set_repeat(False)
						posicaox = i.x 
						posicaoy = i.y
						explosao = Sprite("imagens/explosion.png", 10)
						explosao.set_total_duration(1200)
						explosao.set_position(posicaox, posicaoy);
						tempo_inicio = time.time()
						while(1):
							draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
							explosao.draw()
							explosao.update()
							
							if (time.time() > tempo_inicio + 1):
								break
							janela.update()
						explosao.set_loop(False)
						passou = 1
						animacao = 1
				if passou == 0:
					drop_som = Sound("sons/itens.ogg")
					drop_som.play()
					drop_som.set_repeat(False)
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
						explosao_som = Sound("sons/explosao.ogg")
						explosao_som.play()
						explosao_som.set_repeat(False)
						posicaox = i.x 
						posicaoy = i.y
						explosao = Sprite("imagens/explosion.png", 10)
						explosao.set_total_duration(1200)
						explosao.set_position(posicaox, posicaoy);
						tempo_inicio = time.time()
						while(1):
							draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
							explosao.draw()
							explosao.update()
							
							if (time.time() > tempo_inicio + 1):
								break
							janela.update()
						explosao.set_loop(False)
						passou = 1
						animacao = 1
					elif joyplay2.collided(i):
						obstaculos.remove(i)
						explosao_som = Sound("sons/explosao.ogg")
						explosao_som.play()
						explosao_som.set_repeat(False)
						posicaox = i.x 
						posicaoy = i.y
						explosao = Sprite("imagens/explosion.png", 10)
						explosao.set_total_duration(1200)
						explosao.set_position(posicaox, posicaoy);
						tempo_inicio = time.time()
						while(1):
							draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
							explosao.draw()
							explosao.update()
							
							if (time.time() > tempo_inicio + 1):
								break
							janela.update()
						explosao.set_loop(False)
						passou = 1
						animacao = 1
				if passou == 0:
					drop_som = Sound("sons/itens.ogg")
					drop_som.play()
					drop_som.set_repeat(False)
					itens_chao.append(granada)
					itens_chao_nome.append("granada")
			elif bolsa_nome[-1] == "seringa":
				for i in soldado:
					if i == "-1":
						continue
					posicao = soldado.index(i)
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if necessidade_soldados_nome[posicao] == "seringa":
						if joyplay1.collided(i):
							soldado[posicao] = "-1"
							cura_som = Sound("sons/cura.ogg")
							cura_som.play()
							cura_som.set_repeat(False)
							#soldado.remove(i)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							#necessidade_soldados_nome.remove(necessidade_soldados_nome[posicao])
							necessidade_soldados_nome[posicao] = "0"
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicaox = i.x 
							posicaoy = i.y
							healing = Sprite("imagens/healing.png", 9)
							healing.set_total_duration(1200)
							healing.set_position(posicaox, posicaoy + 20);
							tempo_inicio = time.time()
							while(1):
								draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
								healing.draw()
								healing.update()
								if (time.time() > tempo_inicio + 1):
									break
								janela.update()
							healing.set_loop(False)
							passou = 1
							animacao = 1
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
						elif joyplay2.collided(i):
							#soldado.remove(i)
							soldado[posicao] = "-1"
							cura_som = Sound("sons/cura.ogg")
							cura_som.play()
							cura_som.set_repeat(False)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							passou = 1
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicaox = i.x 
							posicaoy = i.y
							healing = Sprite("imagens/healing.png", 9)
							healing.set_total_duration(1200)
							healing.set_position(posicaox, posicaoy + 20);
							tempo_inicio = time.time()
							while(1):
								draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
								healing.draw()
								healing.update()
								if (time.time() > tempo_inicio + 1):
									break
								janela.update()
							healing.set_loop(False)
							passou = 1
							animacao = 1
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
				if passou == 0:
					drop_som = Sound("sons/itens.ogg")
					drop_som.play()
					drop_som.set_repeat(False)
					seringa = Sprite("imagens/seringa.png")
					seringa.set_position(joy_play.x, joy_play.y+joy_play.height-seringa.height)
					itens_chao.append(seringa)
					itens_chao_nome.append("seringa")
			elif bolsa_nome[-1] == "atadura":
				for i in soldado:
					if i == "-1":
						continue
					posicao = soldado.index(i)
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if necessidade_soldados_nome[posicao] == "atadura":
						if joyplay1.collided(i):
							#soldado.remove(i)
							soldado[posicao] = "-1"
							cura_som = Sound("sons/cura.ogg")
							cura_som.play()
							cura_som.set_repeat(False)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							#necessidade_soldados_nome.remove(necessidade_soldados_nome[posicao])
							necessidade_soldados_nome[posicao] = "0"
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicaox = i.x 
							posicaoy = i.y
							healing = Sprite("imagens/healing.png", 9)
							healing.set_total_duration(1200)
							healing.set_position(posicaox, posicaoy + 20);
							tempo_inicio = time.time()
							while(1):
								draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
								healing.draw()
								healing.update()
								if (time.time() > tempo_inicio + 1):
									break
								janela.update()
							healing.set_loop(False)
							passou = 1
							animacao = 1
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
						elif joyplay2.collided(i):
							soldado[posicao] = "-1"
							#soldado.remove(i)
							cura_som = Sound("sons/cura.ogg")
							cura_som.play()
							cura_som.set_repeat(False)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicaox = i.x 
							posicaoy = i.y
							healing = Sprite("imagens/healing.png", 9)
							healing.set_total_duration(1200)
							healing.set_position(posicaox, posicaoy + 20);
							tempo_inicio = time.time()
							while(1):
								draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
								healing.draw()
								healing.update()
								if (time.time() > tempo_inicio + 1):
									break
								janela.update()
							healing.set_loop(False)
							passou = 1
							animacao = 1
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
				if passou == 0:
					drop_som = Sound("sons/itens.ogg")
					drop_som.play()
					drop_som.set_repeat(False)
					atadura = Sprite("imagens/atadura.png")
					atadura.set_position(joy_play.x, joy_play.y+joy_play.height-atadura.height)
					itens_chao.append(atadura)
					itens_chao_nome.append("atadura")
			elif bolsa_nome[-1] == "pilula":
				for i in soldado:
					if i == "-1":
						continue
					posicao = soldado.index(i)
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if necessidade_soldados_nome[posicao] == "pilula":
						if joyplay1.collided(i):
							#soldado.remove(i)
							soldado[posicao] = "-1"
							cura_som = Sound("sons/cura.ogg")
							cura_som.play()
							cura_som.set_repeat(False)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							#necessidade_soldados_nome.remove(necessidade_soldados_nome[posicao])
							necessidade_soldados_nome[posicao] = "0"
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicaox = i.x 
							posicaoy = i.y
							healing = Sprite("imagens/healing.png", 9)
							healing.set_total_duration(1200)
							healing.set_position(posicaox, posicaoy + 20);
							tempo_inicio = time.time()
							while(1):
								draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
								healing.draw()
								healing.update()
								if (time.time() > tempo_inicio + 1):
									break
								janela.update()
							healing.set_loop(False)
							passou = 1
							animacao = 1
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
						elif joyplay2.collided(i):
							#soldado.remove(i)
							soldado[posicao] = "-1"
							cura_som = Sound("sons/cura.ogg")
							cura_som.play()
							cura_som.set_repeat(False)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + duracao_motivacao/3
							else:
								motivacao = duracao_motivacao
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicaox = i.x 
							posicaoy = i.y
							healing = Sprite("imagens/healing.png", 9)
							healing.set_total_duration(1200)
							healing.set_position(posicaox, posicaoy + 20);
							tempo_inicio = time.time()
							while(1):
								draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
								healing.draw()
								healing.update()
								if (time.time() > tempo_inicio + 1):
									break
								janela.update()
							healing.set_loop(False)
							passou = 1
							animacao = 1
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
				if passou == 0:
					drop_som = Sound("sons/itens.ogg")
					drop_som.play()
					drop_som.set_repeat(False)
					pilula = Sprite("imagens/pilula.png")
					pilula.set_position(joy_play.x, joy_play.y+joy_play.height-pilula.height)
					itens_chao.append(pilula)
					itens_chao_nome.append("pilula")
			elif bolsa_nome[-1] == "primeiros_socorros":
				for i in soldado:
					if i == "-1":
						continue
					posicao = soldado.index(i)
					joyplay1 = Sprite("imagens/joy-frente.png")
					joyplay1.set_position(joy_play.x+50, joy_play.y)
					joyplay2 = Sprite("imagens/joy-frente.png")
					joyplay2.set_position(joy_play.x-50, joy_play.y)
					if necessidade_soldados_nome[posicao] == "primeirossocorros":
						if joyplay1.collided(i):
							#soldado.remove(i)
							soldado[posicao] = "-1"
							cura_som = Sound("sons/cura.ogg")
							cura_som.play()
							cura_som.set_repeat(False)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + (duracao_motivacao * (2/5))
							else:
								motivacao = duracao_motivacao
							#necessidade_soldados_nome.remove(necessidade_soldados_nome[posicao])
							necessidade_soldados_nome[posicao] = "0"
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicaox = i.x 
							posicaoy = i.y
							healing = Sprite("imagens/healing.png", 9)
							healing.set_total_duration(1200)
							healing.set_position(posicaox, posicaoy + 20);
							tempo_inicio = time.time()
							while(1):
								draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
								healing.draw()
								healing.update()
								if (time.time() > tempo_inicio + 1):
									break
								janela.update()
							healing.set_loop(False)
							passou = 1
							animacao = 1
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
						elif joyplay2.collided(i):
							#soldado.remove(i)
							soldado[posicao] = "-1"
							cura_som = Sound("sons/cura.ogg")
							cura_som.play()
							cura_som.set_repeat(False)
							if motivacao <= duracao_motivacao*2/3:
								motivacao = motivacao + (duracao_motivacao * (2/5))
							else:
								motivacao = duracao_motivacao
							if len(necessidade_soldados) == 1:
								necessidade_soldados.remove(necessidade_soldados[-1])
							posicaox = i.x 
							posicaoy = i.y
							healing = Sprite("imagens/healing.png", 9)
							healing.set_total_duration(1200)
							healing.set_position(posicaox, posicaoy + 20);
							tempo_inicio = time.time()
							while(1):
								draw_sprites.draw(fundo, itens_chao, obstaculos, escada, escada1, escada2, soldado, soldado_morto, mochila, necessidade_soldados, joy_play, teclado, bolsa, motiv_interface, motivacao, duracao_motivacao)
								healing.draw()
								healing.update()
								if (time.time() > tempo_inicio + 1):
									break
								janela.update()
							healing.set_loop(False)
							passou = 1
							animacao = 1
							posicao_y_draw_curativo = posicao_y_draw_curativo - 130
				if passou == 0:
					drop_som = Sound("sons/itens.ogg")
					drop_som.play()
					drop_som.set_repeat(False)
					primeirossocorros = Sprite("imagens/primeiros-socorros.png")
					primeirossocorros.set_position(joy_play.x, joy_play.y+joy_play.height-primeirossocorros.height)
					itens_chao.append(primeirossocorros)
					itens_chao_nome.append("primeiros_socorros")
			if animacao == 0:
				tempo_inicio = time.time()
				while(1):
					if (time.time() > tempo_inicio + 0.5):
						break
					janela.update()
			bolsa.remove(bolsa[-1])
			bolsa_nome.remove(bolsa_nome[-1])
			posicao_y_draw_inventario = posicao_y_draw_inventario - 130
		#time.sleep(1)
		#while(1):
			#pygame.time.wait(200)
			#break
	return posicao_y_draw_inventario, posicao_y_draw_curativo, motivacao

def adiciona_item_na_bolsa(itens_chao, itens_chao_nome, bolsa, bolsa_nome, joy_play, posicao_y_draw_inventario, teclado, motivacao, duracao_motivacao):
	for i in itens_chao:
		if teclado.key_pressed('SPACE'):
			if joy_play.collided(i):
				posicao = itens_chao.index(i)
				if(itens_chao_nome[posicao] == "primeiros_socorros"):
#					if motivacao <= duracao_motivacao*5/6:
#						motivacao = motivacao + duracao_motivacao/6
#					else:
#						motivacao = duracao_motivacao
					primeiros_socorros_grande = Sprite("imagens/primeiros-socorros-grande.png")
					primeiros_socorros_grande.set_position(20, primeiros_socorros_grande.height + posicao_y_draw_inventario )
					bolsa.append(primeiros_socorros_grande)
					bolsa_nome.append("primeiros_socorros")
				if(itens_chao_nome[posicao] == "seringa"):
#					if motivacao <= duracao_motivacao*5/6:
#						motivacao = motivacao + duracao_motivacao/6
#					else:
#						motivacao = duracao_motivacao
					seringa_grande = Sprite("imagens/seringa-grande.png")
					seringa_grande.set_position(20, seringa_grande.height + posicao_y_draw_inventario )
					bolsa.append(seringa_grande)
					bolsa_nome.append("seringa")
				if(itens_chao_nome[posicao] == "atadura"):
#					if motivacao <= duracao_motivacao*5/6:
#						motivacao = motivacao + duracao_motivacao/6
#					else:
#						motivacao = duracao_motivacao
					atadura_grande = Sprite("imagens/atadura-grande.png")
					atadura_grande.set_position(20, atadura_grande.height + posicao_y_draw_inventario )
					bolsa.append(atadura_grande)
					bolsa_nome.append("atadura")
				if(itens_chao_nome[posicao] == "pilula"):
#					if motivacao <= duracao_motivacao*5/6:
#						motivacao = motivacao + duracao_motivacao/6
#					else:
#						motivacao = duracao_motivacao
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

