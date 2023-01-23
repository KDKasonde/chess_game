# import modules

import pygame
import os
from chess_game import chess

"""
Created on Fri Aug 20 18:06:50 2021

@author: kasonde
"""

"""
Chess game with graphics
"""

# Get file directory

sourceFileDir = os.path.dirname(os.path.abspath('main.py'))
# define the screen, framerate and other
screen = pygame.display.set_mode((chess.WIDTH, chess.HEIGHT))
FRAMERATE = 60
pygame.display.set_caption("Chess")
Assets = os.path.join(sourceFileDir, 'Assests')



# update the window


def draw_window():
    screen.fill(chess.WHITE)

    pygame.display.update()
    return
# place chess piece on board


def place_piece(colour, piece, x, y):
    piece = ChessPiece(colour, piece, x, y)
    return piece

# main game loop


def main():

    clock = pygame.time.Clock()
    run = True
    board = chess.Board()
    draw_window()
    board.draw_squares(screen)
    while run:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        pygame.display.flip()
    pygame.quit()
    

if __name__ == "__main__":
    main()
