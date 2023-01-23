from chess_game.chess import (
    WHITE,
    TILE_SIZE,
)
import os
import pygame

sourceFileDir = os.path.dirname(os.path.abspath('main.py'))
Assets = os.path.join(sourceFileDir, 'Assests')


class Piece:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.selected = False
        self.x = 0
        self.y = 0
        self.name = ""

    def calculate_position(self):
        self.x = TILE_SIZE * self.col
        self.y = TILE_SIZE * self.row

    def __repr__(self):
        return str(self.colour + self.name)


class King(Piece):
    def __init__(self):
        self.name = "king"

    def draw(self, screen):
        location = os.path.join(Assets, self.colour + "king" + '.png')
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        screen.blit(image, (self.x, self.y))


class Queen(Piece):
    def __init__(self):
        self.name = "queen"

    def draw(self, screen):
        location = os.path.join(Assets, self.colour + "queen" + '.png')
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        screen.blit(image, (self.x, self.y))


class Rook(Piece):
    def __init__(self):
        self.name = "rook"

    def draw(self, screen):
        location = os.path.join(Assets, self.colour + "rook" + '.png')
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        screen.blit(image, (self.x, self.y))


class Knight(Piece):
    def __init__(self):
        self.name = "knight"

    def draw(self, screen):
        location = os.path.join(Assets, self.colour + "knight" + '.png')
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        screen.blit(image, (self.x, self.y))


class Bishop(Piece):
    def __init__(self):
        self.name = "bishop"

    def draw(self, screen):
        location = os.path.join(Assets, self.colour + "bishop" + '.png')
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        screen.blit(image, (self.x, self.y))


class Pawn(Piece):
    def __init__(self):
        self.name = "pawn"
        if self.colour == WHITE:
            self.direction = 1
        else:
            self.direction = -1

    def draw(self, screen):
        location = os.path.join(Assets, self.colour + "pawn" + '.png')
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        screen.blit(image, (self.x, self.y))