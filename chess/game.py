from chess_game.chess.constants import (
    config,
)
from chess_game.chess.board import Board
from chess_game.chess.piece import (
    Piece,
)
import pygame
from typing import Union, Optional, Tuple


class Game:
    """
    This class controls the flow of a game. Including saving and loading games.

    Attributes
    ----------
    screen: pygame.Surface
        This is defines the blank board. On which pygame will draw the pieces.
    cfg: str, optional
        This defines the game in which a player wishes to load in. defined by a fen string.

    Methods
    ----------
    reset()
        resets the board to the position given in the config file.
    select(piece, row, col)
        triggers bool on input piece to signify it has been selected.
    move(new_position)
        moves the current selected piece to the input new position.
    draw(mouse_position)
        draws the piece being dragged by the mouse each frame, so piece can be mouse dragged.
    """

    def __init__(
        self,
        screen: Union[pygame.Surface, pygame.SurfaceType],
        cfg: Optional[str] = None,
    ):
        self.piece_grabbed = None
        self.selected_piece = None
        self.screen = screen
        if cfg is None:
            self.cfg = config
        else:
            self.cfg = cfg
        self.board = Board(self.cfg)
        self.board.create_board()

    def _init(self):
        self.selected_piece = None
        self.piece_grabbed = False
        self.board = Board(self.cfg)
        self.board.create_board()

    def reset(self):
        self._init()

    def select(self, piece: Piece, row: int, col: int) -> None:
        """
        triggers bool on input piece to signify it has been selected. And saves the piece in a class attribute.
        Parameters
        ----------
        piece: Piece
            The piece of interest that will become selected.
        row: int
            The current row of the selected piece.
        col: int
            The current col of the selected piece.
        Returns
        -------
        None
        """
        if self.selected_piece is not None:
            if piece == self.selected_piece[0]:
                self.selected_piece = None
                return

        if piece != 0:
            self.selected_piece = piece, row, col
            self.piece_grabbed = True
        return

    def move(self, new_position: Tuple[int, int]) -> None:
        """

        Parameters
        ----------
        new_position: Tuple[int, int]
            The row, col of the position the player wants to move the piece to.

        Returns
        -------
        None
        """

        if self.selected_piece is not None:
            self.piece_grabbed = False

        if (new_position[0] is not None) & (new_position[1] is not None):
            piece, old_row, old_col = self.selected_piece
            new_row, new_col = new_position
            self.board.move(piece, new_row, new_col)
            self.selected_piece = None

        return

    def draw(self, mouse_position: Tuple[int, int]) -> None:
        """

        Parameters
        ----------
        mouse_position: Tuple[int, int]
            The row, col of the position the mouse is hovering over in the current frame.


        Returns
        -------
        None
        """
        if self.piece_grabbed:
            self.board.draw_piece(self.screen, self.selected_piece, mouse_position)
        else:
            self.board.draw_piece(self.screen, self.selected_piece)
        return
