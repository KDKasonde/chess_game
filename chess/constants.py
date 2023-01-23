# size of display
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
# some colours I will use
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# define some functions and classes for the game loop

TILE_SIZE = 100
#define FEN starting postion
config = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
PIECE_DICT = {
        'b': 'black-bishop',
        'B': 'white-bishop',
        'k': 'black-king',
        'K': 'white-king',
        'n': 'black-knight',
        'N': 'white-knight',
        'p': 'black-pawn',
        'P': 'white-pawn',
        'q': 'black-queen',
        'Q': 'white-queen',
        'r': 'black-rook',
        'R': 'white-rook'
    }
