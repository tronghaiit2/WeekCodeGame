from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Program")


def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH - TOOLBAR_HEIGHT, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT))


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = ORANGE

button_x = WIDTH - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(button_x, 10, 50, 50, ORANGE),
    Button(button_x, 70, 50, 50, YELLOW),
    Button(button_x, 130, 50, 50, GREEN),
    Button(button_x, 190, 50, 50, BLUE),
    Button(button_x, 250, 50, 50, WHITE, "Erase", BLACK),
    Button(button_x, 310, 50, 50, WHITE, "Clear", BLACK)
]

pos = (0,0)
pos_x = 0;
pos_y = 0;
grid[pos_y][pos_x] = drawing_color

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and pos_y  + 1< ROWS:
            pos_y +=  1;
            grid[pos_y][pos_x] = drawing_color
        elif keys[pygame.K_UP] and pos_y > 0:
            pos_y -=  1;
            grid[pos_y][pos_x] = drawing_color
        elif keys[pygame.K_RIGHT] and pos_x + 1< COLS:
            pos_x +=  1;
            grid[pos_y][pos_x] = drawing_color
        elif keys[pygame.K_LEFT] and pos_x > 0:
            pos_x -=  1;
            grid[pos_y][pos_x] = drawing_color

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:

                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK

    draw(WIN, grid, buttons)

pygame.quit()
