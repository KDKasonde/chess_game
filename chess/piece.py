from chess_game.chess.constants import (
    WHITE,
    BLACK,
    TILE_SIZE,
)
import os
import pygame
from typing import Union, Optional, Tuple, List

sourceFileDir = os.path.dirname(os.path.abspath("main.py"))
Assets = os.path.join(sourceFileDir, "chess_game", "Assests")


class Piece:
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        self.row = row
        self.col = col
        self.colour = colour
        self.selected = False
        self.x = 0
        self.y = 0
        self.name = ""
        self.calculate_position()

    def _sense_check_move(self, row: int, col: int, board: List[List[int]]):
        if (row not in [x for x in range(8)]) or (col not in [x for x in range(8)]):
            return False

        if isinstance(board[row][col], int):
            if board[row][col] != 0:
                return False
        else:
            if board[row][col].colour == self.colour:
                return False

        return True

    @staticmethod
    def _update_en_passant(last_moved_piece):
        if last_moved_piece is None:
            return
        if last_moved_piece.name != "Pawn":
            return
        else:
            last_moved_piece.en_passant = False
        return

    def calculate_position(self):
        self.x = TILE_SIZE * self.col
        self.y = TILE_SIZE * self.row

    def __repr__(self):
        if self.colour == WHITE:
            str_colour = "White"
        else:
            str_colour = "Black"
        return str(str_colour + self.name)

    def draw(
        self,
        screen: Union[pygame.Surface, pygame.SurfaceType],
        position: Optional[Tuple[int, int]] = None,
    ):
        if self.colour == WHITE:
            str_colour = "White"
        else:
            str_colour = "Black"
        piece_image = str_colour + self.name + ".png"
        location = os.path.join(Assets, piece_image)
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
        if position is not None:
            screen.blit(
                image, (position[0] - TILE_SIZE / 2, position[1] - TILE_SIZE / 2)
            )
        else:
            screen.blit(image, (self.x, self.y))

    def move(self, row: int, col: int):
        self.row = row
        self.col = col
        self.calculate_position()

    def is_valid_move(self, row: int, col: int, board: List[List[int]]):

        return True


class King(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "King"
        self.moved = False

    def is_valid_move(
        self, row: int, col: int, board: List[List[int]], last_moved_piece: Piece = None
    ):

        status = self._sense_check_move(row, col, board)
        if not status:
            return False
        if (abs(row - self.row) > 1) or (abs(col - self.col) > 1):
            return False
        self._update_en_passant(last_moved_piece)
        return True

    def is_castle(self, row: int, col: int, board: List[List[int]]):

        if (row not in [x for x in range(8)]) or (col not in [x for x in range(8)]):
            return False
        if (abs(row - self.row) != 0) or (abs(col - self.col) != 2):
            return False
        if col < self.col:
            if (board[row][0].name == "Rook") & (not board[row][0].moved):
                self.moved = True
                return True
        if col > self.col:
            if (board[row][7].name == "Rook") & (not board[row][7].moved):
                self.moved = True
                return True
        return False


class Queen(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Queen"

    def is_valid_move(
        self, row: int, col: int, board: List[List[int]], last_moved_piece: Piece = None
    ):
        status = self._sense_check_move(row, col, board)
        if not status:
            return False
        if (
            (abs(row - self.row) == abs(col - self.col))
            or (abs(row - self.row) == 0)
            or (abs(col - self.col) == 0)
        ):
            self._update_en_passant(last_moved_piece)
            return True


class Rook(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Rook"
        self.moved = False

    def is_valid_move(
        self, row: int, col: int, board: List[List[int]], last_moved_piece: Piece = None
    ):

        status = self._sense_check_move(row, col, board)
        if not status:
            return False
        if (abs(row - self.row) == 0) or (abs(col - self.col) == 0):
            self.moved = True
            self._update_en_passant(last_moved_piece)
            return True
        return False


class Knight(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Knight"

    def is_valid_move(
        self, row: int, col: int, board: List[List[int]], last_moved_piece: Piece = None
    ):

        status = self._sense_check_move(row, col, board)
        if not status:
            return False

        if ((abs(row - self.row) == 1) & (abs(col - self.col) == 2)) or (
            (abs(row - self.row) == 2) & (abs(col - self.col) == 1)
        ):
            self._update_en_passant(last_moved_piece)
            return True


class Bishop(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Bishop"

    def is_valid_move(
        self, row: int, col: int, board: List[List[int]], last_moved_piece: Piece = None
    ):

        status = self._sense_check_move(row, col, board)
        if not status:
            return False
        if abs(row - self.row) == abs(col - self.col):
            self._update_en_passant(last_moved_piece)
            return True


class Pawn(Piece):
    def __init__(self, row: int, col: int, colour: Tuple[int, int, int]):
        super().__init__(row, col, colour)
        self.name = "Pawn"
        self.moved = False
        self.en_passant = False
        if self.colour == WHITE:
            self.direction = 1
        else:
            self.direction = -1

    def _check_en_passant(
        self, row: int, col: int, board: List[List[int]], last_moved_piece: Piece
    ):
        if last_moved_piece.name != "Pawn":
            return False
        if isinstance(board[row][col], int):
            target_pawn_row = row - 1 * self.direction
            opposing_pawn = board[target_pawn_row][col]
            if isinstance(opposing_pawn, int):
                return False
            if opposing_pawn != last_moved_piece:
                return False
            if not opposing_pawn.en_passant:
                return False
            if opposing_pawn.colour != self.colour:
                board[target_pawn_row][col] = 0
                self.moved = True
                return True

    def _check_capture(
        self, row: int, col: int, board: List[List[int]], last_moved_piece: Piece
    ):
        if self._check_en_passant(row, col, board, last_moved_piece):
            return True
        if (self.direction * (row - self.row) == 1) & (
            abs(self.direction * (col - self.col)) == 1
        ):
            if isinstance(board[row][col], int):
                return False
            elif board[row][col].colour == self.colour:
                return False
            else:
                return True

    def is_valid_move(
        self, row: int, col: int, board: List[List[int]], last_moved_piece: Piece
    ):

        status = self._sense_check_move(row, col, board)
        if not status:
            return False

        if (
            (self.direction * (row - self.row) == 2)
            & (self.direction * (col - self.col) == 0)
            & (not self.moved)
        ):
            self.en_passant = True
            self.moved = True
            self._update_en_passant(last_moved_piece)
            return True

        if (self.direction * (row - self.row) == 1) & (
            self.direction * (col - self.col) == 0
        ):
            self.moved = True
            self._update_en_passant(last_moved_piece)
            return True

        if not (
            (self.direction * (row - self.row) == 1)
            & (abs(self.direction * (col - self.col)) == 1)
        ):
            return False

        if self._check_capture(row, col, board, last_moved_piece):
            self._update_en_passant(last_moved_piece)
            return True

        return False


def put_piece(string: str, row: int, col: int):

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
