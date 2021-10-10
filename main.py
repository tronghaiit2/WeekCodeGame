from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blockchain Game")


def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, ((j+6) * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (TOOLBAR_WIDTH, i * PIXEL_SIZE),
                             (WIDTH - TOOLBAR_WIDTH, i * PIXEL_SIZE))

        for i in range(6, COLS + 7):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

    pygame.display.update()

def draw_buttons(win, buttons):
    win.fill(BG_COLOR)
    for button in buttons:
        button.draw(win)

    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos

    if x < 180 or x > 1260:
        raise IndexError
    if y < 0 or y > 600:
        raise IndexError

    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

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

# Setup player P1
P1_pos_x = 0;
P1_pos_y = 0;
grid[P1_pos_y][P1_pos_x] = drawing_colors[1]

# Setup player P2
P2_pos_x = 0;
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
draw_buttons(WIN, buttons)

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Draw by keyboard
        keys = pygame.key.get_pressed()

        #P1
        if keys[pygame.K_s] and P1_pos_y + 1 < ROWS:
            P1_pos_y +=  1;
#            for i in range(5):
#                if(grid[P1_pos_y][P1_pos_x] == drawing_colors[i]) count[i] -= 1
            grid[P1_pos_y][P1_pos_x] = drawing_colors[1]
        elif keys[pygame.K_w] and P1_pos_y > 0:
            P1_pos_y -=  1;
            grid[P1_pos_y][P1_pos_x] = drawing_colors[1]
        elif keys[pygame.K_d] and P1_pos_x + 1 < COLS:
            P1_pos_x +=  1;
            grid[P1_pos_y][P1_pos_x] = drawing_colors[1]
        elif keys[pygame.K_a] and P1_pos_x > 0:
            P1_pos_x -=  1;
            grid[P1_pos_y][P1_pos_x] = drawing_colors[1]

        #P2
        if keys[pygame.K_g] and P2_pos_y + 1 < ROWS:
            P2_pos_y +=  1;
            grid[P2_pos_y][P2_pos_x] = drawing_colors[2]
        elif keys[pygame.K_t] and P2_pos_y > 0:
            P2_pos_y -=  1;
            grid[P2_pos_y][P2_pos_x] = drawing_colors[2]
        elif keys[pygame.K_h] and P2_pos_x + 1 < COLS:
            P2_pos_x +=  1;
            grid[P2_pos_y][P2_pos_x] = drawing_colors[2]
        elif keys[pygame.K_f] and P2_pos_x > 0:
            P2_pos_x -=  1;
            grid[P2_pos_y][P2_pos_x] = drawing_colors[2]

        #P3
        if keys[pygame.K_k] and P3_pos_y + 1 < ROWS:
            P3_pos_y +=  1;
            grid[P3_pos_y][P3_pos_x] = drawing_colors[3]
        elif keys[pygame.K_i] and P3_pos_y > 0:
            P3_pos_y -=  1;
            grid[P3_pos_y][P3_pos_x] = drawing_colors[3]
        elif keys[pygame.K_l] and P3_pos_x + 1 < COLS:
            P3_pos_x +=  1;
            grid[P3_pos_y][P3_pos_x] = drawing_colors[3]
        elif keys[pygame.K_j] and P3_pos_x > 0:
            P3_pos_x -=  1;
            grid[P3_pos_y][P3_pos_x] = drawing_colors[3]

        #P4
        if keys[pygame.K_DOWN] and P4_pos_y + 1 < ROWS:
            P4_pos_y +=  1;
            grid[P4_pos_y][P4_pos_x] = drawing_colors[4]
        elif keys[pygame.K_UP] and P4_pos_y > 0:
            P4_pos_y -=  1;
            grid[P4_pos_y][P4_pos_x] = drawing_colors[4]
        elif keys[pygame.K_RIGHT] and P4_pos_x + 1 < COLS:
            P4_pos_x +=  1;
            grid[P4_pos_y][P4_pos_x] = drawing_colors[4]
        elif keys[pygame.K_LEFT] and P4_pos_x > 0:
            P4_pos_x -=  1;
            grid[P4_pos_y][P4_pos_x] = drawing_colors[4]

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

                        # Setup player P1
                        P1_pos_x = 0;
                        P1_pos_y = 0;
                        grid[P1_pos_y][P1_pos_x] = drawing_colors[1]

                        # Setup player P2
                        P2_pos_x = 0;
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
                        draw_buttons(WIN, buttons)

                    #P1
                    if button.text == "D1" and P1_pos_y + 1 < ROWS:
                        P1_pos_y +=  1;
                        grid[P1_pos_y][P1_pos_x] = drawing_colors[1]
                    elif button.text == "U1" and P1_pos_y > 0:
                        P1_pos_y -=  1;
                        grid[P1_pos_y][P1_pos_x] = drawing_colors[1]
                    elif button.text == "R1" and P1_pos_x + 1 < COLS:
                        P1_pos_x +=  1;
                        grid[P1_pos_y][P1_pos_x] = drawing_colors[1]
                    elif button.text == "L1" and P1_pos_x > 0:
                        P1_pos_x -=  1;
                        grid[P1_pos_y][P1_pos_x] = drawing_colors[1]

                    #P2
                    if button.text == "D2" and P2_pos_y + 1 < ROWS:
                        P2_pos_y +=  1;
                        grid[P2_pos_y][P2_pos_x] = drawing_colors[2]
                    elif button.text == "U2" and P2_pos_y > 0:
                        P2_pos_y -=  1;
                        grid[P2_pos_y][P2_pos_x] = drawing_colors[2]
                    elif button.text == "R2" and P2_pos_x + 1 < COLS:
                        P2_pos_x +=  1;
                        grid[P2_pos_y][P2_pos_x] = drawing_colors[2]
                    elif button.text == "L2" and P2_pos_x > 0:
                        P2_pos_x -=  1;
                        grid[P2_pos_y][P2_pos_x] = drawing_colors[2]

                    #P3
                    if button.text == "D3" and P3_pos_y + 1 < ROWS:
                        P3_pos_y +=  1;
                        grid[P3_pos_y][P3_pos_x] = drawing_colors[3]
                    elif button.text == "U3" and P3_pos_y > 0:
                        P3_pos_y -=  1;
                        grid[P3_pos_y][P3_pos_x] = drawing_colors[3]
                    elif button.text == "R3" and P3_pos_x + 1 < COLS:
                        P3_pos_x +=  1;
                        grid[P3_pos_y][P3_pos_x] = drawing_colors[3]
                    elif button.text == "L3" and P3_pos_x > 0:
                        P3_pos_x -=  1;
                        grid[P3_pos_y][P3_pos_x] = drawing_colors[3]

                    #P4
                    if button.text == "D4" and P4_pos_y + 1 < ROWS:
                        P4_pos_y +=  1;
                        grid[P4_pos_y][P4_pos_x] = drawing_colors[4]
                    elif button.text == "U4" and P4_pos_y > 0:
                        P4_pos_y -=  1;
                        grid[P4_pos_y][P4_pos_x] = drawing_colors[4]
                    elif button.text == "R4" and P4_pos_x + 1 < COLS:
                        P4_pos_x +=  1;
                        grid[P4_pos_y][P4_pos_x] = drawing_colors[4]
                    elif button.text == "L4" and P4_pos_x > 0:
                        P4_pos_x -=  1;
                        grid[P4_pos_y][P4_pos_x] = drawing_colors[4]

    draw_grid(WIN, grid)

pygame.quit()
