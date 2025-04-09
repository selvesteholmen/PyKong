import pygame as pg

class End_Game:
    def __init__(self, game):
        self.game = game
        self.ladders = [
            Ladder(502, 115, 5, 5),
        ]

    def draw(self):
        for brick in self.ladders:
            pg.draw.rect(self.game.screen, 'Blue', brick.rect)

class Ladder:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)