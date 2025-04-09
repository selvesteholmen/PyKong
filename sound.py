import pygame as pg

#Lyd klasse
class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'Sound' #Path i filene
        self.death = pg.mixer.Sound(self.path + '/Death.wav')
        self.win = pg.mixer.Sound(self.path + '/Win.wav')
        self.jump = pg.mixer.Sound(self.path + '/Jump.wav') #Finner lyden og putter den i mixeren, blir som et soundboard hvor programmet kan spille av lyder som ligger her
        self.theme = pg.mixer.music.load(self.path + '/Song.mp3') #Putter lyden i en spilleliste