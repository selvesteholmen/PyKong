import pygame as pg

#Klasse for å plassere stigene rundt på kartet
class Barrel_Ladders:
    def __init__(self, game):
        self.game = game
        self.ladders = [ #Liste med stigene
            Ladder(671, 190, 5, 20), #Lager en stige, bruker klassen "Ladder" nummerene er størrelse og posisjon.
            Ladder(218, 275, 5, 20),
            Ladder(332, 270, 5, 20),
            Ladder(671, 362, 5, 20),
            Ladder(467, 353, 5, 20),
            Ladder(219, 450, 5, 20),
            Ladder(400, 440, 5, 20),
            Ladder(671, 537, 5, 20),
        ]

    #Tegner alle stigene
    def draw(self):
        for brick in self.ladders:
            pg.draw.rect(self.game.screen, 'White', brick.rect)

#Ny klasse for hva en "Ladder" er
class Ladder:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height) #Sier at det er en rektangel med posisjon og størrelse som kan endres.