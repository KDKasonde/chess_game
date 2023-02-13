# import modules

import pygame
import os
from chess_game.chess import (
    Game,
    Board,
    WIDTH,
    HEIGHT,
    WHITE,
    TILE_SIZE,
    Piece,
)

"""
Created on Fri Aug 20 18:06:50 2021

@author: kasonde
"""

"""
Chess game with graphics
"""

# Get file directory

sourceFileDir = os.path.dirname(os.path.abspath("main.py"))
# define the screen, framerate and other
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FRAMERATE = 60
pygame.display.set_caption("Chess")
Assets = os.path.join(sourceFileDir, "chess_game", "Assests")


def get_square_under_mouse(board: Board):
    x, y = pygame.mouse.get_pos()
    row = y // TILE_SIZE
    col = x // TILE_SIZE
    piece = board.get_piece(row, col)

    return piece, row, col


def draw_drag(board: Board, selected_piece: Piece):
    row, col = None, None
    if selected_piece:
        piece, row, col = get_square_under_mouse(board)

    return row, col


def draw_window():
    screen.fill(WHITE)

    pygame.display.update()
    return


# place chess piece on board


# main game loop


def main():
    clock = pygame.time.Clock()
    run = True
    game = Game(screen)
    draw_window()

    while run:
        clock.tick(FRAMERATE)
        piece, row, col = get_square_under_mouse(game.board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.selected_piece:
                    if game.selected_piece[0] != piece:
                        game.move(drop_position)
                    else:
                        game.piece_grabbed = True
                else:
                    game.select(piece, row, col)

            if event.type == pygame.MOUSEBUTTONUP:
                if game.selected_piece:
                    drop_position = draw_drag(game.board, game.selected_piece)
                    if (drop_position[0] == game.selected_piece[1]) & (
                        drop_position[1] == game.selected_piece[2]
                    ):
                        drop_position = None
                        game.piece_grabbed = False
                    else:
                        game.move(drop_position)
                        drop_position = None

        game.draw(pygame.mouse.get_pos())
        drop_position = draw_drag(game.board, game.selected_piece)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
