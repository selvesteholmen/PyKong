import pygame as pg

class Map:
    def __init__(self, game):
        self.game = game
        self.bricks = [
            Brick(447, 627, 68, 2),#Start på nytt gulv
            Brick(105, 630, 340, 2),
            Brick(515, 624, 68, 2),
            Brick(583, 621, 68, 2),
            Brick(653, 619, 68, 2),
            Brick(721, 616, 68, 2),
            Brick(653, 550, 68, 2),#Start på nytt gulv
            Brick(585, 547, 68, 2),
            Brick(517, 544, 68, 2),
            Brick(449, 541, 68, 2),
            Brick(381, 539, 68, 2),
            Brick(313, 536, 68, 2),
            Brick(245, 533, 68, 2),
            Brick(177, 530, 68, 2),
            Brick(130, 528, 46, 2),
            Brick(175, 465, 68, 2),#Start på nytt gulv
            Brick(243, 462, 68, 2),
            Brick(311, 459, 68, 2),
            Brick(379, 456, 68, 2),
            Brick(447, 453, 68, 2),
            Brick(515, 450, 68, 2),
            Brick(583, 447, 68, 2),
            Brick(651, 444, 68, 2),
            Brick(719, 441, 46, 2),
            Brick(653, 380, 68, 2),  # Start på nytt gulv
            Brick(585, 377, 68, 2),
            Brick(517, 374, 68, 2),
            Brick(449, 371, 68, 2),
            Brick(381, 368, 68, 2),
            Brick(313, 365, 68, 2),
            Brick(245, 362, 68, 2),
            Brick(177, 359, 68, 2),
            Brick(130, 356, 46, 2),
            Brick(175, 295, 68, 2),  # Start på nytt gulv
            Brick(243, 292, 68, 2),
            Brick(311, 289, 68, 2),
            Brick(379, 286, 68, 2),
            Brick(447, 283, 68, 2),
            Brick(515, 280, 68, 2),
            Brick(583, 277, 68, 2),
            Brick(651, 274, 68, 2),
            Brick(719, 271, 46, 2),
            Brick(653, 210, 68, 2),  # Start på nytt gulv
            Brick(585, 207, 68, 2),
            Brick(517, 204, 68, 2),
            Brick(449, 201, 68, 2),
            Brick(129, 199, 320, 2),
        ]

    def draw(self):
        for brick in self.bricks:
            pg.draw.rect(self.game.screen, 'green', brick.rect)

class Brick:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)




