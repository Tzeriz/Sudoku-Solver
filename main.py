# https://github.com/Tzeriz/Sudoku-Solver

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

Title: title_rect, title_button
Tile: tile_size, tile_spacing, tile_font
Grid: grid_side, grid_row, grid_col, grid_rect
Number option: num_y, num_x, num_rect_size, num_font
Button: button_size, button_space, button_rect, button_text, button_font, button_color
Message: message_rect, message_status, message_text, message_font
Exit Image: exit_button, exit_button_rect
"""

# Global Variable Declaration
# tile and grid global var
tile_size = scr[0] // 11
grid_row, grid_col = [0] * 9, [0] * 9
tile_spacing = (2, 1)  # tile spacing = (thin spacing, thick spacing)
tile_font = pygame.font.SysFont("garamond", int(tile_size / 1.5))
grid_side = tile_size * 9 + 4 * tile_spacing[0] + 6 * tile_spacing[1]
grid_rect = [(scr[0] - grid_side) / 2, scr[1] / 3.2, grid_side, grid_side]  # [x, y, width, height]
# title global var
title_rect = [scr[0] / 6, scr[1] * 0.04, scr[0] * 2 / 3, scr[0] / 3]
title_button = pygame.transform.scale(pygame.image.load('sudoku_solver_title.png').convert_alpha(), (scr[0] * 2 / 3, scr[0] / 3))
# num global var
num_rect_size = scr[0] // 10
num_y = scr[1] * 0.85
num_x = [(scr[0] - 9 * num_rect_size) / 2]
num_font = pygame.font.SysFont("garamond", int(num_rect_size / 1.5))
# button global var
button_rect = [[0] * 4] * 3
button_size = (scr[0] // 5.5, scr[1] // 20)
button_font = pygame.font.SysFont("castellar", int(button_size[1] // 1.75))
# harrington,
button_text = ["Delete", "Clear", "Solve"]
# button_color = ["#900603", "#fca510", "#32612d"]
button_space = button_size[0] * 0.65
# message list
message_status = 0
message_list = ["Please input the puzzle and click \"solve\"", "Invalid Input! Please try again", "Solving...", "Sudoku Solved!", "No valid solution"]
message_rect = [scr[0] / 6, scr[1] / 4.05, scr[0] * 2 / 3, scr[1] / 24]
# exit image
exit_button = pygame.transform.scale(pygame.image.load('exit.png').convert_alpha(), (scr[1] / 25, scr[1] / 25))
exit_button_rect = [scr[0] - exit_button.get_size()[0] - 15, 20, exit_button.get_size()[0], exit_button.get_size()[1]]

# Initialize Lists
# Tile var
for index in range(9):
    # store row pos
    grid_row[index] = grid_rect[1] + tile_size * index + tile_spacing[0] * (index // 3 + 1) + tile_spacing[1] * (
                index - index // 3)
    # store col pos
    # tile.x = grid.x + num * tile size + num * thick space + num * thin space
    grid_col[index] = grid_rect[0] + tile_size * index + tile_spacing[0] * (index // 3 + 1) + tile_spacing[1] * (
                index - index // 3)

# Number Option
for _ in range(8):
    num_x.append(num_x[-1] + num_rect_size)

# Three Button - Delete, Clear, and Solve
for button_num in range(3):
    #  draw button rect
    button_rect[button_num] = [
        (scr[0] - 3 * button_size[0] - 2 * button_space) / 2 + button_num * (button_size[0] + button_space),
        scr[1] * 0.93, button_size[0], button_size[1]]


# UI Graphics
def draw(curr_sudoku):
    screen.fill(sudoku.tile_color_list[0])  # UI background

    """ Title """
    screen.blit(title_button, title_rect)

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
            if curr_sudoku.num[i][k] != 0:
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
        # pygame.draw.rect(screen, button_color[i], button_rect[i])
        # blit button text
        button_render = button_font.render(button_text[i], True, sudoku.text_color_list[0])
        button_text_rect = button_render.get_rect(
            center=(button_rect[i][0] + button_rect[i][2] // 2, button_rect[i][1] + button_rect[i][3] / 2))
        screen.blit(button_render, button_text_rect)

    """ Message """
    message_font = pygame.font.SysFont("garamond", 17 if message_status <= 1 else 22)
    message_render = message_font.render(message_list[message_status], True, sudoku.text_color_list[1] if message_status == 1 else sudoku.text_color_list[0])
    message_text_rect = message_render.get_rect(
        center=(message_rect[0] + message_rect[2] / 2, message_rect[1] + message_rect[3] / 2))
    screen.blit(message_render, message_text_rect)

    # Exit
    screen.blit(exit_button, exit_button_rect)

    # Pygame Update
    pygame.display.update()


# Focus to clicked tile
def focus_tile(curr_sudoku, curr_mouse):
    # Return: True if a tile is being clicked
    global grid_row, grid_col, tile_size

    # check which pos in the grid is being clicked on
    for i in range(9):
        if 0 <= curr_mouse[1] - grid_row[i] <= tile_size:
            for k in range(9):
                # print(curr_mouse)
                if 0 <= curr_mouse[0] - grid_col[k] <= tile_size:
                    curr_sudoku.curr_focus = (i, k)
                    draw(curr_sudoku)


# Input number to currently focused tile
def input_num(curr_sudoku, curr_mouse):
    # Return: True if a num tile has been clicked
    global num_rect_size, num_x, num_y, message_status

    # check which pos in the grid is being clicked on
    if 0 <= curr_mouse[1] - num_y <= num_rect_size:
        for i in range(9):
            if 0 <= curr_mouse[0] - num_x[i] <= num_rect_size:
                # enter
                curr_sudoku.enter(i + 1)
                # update message
                message_update(0, curr_sudoku)


# Delete curr tile value if clicked
def delete(curr_sudoku, curr_mouse):
    global button_size, button_rect, message_status

    if 0 <= curr_mouse[0] - button_rect[0][0] <= button_size[0] and 0 <= curr_mouse[1] - button_rect[0][1] <= button_size[1]:
        # delete num
        curr_sudoku.num[curr_sudoku.curr_focus[0]][curr_sudoku.curr_focus[1]] = 0
        # update message
        message_update(0, curr_sudoku)


def click_clear(curr_sudoku, curr_mouse):
    global button_size, button_rect, message_status
    if 0 <= curr_mouse[0] - button_rect[1][0] <= button_size[0] and 0 <= curr_mouse[1] - button_rect[1][1] <= button_size[1]:
        # clear
        curr_sudoku.reset()
        # update message
        message_update(0, curr_sudoku)
        return True
    return False


# check if 'solve' is clicked, return bool
def click_solve(curr_mouse) -> bool:
    global button_size, button_rect
    return 0 <= curr_mouse[0] - button_rect[2][0] <= button_size[0] and 0 <= curr_mouse[1] - button_rect[2][1] <= button_size[1]


def message_update(status, curr_sudoku):
    global message_status
    if status == 0:
        curr_sudoku.text_color = [[sudoku.text_color_list[0] for _ in range(9)] for _ in range(9)]
    message_status = status
    draw(curr_sudoku)


# MAIN()
# Function Loop
def main():
    global message_status

    """ Sudoku Setup """
    solver = sudoku.Sudoku()

    """ Function Loop"""
    draw(solver)
    solved = False

    while True:

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                mouse = pygame.mouse.get_pos()

                # Quit
                if 0 <= mouse[0] - exit_button_rect[0] <= exit_button_rect[2] and 0 <= mouse[1] - exit_button_rect[1] <= exit_button_rect[3]:
                    pygame.quit()
                    sys.exit()

                # User Actions
                if solved:  # when sudoku is solved, prevent user action other than 'clear'
                    solved = not click_clear(solver, mouse)
                # user action - focus, input, and delete
                else:
                    focus_tile(solver, mouse) or input_num(solver, mouse) or delete(solver, mouse) or click_clear(solver, mouse)
                    # solve
                    if click_solve(mouse):
                        if solver.check():  # valid input
                            message_update(2, solver)  # message: invalid input
                            if solver.solve():  # solve
                                solver.curr_focus = (-1, -1)  # remove focusing when solved
                                solved = True
                                message_update(3, solver)  # message: solved
                            else:
                                message_update(5, solver)  # message: no solution
                        else:
                            message_update(1, solver)  # message: entering


if __name__ == '__main__':
    main()
