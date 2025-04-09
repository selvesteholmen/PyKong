import pygame as pg

class End_Ladders:
    def __init__(self, game):
        self.game = game
        self.ladders = [
            Ladder(660, 270, 5, 5),
            Ladder(229, 357, 5, 5),
            Ladder(343, 362, 5, 5),
            Ladder(660, 442, 5, 5),
            Ladder(456, 450, 5, 5),
            Ladder(230, 525, 5, 5),
            Ladder(411, 535, 5, 5),
            Ladder(660, 615, 5, 5),
        ]

    def draw(self):
        for brick in self.ladders:
            pg.draw.rect(self.game.screen, 'Green', brick.rect)

class Ladder:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)