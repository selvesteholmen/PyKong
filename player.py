import pygame as pg
import math
from settings import *
from map import *


class Player:
    def __init__(self, game):
        self.game = game
        self.map = map
        self.x, self.y = PLAYER_POS #Posisjon på kartet
        self.width, self.height = 20, 20
        self.in_air = True
        self.vx, self.vy = 0, 0 #Velositet
        self.is_jumping = False
        self.last_movement_right = True
        self.idle = True
        self.moving_right = False
        self.moving_left = False
        self.can_climb = False
        self.gravity = True
        self.climbing = False
        self.win = False

    #Funskjon som ser om spilleren står stille
    def check_if_idle(self):
        if self.vx == 0:
            self.idle = True

    #Bevegelses funskjon
    def movement(self):
        speed = PLAYER_SPEED * self.game.delta_time #Setter farten ved å bruke farten fra settings, og vi bruker delta_time slik at fpsen ikke endrer på farten.
        jump_power = JUMP_POWER * self.game.delta_time

        keys = pg.key.get_pressed() #Sier at keys er pg.key etc, da slipper jeg å skrive den lange settningen for hver gang.

        #Gå til venstre
        if keys[pg.K_a] and not self.climbing: #Kriterier for å la funksjonen kjøre, dette er for å hindre bevegelser når man klatrer etc
            self.vx -= speed #Endrer på velositeten når man beveger seg
            self.last_movement_right = False #Sier at siste bevegelse ikke var mot høyre (Trenger denne til
            self.moving_right = False #Forteller programmet hvilken vei karakteren går.
            self.moving_left = True
            self.idle = False #Gjør at spilleren ikke lenger går som idle

        #Gå til Høyre
        if keys[pg.K_d] and not self.climbing:
            self.vx += speed
            self.last_movement_right = True
            self.moving_right = True
            self.moving_left = False
            self.idle = False

        #Hoppe
        if keys[pg.K_SPACE] and not self.in_air and not self.is_jumping and not self.climbing:
            self.is_jumping = True
            self.vy -= jump_power + abs(self.vy) * 0.2  #Legger til momentum til velositeten, abs står for absolute, og bruker den absolutte verdien
            self.in_air = True
            self.game.sound.jump.play() #Spiller av lyd som er lagt inn

        #Klatre
        if keys[pg.K_w] and self.can_climb and not self.is_jumping:
            self.climbing = True
            self.gravity = False #Skrur av tygdekraft når man klatrer (Slik at man ikke sklir ned på stigen)
            self.y -= 0.005 #Endrer bare y og ikke velositet (vy) dette er på grunn av at tygdekraft ikke har en effekt når man er på stigen

        #Gå ned på stige
        if keys[pg.K_s] and self.climbing:
            self.y += 0.005

        #Tyngdekraft
        if self.gravity: #Kjører bare når den er skrudd på (true)
            GRAVITY = 0.000001
            self.vy += GRAVITY * self.game.delta_time #Passer på at velositeten går ned over tid.
        else:
            self.vy = 0 #Hvis den er skrudd av (false) så er tygdekraften 0
            GRAVITY = 0

        #oppdaterer posisjonen med bruk av gravitet og velositet
        self.x += self.vx * self.game.delta_time
        self.y += self.vy * self.game.delta_time + 0.5 * GRAVITY * self.game.delta_time ** 2

        #kollisjonsboks så man ikke faller igjennom bakken
        player_rect = pg.Rect(self.x * 100, self.y * 100, self.width, self.height) #Finner spilleren sin boks
        for brick in self.game.map.bricks:
            if player_rect.colliderect(brick.rect): #Ser om man berører en bit av spillkartet
                if self.vy > 0:
                    self.y = brick.rect.top / 100 - self.height / 100
                    self.in_air = False
                    self.is_jumping = False
                    self.gravity = True
                    self.climbing = False
                    self.vy = 0
                    self.vx = 0

                if brick.rect.colliderect(player_rect) and self.vy >= 0 and self.climbing:
                    if self.y + self.height / 100 >= brick.rect.bottom / 100 and self.y + 0.9 * self.height / 100 <= brick.rect.bottom / 100:
                        self.in_air = False
                        self.climbing = False
                        self.vx = 0

        #Plaserer spilleren på bakken når den er på toppen av en stige
        player_rect = pg.Rect(self.x * 100, self.y * 100, self.width, self.height)
        self.can_climb = False
        for ladder in self.game.map_ladders.ladders:
            if player_rect.colliderect(ladder.rect):
                self.can_climb = True
                if self.climbing:
                    self.x = (ladder.rect.left + ladder.rect.width / 2) / 100 - 0.09
        if not self.can_climb:
            self.gravity = True

        #Ser om spilleren er på slutten
        player_rect = pg.Rect(self.x * 100, self.y * 100, self.width, self.height)
        for ladder in self.game.end_game.ladders:
            if player_rect.colliderect(ladder.rect):
                self.win = True

        self.vy += GRAVITY * self.game.delta_time
        self.vx *= FRICTION

    def draw(self):
        pg.draw.rect(self.game.screen, 'red', (self.x * 100, self.y * 100, self.width, self.height))

    def update(self):
        self.check_if_idle()
        self.movement()
