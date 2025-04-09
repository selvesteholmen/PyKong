import pygame as pg
import pygame.transform
from settings import *
import os
from collections import deque

#Fungerer likt som barrel_sprite
class spritesetup:
    def __init__(self, game, path='Animation/Player/img0.png'):
        self.right_image = pg.image.load('Animation/Player/img0.png').convert_alpha()
        self.game = game
        self.player = game.player
        self.x, self.y = self.player.x, self.player.y
        self.width, self.height = 20, 20
        self.image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.scale(self.image,(self.player.width, self.player.height))
        self.screen = game.screen

    def get_sprite(self):
        self.dx = self.player.x
        self.dy = self.player.y
        self.width = self.player.width
        self.height = self.player.height

    def update(self):
        self.get_sprite()

    def draw(self):
        self.screen.blit(self.image, (self.dx * 100 - 10, self.dy * 100 - 20))

class animationsetup(spritesetup):
    def __init__(self, game, path='Animation/Player/img0.png',
                 animation_time = 120):
        super().__init__(game, path)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
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
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                img = pg.transform.scale(img,(40, 40))
                images.append(img)
        return images


