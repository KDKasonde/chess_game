from chess_game import chess
import pygame


class Board:

    def __init__(self):
        self.selected_piece = None

    def draw_squares(self, screen):
        start_x, start_y = 0, 0
        x, y = start_x, start_y
        for row in range(chess.ROWS):
            for col in range(row % 2, chess.ROWS, 2):
                pygame.draw.rect(
                    screen,
                    chess.BLACK,
                    (
                        (chess.TILE_SIZE * col),
                        (chess.TILE_SIZE * row),
                        chess.TILE_SIZE,
                        chess.TILE_SIZE
                    )
                )


    def create_board(self):
        pass

