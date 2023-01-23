from chess_game.chess.constants import (
    ROWS,
    COLS,
    BLACK,
    TILE_SIZE,
    config,
    PIECE_DICT
)
from chess_game.chess.piece import (
    put_piece
)
import pygame


class Board:

    def __init__(self, cfg = None):
        self.selected_piece = None
        self.board = []
        if cfg is None:
            self.cfg = config
        else:
            self.cfg = cfg
        self.create_board()

    def create_board(self):
        row, col = 0, 0
        self.board.append([])
        for string in self.cfg:
            if string in PIECE_DICT.keys():
                print('( ' + string + " , "+ str(row) + " , "+ str(col) )
                self.board[row].append(put_piece(string, row, col))
                col += 1
            elif string == "/":
                self.board.append([])
                row += 1
                col = 0
            else:
                for i in range(int(string)):
                    self.board[row].append(0)
                    col += 1

    def draw(self, screen):
        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]

                if piece != 0:
                    piece.draw(screen)

    def draw_squares(self, screen):
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (
                        (TILE_SIZE * col),
                        (TILE_SIZE * row),
                        TILE_SIZE,
                        TILE_SIZE
                    )
                )

    def move(self, piece, row, col):
        pass
