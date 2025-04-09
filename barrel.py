                            #Importerer alt jeg trenger og informasjon fra andre filer
import pygame as pg
import math
import random
from settings import *
from barrel_sprite import *
from map import *

# Lager en ny klasse
class barrel(BarrelAnimationSetup): #Lager en ny klasse "Objekt" det i parantes er sånn at den skal ta koden ifra den klassen
    def __init__(self, game, path='Animation/Barrel/img0.png', #Definerer altså hva som hører til i denne klassen og hvor den hører til
                 animation_time=130):
        super().__init__(game, path, animation_time)  #En ny __init__ som lar meg styre de forskjellige variablene inni samme klasse
        self.moving_left_images = self.get_images(self.path + '/Left') #Finner fram bildene den skal bruke når den animeres
        self.moving_right_images = self.get_images(self.path + '/Right')
        self.falling_images = self.get_images(self.path + '/Falling')

        self.game = game #Setter verdiene på variablene til det de skal være
        self.map = map
        self.radius = 15
        self.width, self.height = 20, 20
        self.x, self.y = 2.7, 1.8
        self.vx, self.vy = 0, 0
        self.moving_right = True
        self.falling = False
        self.number_received = False
        self.game_over = pg.image.load('Bilder/game_over.png') #Finner game_over bildet.
        self.touched_ladders = set()
        self.dead = False

    #Bestemmer hvordan den skal bevege seg
    def movement(self): #Lager en ny definition som blir brukt til bevegelse

        speed = BARREL_SPEED * self.game.delta_time #Setter farten på tønnene

        #Alt under er for å passe på at tønnen beveger seg rikitg, og vender før den går av kanten.
        if self.x > 7.48 and self.moving_right:
            self.moving_right = False
        if self.x < 1.255 and not self.moving_right:
            self.moving_right = True

        if self.moving_right and not self.falling:
            self.vx += speed
            if self.x > 7.2:
                self.vx -= 0.0006
        if not self.moving_right and not self.falling:
            self.vx -= speed
            if self.x < 1.6:
                self.vx += 0.0006

        #Dette under fjerner tønnen da den er på enden av løypen sin.
        if not self.moving_right and not self.falling:
            if self.x < 1.4 and self.y > 6:
                #self.y = 50
                self.game.barrel_handler.barrels.remove(self)

        if self.dead: #Spiller av game_over skjerm da man treffer en tønne
            self.screen.blit(self.game_over, (200, 225)) #Tegner game_over

        #Passer på at den ikke faller igjennom bakken
        barrel_rect = pg.Rect(self.x * 100, self.y * 100, self.width, self.height) #Finner hitboxen sin
        for brick in self.game.map.bricks: #Hvis den treffer "Brick" altså bakken
            if barrel_rect.colliderect(brick.rect) and not self.falling: #Og den ikke faller
                if self.vy > 0: #Så blir den plassert oppå bakken og ikke har noe y velositet
                    self.y = brick.rect.top / 100 - self.height / 100 #Finner toppen av brikken og plasseren den der.
                    self.vy = 0

        #Alt under gjør detr samme, bare denne finner stiger og får de til å falle ned stigen
        barrel_rect = pg.Rect(self.x * 100, self.y * 100, self.width, self.height)
        for brick in self.game.end_ladders.ladders:
            if barrel_rect.colliderect(brick.rect) and self.falling:
                self.falling = False
                if self.moving_right:
                    self.moving_right = False
                else:
                    self.moving_right = True

        #Denne brukes for å finne ut om tønnen kan falle ned eller ikke, denne biten gir den valget om å falle ned eller ikke, og bruker 1 og 0 som ja og nei
        barrel_rect = pg.Rect(self.x * 100, self.y * 100, self.width, self.height)
        can_roll = not self.touched_ladders
        for ladder in self.game.barrel_ladders.ladders:
            if barrel_rect.colliderect(ladder.rect):
                if ladder not in self.touched_ladders:
                    self.touched_ladders.add(ladder)
                    if can_roll:
                        climb = random.randint(0, 1)
                        if climb == 1:
                            self.vx = 0
                            self.falling = True
                            self.vy += speed / 2

            elif ladder in self.touched_ladders:
                self.touched_ladders.remove(ladder) #Fjerner stigen fra sin egen liste, dette gjør slik at den ikke reagerer på samme stige, men andre tønner kan bruke de

        #Denne fungerer likt, bare nå finner den spiller og tønne for å se om de kolliderer.
        player_rect = pg.Rect(self.game.player.x * 100, self.game.player.y * 100, self.game.player.width,
                              self.game.player.height)
        barrel_rect = pg.Rect(self.x * 100, self.y * 100, self.width, self.height)
        if player_rect.colliderect(barrel_rect): #Denne "Dreper" da karakteren når de røres.
            self.dead = True
            self.screen.blit(pg.image.load('Bilder/game_over.png'), (200, 250))
            pg.display.flip()
            pg.mixer.music.stop()
            self.game.sound.death.play()
            pg.time.delay(5000)
            pg.quit()

        #Dette under passer på at tønnen har riktig fart, tyngdekraft og posisjon.
        self.x += self.vx * self.game.delta_time
        self.y += self.vy * self.game.delta_time + 0.5 * GRAVITY * self.game.delta_time ** 2

        self.vy += GRAVITY * self.game.delta_time
        self.vx *= FRICTION

    #Passer på at alle funksjonene oppdaterer
    def update(self): #Optaterer alle funksjonene så de ikke er fryst og får nye verdier.
        self.movement()
        self.check_animation_time()
        self.get_sprite()
        self.moving()
        self.is_falling()

    #Animasjon
    def moving(self): #Animasjons bruk, altså for å velge bildene som skal bli brukt.
        if self.moving_right and not self.falling:
            self.animate(self.moving_right_images)
        if not self.moving_right and not self.falling:
            self.animate(self.moving_left_images)

    #Velger bilder for da den faller
    def is_falling(self): #Animasjons bruk, altså for å velge bildene som skal bli brukt.
        if self.falling:
            self.animate(self.falling_images)

    #Tegner tønnen på spillbrettet
    def draw(self): #Tegner tønnen på riktig sted.
        #pg.draw.rect(self.game.screen, 'brown', (self.x * 100, self.y * 100, self.width, self.height))
        self.screen.blit(self.image, (self.dx * 100 - 2.5, self.dy * 100 - 5))