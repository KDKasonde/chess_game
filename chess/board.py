from chess_game.chess.constants import (
    ROWS,
    COLS,
    BLACK,
    WHITE,
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

    def get_piece(self, row, col):
        return self.board[row][col]

    def draw_squares(self, screen):
        black = False
        for row in range(ROWS):
            for col in range(COLS):
                print(row,  col, black)

                pygame.draw.rect(
                    screen,
                    BLACK if black else WHITE,
                    (
                        (TILE_SIZE * col),
                        (TILE_SIZE * row),
                        TILE_SIZE,
                        TILE_SIZE
                    )
                )
                black = not black
            black = not black

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        return
