import pygame, sys
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (123, 123, 123)
ORANGE = (255, 93, 86)
YELLOW = (255, 198, 65)
GREEN = (167, 210, 0)
BLUE = (58, 194, 234)

ORANGE_HEAD = (186, 0, 0)
YELLOW_HEAD = (210, 152, 18)
GREEN_HEAD = (70, 158, 0)
BLUE_HEAD = (22, 94, 239)

FPS = 240

WIDTH, HEIGHT = 1440, 700

ROWS = 20
COLS = 36

TOOLBAR_HEIGHT = 100
TOOLBAR_WIDTH = 180

PIXEL_SIZE = 30

BG_COLOR = WHITE

DRAW_GRID_LINES = True

timeDefault = 500
countdown = 3

# Setup drawing color
drawing_colors = [GRAY, ORANGE, YELLOW, GREEN, BLUE]
drawing_colors_head = [GRAY,ORANGE_HEAD, YELLOW_HEAD, GREEN_HEAD, BLUE_HEAD]
def get_font(size):
    return pygame.font.SysFont("comicsans", size)
