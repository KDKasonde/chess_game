from chess_game.chess.constants import (
    WHITE,
    BLACK,
    TILE_SIZE,
)
import os
import pygame

sourceFileDir = os.path.dirname(os.path.abspath('main.py'))
Assets = os.path.join(sourceFileDir, 'chess_game' ,'Assests')


class Piece:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.selected = False
        self.x = 0
        self.y = 0
        self.name = ""
        self.calculate_position()

    def calculate_position(self):
        self.x = TILE_SIZE * self.col
        self.y = TILE_SIZE * self.row

    def __repr__(self):
        if self.colour == WHITE:
            str_colour = "White"
        else:
            str_colour = "Black"
        return str(str_colour + self.name)

    def draw(self, screen, position=None):
        if self.colour == WHITE:
            str_colour = "White"
        else:
            str_colour = "Black"
        piece_image = str_colour+self.name+ '.png'
        location = os.path.join(Assets, piece_image)
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        if position is not None:
            screen.blit(image, (position[0] - TILE_SIZE/2, position[1] - TILE_SIZE/2))
        else:
            screen.blit(image, (self.x, self.y))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()


class King(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
        self.name = "King"


class Queen(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
        self.name = "Queen"


class Rook(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
        self.name = "Rook"


class Knight(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
        self.name = "Knight"


class Bishop(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
        self.name = "Bishop"


class Pawn(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
        self.name = "Pawn"
        if self.colour == WHITE:
            self.direction = 1
        else:
            self.direction = -1


def put_piece(string, row, col):

    if string.isupper():
        colour = BLACK
    else:
        colour = WHITE
    if string.lower() == "b":
        return Bishop(row, col, colour)
    elif string.lower() == "n":
        return Knight(row, col, colour)
    elif string.lower() == "k":
        return King(row, col, colour)
    elif string.lower() == "p":
        return Pawn(row, col, colour)
    elif string.lower() == "q":
        return Queen(row, col, colour)
    else:
        return Rook(row, col, colour)
