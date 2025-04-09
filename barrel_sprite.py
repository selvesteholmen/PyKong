import pygame as pg
import pygame.transform
from settings import *
import os
from collections import deque

#Noter, mesteparten av koden er ikke brukt, det er satt opp slik så jeg steg for steg kan få det til å fungere
#Og derfor blir noe kode ikke nødvendig senere.

#Lager ny klasse for å finne bilder
class BarrelSpriteSetup:
    def __init__(self, game, path='Animation/Barrel/img0.png'): #Samme som de andre kodene, bare denne bruker path for å vise hvor i filen man finner bilde.
        self.game = game
        self.x, self.y = 1, 1
        self.width, self.height = 25, 25
        self.image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.screen = game.screen

    def get_sprite(self):
        self.dx = self.x
        self.dy = self.y
        self.width = self.width
        self.height = self.height

    def update(self):
        self.get_sprite()

    def draw(self):
        self.screen.blit(self.image, (self.dx * 100 - 2.5, self.dy * 100 - 5))

class BarrelAnimationSetup(BarrelSpriteSetup):
    def __init__(self, game, path='Animation/Barrel/img0.png',
                 animation_time = 120):
        super().__init__(game, path)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0] # Splitter pathen fra "/" og sier den skal splitte 1 gang. Kort sagt, finner riktig mappe
        self.images = self.get_images(self.path) #Henter bilder fra path.
        self.animation_time_prev = pg.time.get_ticks() #Finner ut hvor lang tid som har gått
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1) #Roterer bildene funnet i mappen
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(os.path.join(path, file_name)).convert_alpha()
                img = pg.transform.scale(img, (25, 25))
                images.append(img)
        return images