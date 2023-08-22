from chess_game.chess.constants import config, WHITE, BLACK, GREY, YELLOW
from chess_game.chess.board import Board
from chess_game.chess.piece import (
    Piece,
)
import pygame
from typing import Union, Optional, Tuple
import os


sourceFileDir = os.path.dirname(os.path.abspath("main.py"))
Assets = os.path.join(sourceFileDir, "chess_game", "Assests")


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

    TILE_SIZE = 200
    OFFSET = 200

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
        self.board = Board(self.cfg["current_board"])
        self.active_player = self.cfg["active_player"]
        self.board.create_board()
        self.promotion_target = None

    def _init(self) -> None:
        """
        private method for resetting the game board
        Returns
        -------
            None
        """
        self.selected_piece = None
        self.piece_grabbed = False
        self.board = Board(self.cfg["current_board"])
        self.active_player = self.cfg["active_player"]
        self.board.create_board()
        return

    def _switch_player(self) -> None:
        """
        Private method to switch the games active player
        Returns
        -------
            None
        """
        if self.active_player == "white":
            self.active_player = "black"
        else:
            self.active_player = "white"
        return

    def _get_str_colour(self) -> str:
        """
        Private method for retrieving the colour given an rgb representation/
        Returns
        -------
            None
        """
        colour = self.selected_piece[0].colour
        if colour == WHITE:
            return "white"
        elif colour == BLACK:
            return "black"
        else:
            raise ValueError

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
        This method takes the current piece instance and checks whether it is a valid move,
        calling the board object move method to actually move the piece and switching players
        if successful.
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

        if new_position[0] is None:
            self.selected_piece = None
            return

        if new_position[1] is None:
            self.selected_piece = None
            return

        colour = self._get_str_colour()
        if colour != self.active_player:
            self.selected_piece = None
            return

        piece, old_row, old_col = self.selected_piece
        new_row, new_col = new_position
        is_valid_move, pawn_promotion = self.board.move(piece, new_row, new_col)
        self.selected_piece = None
        if pawn_promotion and is_valid_move:
            self._promotion_screen(piece, new_row, new_col)
            return
        if is_valid_move:
            self._switch_player()

        return

    def _promotion_screen(self, piece: Piece, new_row: int, new_col: int) -> None:
        """
        This sets the promotion target in the game so that it can start the promotion
        screen.
        Parameters
        ----------
        piece: Piece
            The piece that needs promoting.
        new_row: int
            The row it has moved to (0 or 7) in all cases.
        new_col: int
            The column the piece is now on.

        Returns
        -------
            None
        """
        self.promotion_target = {
            "piece": piece,
            "row": new_row,
            "col": new_col,
        }

        return

    def draw_promotion_window(self):
        """
        This method draws the screen that gives the current player piece options for
        promoting a pass pawn.
        Returns
        -------
            None
        """
        pygame.draw.rect(
            self.screen,
            GREY,
            (0, self.TILE_SIZE, self.TILE_SIZE * 4, self.TILE_SIZE * 2),
        )
        for index, piece in enumerate(["Queen", "Rook", "Bishop", "Knight"]):
            str_colour = "White" if self.active_player == "white" else "Black"
            piece_image = str_colour + piece + ".png"
            location = os.path.join(Assets, piece_image)
            image = pygame.image.load(location).convert_alpha()
            image = pygame.transform.scale(image, (self.TILE_SIZE, self.TILE_SIZE))
            self.screen.blit(image, (self.TILE_SIZE * index, self.TILE_SIZE * 1.5))
        return

    def _draw_focus(self, piece: str, x: int, y: int) -> None:
        """
        Method used to draw the piece the use is currently hovering over,
        to highlight what will be selected.
        Parameters
        ----------
        piece: str
            This is the name of the piece the user is hovering over.
        x: int
            The x axis location of that piece on the window.
        y: int
            The y axis location of the piece being hovered over.

        Returns
        -------
            None
        """
        str_colour = "White" if self.active_player == "white" else "Black"
        piece_image = str_colour + piece + ".png"
        location = os.path.join(Assets, piece_image)
        image = pygame.image.load(location).convert_alpha()
        image = pygame.transform.scale(image, (self.TILE_SIZE, self.TILE_SIZE))
        pygame.draw.rect(
            self.screen,
            YELLOW,
            (x, y, self.TILE_SIZE, self.TILE_SIZE),
        )
        self.screen.blit(image, (x, y))
        return

    def check_promotion_window(self) -> None:
        """
        Method to check whether a user is hovering over the promotion options.
        Returns
        -------
            None
        """
        x, y = pygame.mouse.get_pos()
        options = {
            "Queen": [(0, 200), (300, 500)],
            "Rook": [(200, 400), (300, 500)],
            "Bishop": [(400, 600), (300, 500)],
            "Knight": [(600, 800), (300, 500)],
        }

        for element in options.keys():
            col_coords = options[element][0]
            row_coords = options[element][1]
            if (col_coords[0] <= x <= col_coords[1]) and (
                row_coords[0] <= y <= row_coords[1]
            ):
                self._draw_focus(piece=element, x=col_coords[0], y=row_coords[0])
        return

    def draw(self, mouse_position: Tuple[int, int]) -> None:
        """
        This method draws the board screen.
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
        if self.promotion_target is not None:
            self.draw_promotion_window()
            self.check_promotion_window()
        return
