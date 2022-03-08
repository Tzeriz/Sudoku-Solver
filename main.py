import sys
import pygame

import sudoku

""" Pygame Setup and Global Variables"""
pygame.init()
screen = pygame.display.set_mode((400, 400 * 16 / 9))
# Preset size = (390, 600)
pygame.display.set_caption("Sudoku Solver")
scr = [screen.get_size()[0] - 2, screen.get_size()[1] - 27]
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 100)

""" 
Graphic Global Variables

Title: title_rect, title_font,
Tile: tile_size, tile_spacing, tile_font
Grid: grid_side, grid_row, grid_col, grid_rect
Number option: num_y, num_x, num_rect_size, num_font
Button: button_size, button_space, button_rect, button_text, button_font
Message: message_rect, message_status, message_text, message_font
"""


# Global Variable Declaration
# tile and grid global var
tile_size = scr[0] // 11
grid_row, grid_col = [0] * 9, [0] * 9
tile_spacing = (2, 1)  # tile spacing = (thin spacing, thick spacing)
tile_font = pygame.font.SysFont("Helvetica", int(tile_size / 1.5))
grid_side = tile_size * 9 + 4 * tile_spacing[0] + 6 * tile_spacing[1]
grid_rect = [(scr[0] - grid_side) / 2, scr[1] / 5.5, grid_side, grid_side]  # [x, y, width, height]
# title global var
title_rect = [scr[0] / 4, scr[1] * 0.075, scr[0] / 2, scr[1] * 0.05]
title_font = pygame.font.SysFont("Helvetica", scr[0] // 13)
# num global var
num_rect_size = scr[0] // 10 + 1
num_y = scr[1] * 23.5 / 32
num_x = [(scr[0] - 9 * num_rect_size) / 2]  # -1 is for adjusting alignment with grid
num_font = pygame.font.SysFont("Helvetica", int(num_rect_size // 1.5))
# button global var
button_rect = [[0] * 4] * 3
button_size = (scr[0] // 5.5, scr[1] // 20)
button_font = pygame.font.SysFont("Helvetica", int(button_size[1] // 1.75))
button_text = ["Delete", "Clear", "Solve"]
button_space = button_size[0] * 0.65
# message list
message_status = 0
message_list = ["Please enter at least 16 numbers to start solving", "Invalid Input", "Solving...",
                "Sudoku Solved!"]
message_rect = [scr[0] / 6, scr[1] * 11 / 12, scr[0] / 4, scr[1] / 24]

# Initialize Lists
# Tile var
for index in range(9):
    # store row pos
    grid_row[index] = grid_rect[1] + tile_size * index + tile_spacing[0] * (index // 3 + 1) + tile_spacing[1] * (index - index // 3)
    # store col pos
    # tile.x = grid.x + num * tile size + num * thick space + num * thin space
    grid_col[index] = grid_rect[0] + tile_size * index + tile_spacing[0] * (index // 3 + 1) + tile_spacing[1] * (index - index // 3)

# Number Option
for _ in range(8):
    num_x.append(num_x[-1] + num_rect_size)

# Three Button - Delete, Clear, and Solve
for button_num in range(3):
    #  draw button rect
    button_rect[button_num] = [(scr[0] - 3 * button_size[0] - 2 * button_space) / 2 + button_num * (button_size[0] + button_space), scr[1] * 7.5 / 9, button_size[0], button_size[1]]


# UI Graphics
def draw(curr_sudoku):

    screen.fill(sudoku.tile_color_list[0])  # UI background

    """ Title """
    text_render = title_font.render("Sudoku Solver", True, sudoku.text_color_list[0])
    text_rect = text_render.get_rect(center=(title_rect[0] + title_rect[2] / 2, title_rect[1] + title_rect[3] / 2))
    screen.blit(text_render, text_rect)

    """Grid / Tile"""
    # Draw Grid
    pygame.draw.rect(screen, sudoku.text_color_list[0], grid_rect)  # grid background (border)

    # Draw Tile
    for i in range(9):  # row
        for k in range(9):  # col
            # draw Tile
            tile_rect = [grid_col[k], grid_row[i], tile_size, tile_size]
            if curr_sudoku.curr_focus == (i, k):
                pygame.draw.rect(screen, sudoku.tile_color_list[1], tile_rect)  # focus tile - gray
            else:
                pygame.draw.rect(screen, curr_sudoku.tile_color[i][k], tile_rect)

            # Blit text
            if curr_sudoku.num[i][k] is not None:
                text_render = tile_font.render(str(curr_sudoku.num[i][k]), True, curr_sudoku.text_color[i][k])
                text_rect = text_render.get_rect(
                    center=(tile_rect[0] + tile_size / 2, tile_rect[1] + tile_size / 2))  # put text on rectangle
                screen.blit(text_render, text_rect)

    """ Number Option """
    for i in range(9):
        num_rect = [num_x[i], num_y, num_rect_size, num_rect_size]
        num_render = num_font.render(str(i + 1), True, sudoku.text_color_list[0])
        num_text_rect = num_render.get_rect(center=(num_rect[0] + num_rect[2] // 2, num_rect[1] + num_rect[3] / 2))
        screen.blit(num_render, num_text_rect)

    """ Three Button - Delete, Clear, and Solve"""
    for i in range(3):
        # draw button rect
        pygame.draw.rect(screen, "#cccccc", button_rect[i])
        # blit button text
        button_render = button_font.render(button_text[i], True, sudoku.text_color_list[0])
        button_text_rect = button_render.get_rect(
            center=(button_rect[i][0] + button_rect[i][2] // 2, button_rect[i][1] + button_rect[i][3] / 2))
        screen.blit(button_render, button_text_rect)



# Check if a tile is clicked - Focus
def click_grid(curr_sudoku, curr_mouse):
    # Return: True if a tile is being clicked
    global grid_row, grid_col, tile_size

    # check which pos in the grid is being clicked on
    for i in range(9):
        if 0 <= curr_mouse[1] - grid_row[i] <= tile_size:
            for k in range(9):
                # print(curr_mouse)
                if 0 <= curr_mouse[0] - grid_col[k] <= tile_size:
                    curr_sudoku.curr_focus = (i, k)
                    return True
    return False


# Check if a number option is being clicked - Input
def click_num(curr_sudoku, curr_mouse):
    # Return: True if a num tile has been clicked
    global num_rect_size, num_x, num_y

    # check which pos in the grid is being clicked on
    if 0 <= curr_mouse[1] - num_y <= num_rect_size:
        for i in range(9):
            if 0 <= curr_mouse[0] - num_x[i] <= num_rect_size:
                curr_sudoku.enter(i + 1)
                return True
    return False


# Check if a button has been clicked - Function (delete, clear, and solve)
def click_button(curr_sudoku, curr_mouse):
    global button_size, button_rect

    for i in range(3):
        if 0 <= curr_mouse[0] - button_rect[i][0] <= button_size[0] and 0 <= curr_mouse[1] - button_rect[i][1] <= \
                button_size[1]:
            if i == 0:
                curr_sudoku.num[curr_sudoku.curr_focus[0]][curr_sudoku.curr_focus[1]] = None
            elif i == 1:
                curr_sudoku.reset()
            elif i == 2:
                curr_sudoku.solve()
            return True
    return False


# MAIN()
# Function Loop
def main():
    """ Sudoku Setup """
    solver = sudoku.Sudoku()

    """ Function Loop"""
    draw(solver)
    pygame.display.update()

    end = False
    while not end:

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                mouse = pygame.mouse.get_pos()
                if click_grid(solver, mouse) or click_num(solver, mouse) or click_button(solver, mouse):
                    draw(solver)
                    pygame.display.update()

        # Draw
        clock.tick(20)


if __name__ == '__main__':
    main()
