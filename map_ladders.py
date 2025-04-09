import pygame as pg

class Map_Ladders:
    def __init__(self, game):
        self.game = game
        self.ladders = [
            Ladder(660, 557, 5, 50),
            Ladder(411, 460, 5, 75),
            Ladder(230, 470, 5, 50),
            Ladder(456, 373, 5, 75),
            Ladder(660, 382, 5, 55),
            Ladder(343, 295, 5, 55),
            Ladder(229, 297, 5, 55),
            Ladder(660, 212, 5, 55),
            Ladder(502, 135, 5, 55),
        ]

    def draw(self):
        for brick in self.ladders:
            pg.draw.rect(self.game.screen, 'cyan', brick.rect)

class Ladder:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)