import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 93, 86)
YELLOW = (255, 198, 65)
GREEN = (167, 210, 0)
BLUE = (58, 194, 234)

FPS = 240

WIDTH, HEIGHT = 1180, 600

ROWS = 20
COLS = 36

TOOLBAR_HEIGHT = 100

PIXEL_SIZE = 30

BG_COLOR = WHITE

DRAW_GRID_LINES = True


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
