import pygame as pg #Importerer alt som trengs
from barrel import *
from barrel_animations import *
import time
import random

#Ny klasse for BarrelHandler
class BarrelHandler: #Lager ny klasse
    def __init__(self, game): #ny innit, denne får game
        self.game = game #Gir variablene det de skal være
        self.barrels = [] #Barrels er en liste
        self.last_barrel_time = time.time() #Dette er tid
        self.respawntime = 0 #Respawn time starter som 0 sånn at første tønna kommer med en gang

    #Lager nye tønner
    def create_barrel(self): #Ny funksjon som lager en ny tønne
        new_barrel = barrel(self.game) #Sier at new_barrel er barrel.
        self.barrels.append(new_barrel) #Putter en ny barrel i listen med barrels
        self.respawntime = random.randint(3, 5) #Setter tiden før en ny tønne kan komme

    #Opptaderer informasjon
    def update(self):
        if time.time() - self.last_barrel_time > self.respawntime: #Hvis det har gått så så lang tid
            self.create_barrel() #Så lages en ny tønne
            self.last_barrel_time = time.time() #Og den holder øye med når sist tønne ble lagd

        for barrel in self.barrels: #Oppdaterer alle tønnene i listen.
            barrel.update()

    #Tegner tønnene
    def draw(self):
        for barrel in self.barrels:
            barrel.draw()