from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blockchain Game")


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
            pygame.draw.line(win, BLACK, (TOOLBAR_WIDTH, i * PIXEL_SIZE),
                             (WIDTH - TOOLBAR_WIDTH, i * PIXEL_SIZE))

        for i in range(6, COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


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
drawing_color = drawing_colors[0]

#Init buttons
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(210, button_y, 50, 50, ORANGE),
    Button(420, button_y, 50, 50, YELLOW),
    Button(630, button_y, 50, 50, GREEN),
    Button(840, button_y, 50, 50, BLUE),
    Button(1080, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(1180, button_y, 50, 50, WHITE, "Clear", BLACK),
    Button(70, 30, 40, 40, ORANGE, "U1", BLACK),
    Button(70, 110, 40, 40, ORANGE, "D1", BLACK),
    Button(30, 70, 40, 40, ORANGE, "L1", BLACK),
    Button(110, 70, 40, 40, ORANGE, "R1", BLACK),
    Button(70, 490, 40, 40, YELLOW, "U2", BLACK),
    Button(70, 570, 40, 40, YELLOW, "D2", BLACK),
    Button(30, 530, 40, 40, YELLOW, "L2", BLACK),
    Button(110, 530, 40, 40, YELLOW, "R2", BLACK),
    Button(1330, 30, 40, 40, GREEN, "U3", BLACK),
    Button(1330, 110, 40, 40, GREEN, "D3", BLACK),
    Button(1290, 70, 40, 40, GREEN, "L3", BLACK),
    Button(1370, 70, 40, 40, GREEN, "R3", BLACK),
    Button(1330, 490, 40, 40, BLUE, "U4", BLACK),
    Button(1330, 570, 40, 40, BLUE, "D4", BLACK),
    Button(1290, 530, 40, 40, BLUE, "L4", BLACK),
    Button(1370, 530, 40, 40, BLUE, "R4", BLACK),
]

# Draw by keyboard
pos_x = 23;
pos_y = 9;
grid[pos_y][pos_x] = drawing_colors[0]

# Setup player P1
P1_pos_x = 6;
P1_pos_y = 0;
grid[P1_pos_y][P1_pos_x] = drawing_colors[1]

# Setup player P2
P2_pos_x = 6;
P2_pos_y = ROWS - 1;
grid[P2_pos_y][P2_pos_x] = drawing_colors[2]

# Setup player P3
P3_pos_x = COLS - 1;
P3_pos_y = 0;
grid[P3_pos_y][P3_pos_x] = drawing_colors[3]

# Setup player P4
P4_pos_x = COLS - 1;
P4_pos_y = ROWS - 1;
grid[P4_pos_y][P4_pos_x] = drawing_colors[4]

#Init 4 players
players = [
    Player(P1_pos_x, P1_pos_y, 1, drawing_colors[1]),
    Player(P2_pos_x, P2_pos_y, 1, drawing_colors[2]),
    Player(P3_pos_x, P3_pos_y, 1, drawing_colors[3]),
    Player(P4_pos_x, P4_pos_y, 1, drawing_colors[4]),
]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Draw by keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and pos_y  + 1 < ROWS:
            pos_y +=  1;
            grid[pos_y][pos_x] = drawing_color
        elif keys[pygame.K_UP] and pos_y > 0:
            pos_y -=  1;
            grid[pos_y][pos_x] = drawing_color
        elif keys[pygame.K_RIGHT] and pos_x + 1 < COLS:
            pos_x +=  1;
            grid[pos_y][pos_x] = drawing_color
        elif keys[pygame.K_LEFT] and pos_x > 6:
            pos_x -=  1;
            grid[pos_y][pos_x] = drawing_color

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                #grid[row][col] = drawing_color
            except IndexError:

                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = drawing_colors[0]

    draw(WIN, grid, buttons)

pygame.quit()
