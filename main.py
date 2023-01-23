# import modules

import pygame
import os
from chess_game.chess import (
    Board,
    WIDTH,
    HEIGHT,
    WHITE,
)

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
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FRAMERATE = 60
pygame.display.set_caption("Chess")
Assets = os.path.join(sourceFileDir, 'Assests')



# update the window


def draw_window():
    screen.fill(WHITE)

    pygame.display.update()
    return
# place chess piece on board


# main game loop


def main():

    clock = pygame.time.Clock()
    run = True
    board = Board()
    draw_window()
    board.draw(screen)
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
