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
