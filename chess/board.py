from chess_game.chess.constants import (
    ROWS,
    COLS,
    BLACK,
    WHITE,
    TILE_SIZE,
    config,
    PIECE_DICT,
)
from chess_game.chess.piece import (
    Piece,
    put_piece,
)
import pygame
from typing import Union, Optional, Tuple


class Board:
    def __init__(self, cfg: Optional[str] = None):
        self.selected_piece = None
        self.board = []
        if cfg is None:
            self.cfg = config
        else:
            self.cfg = cfg
        self.create_board()
        self.last_moved_piece = None

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

    def draw_piece(
        self,
        screen: Union[pygame.Surface, pygame.SurfaceType],
        selected_piece: Piece,
        mouse_position: Optional[Tuple[int, int]] = None,
    ):
        self.draw_squares(screen)
        if selected_piece is not None:
            moving_piece, moving_row, moving_col = selected_piece
        else:
            moving_piece, moving_row, moving_col = None, None, None
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]

                if piece != 0:
                    # how to display a still selected piece
                    if (moving_row == row) & (moving_col == col):
                        piece.draw(screen, mouse_position)
                    else:
                        piece.draw(screen)

    def get_piece(self, row: int, col: int):
        return self.board[row][col]

    @staticmethod
    def draw_squares(
        screen: Union[pygame.Surface, pygame.SurfaceType],
    ):
        white = False
        for row in range(ROWS):
            for col in range(COLS):

                pygame.draw.rect(
                    screen,
                    WHITE if white else BLACK,
                    ((TILE_SIZE * col), (TILE_SIZE * row), TILE_SIZE, TILE_SIZE),
                )
                white = not white
            white = not white

    def move(self, piece: Piece, row: int, col: int):

        if piece.name == "King":
            if not piece.moved:
                is_castle = piece.is_castle(row, col, self.board, self.last_moved_piece)
                if is_castle:
                    self._castle(piece, row, col)
                    return

        is_valid = piece.is_valid_move(row, col, self.board, self.last_moved_piece)

        if is_valid:
            self.board[row][col] = 0
            self.board[piece.row][piece.col], self.board[row][col] = (
                self.board[row][col],
                self.board[piece.row][piece.col],
            )
            piece.move(row, col)
            self.last_moved_piece = piece

        return is_valid

    def _castle(self, piece: Piece, row: int, col: int):
        if col < piece.col:
            rook = self.board[piece.row][0]
            self.board[rook.row][rook.col], self.board[row][col + 1] = (
                self.board[row][col + 1],
                self.board[rook.row][rook.col],
            )
            rook.move(row, col + 1)
        if col > piece.col:
            rook = self.board[piece.row][7]
            self.board[rook.row][rook.col], self.board[row][col - 1] = (
                self.board[row][col - 1],
                self.board[rook.row][rook.col],
            )
            rook.move(row, col - 1)

        self.board[piece.row][piece.col], self.board[row][col] = (
            self.board[row][col],
            self.board[piece.row][piece.col],
        )
        piece.move(row, col)

        return

    def draw_valid_moves(self, piece):
        pass

    def _en_passant(self):
        pass
