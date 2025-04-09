#Importer pakker og informasjon fra andre filer
import pygame as pg
import sys
from settings import *
from player import *
from map import *
from player_sprite import *
from player_animations import *
from map_ladders import *
from sound import *
from barrel import *
from barrel_animations import *
from barrel_ladders import *
from end_ladders import *
from barrel_handler import *
from end_game import *
import os

#Lager en ny klasse, dette er selve spillet.
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES) #Lager nytt vindu som spillet vises på, dette blir da screen
        self.clock = pg.time.Clock() #Lar meg passe på FPS
        self.delta_time = 1 #Ser hvor lang tid som er imellom hvert frame
        self.new_game() #funskjon

    #Definisjon på funksjonen new_game
    def new_game(self):
        self.player = Player(self) #Player(self) er at den skal bruke klassen ifra de andre kodene og ha tilgang til funksjonene dens ved å bruke self.player. Det vil si at for å bruke player sin draw funskjon, så kan man srkive self.player.draw
        self.map = Map(self)
        self.jpeg = pg.image.load('Bilder/map.png') #pg.image.load er en pygame funskjon som lar meg plassere inn et bilde.
        self.win = pg.image.load('Bilder/win.png')
        self.win = pg.transform.scale(self.win, (500, 200))
        self.info = pg.image.load('Bilder/info.png')
        self.info = pg.transform.scale(self.info, (500, 60))
        self.donkey = pg.image.load('Bilder/donkey.png')
        self.donkey = pg.transform.scale(self.donkey, (140, 80))
        self.player_sprite = sprite(self)
        self.map_ladders = Map_Ladders(self)
        self.barrel_ladders = Barrel_Ladders(self)
        self.end_ladders = End_Ladders(self)
        self.sound = Sound(self)
        self.barrel_handler = BarrelHandler(self)
        self.end_game = End_Game(self)

        pg.mixer.music.play(-1) #Spiller av musikk som er lagt til i en spilleliste.

    #Denne funskjonen bare passer på at de forskjellige funskjonene som endrer seg oppdateres så nye posisjoner, gjennstander, og verdier tegnes på nytt.
    def update(self):
        self.player.update()
        self.barrel_handler.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        self.player_sprite.update()
        self.barrel_handler.draw()
        self.player_sprite.draw()
        self.player_win()

    #Denne funskjonen er en samling av alt som tegnes, denne kjører derfor alle draw funksjonene innenfor de forskjellige filene
    def draw(self):
        self.screen.fill('black') #Tegner først svart bakgrunn
        self.screen.blit(self.jpeg, (100, 0)) #Tegner kartet
        self.screen.blit(self.info, (190, 690))
        self.screen.blit(self.donkey, (175, 120))
        #self.map_ladders.draw()        #Blir ikke brukt, kollisjonsboksene til stigene
        #self.player.draw()             #Blir ikke brukt, kollisjonsboksene til spilleren
        self.player_sprite.draw()  # Tegner grafiske spilleren
        self.barrel_handler.draw()  # Tegner grafiske tønnene
        #self.end_game.draw()

    def player_win(self):
        if self.player.win:
            self.screen.blit(self.win, (200, 250))
            pg.display.flip()
            pg.mixer.music.stop()
            self.sound.win.play()
            pg.time.delay(6000)
            pg.quit()

    #Ser om spilleren trykker på escape, eller om spillet sier quit. Hvis det skjer lukker den spillet.
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    #Passer på at disse 3 funskjonene kjører hele tiden
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__': #Passer på at det er main.py som blir startet når man trykker på play
    game = Game()
    game.run()
