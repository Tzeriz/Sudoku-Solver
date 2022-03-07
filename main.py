import sys
import pygame
from sudoku import *

""" Pygame Setup and Global Variables"""
pygame.init()
screen = pygame.display.set_mode((390, 600))
pygame.display.set_caption("Sudoku Solver")
scr = [screen.get_size()[0] - 2, screen.get_size()[1] - 27]
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 100)

""" Graphic Global Variables """
background_color, line_color, text_color = (255, 255, 255), (0, 0, 0), (0, 0, 0)


""" UI Graphics """
def draw(curr_sudoku):
    global screen, scr

    tile_size, tile_spacing = scr[0] // 11 - 1, (2, 1)  # tile spacing = (thin spacing, thick spacing)
    grid_side = tile_size * 9 + 4 * tile_spacing[0] + 6 * tile_spacing[1]
    grid_rect = [(scr[0] - grid_side) / 2, scr[1] / 8, grid_side, grid_side]  # [x, y, width, height]
    font = pygame.font.SysFont("Helvetica", int(tile_size / 1.5))

    screen.fill(background_color)  # UI background
    pygame.draw.rect(screen, line_color, grid_rect)  # grid background (border)

    # Draw Tile
    for i in range(9):  # row
        for k in range(9):  # col
            # Draw Tile
            tile_rect = [grid_rect[0] + tile_size * k + tile_spacing[0] * (k // 3 + 1) + tile_spacing[1] * (k - k // 3),  # tile.x = grid.x + num * tile size + num * thick space + num * thin space
                         grid_rect[1] + tile_size * i + tile_spacing[0] * (i // 3 + 1) + tile_spacing[1] * (i - i // 3),
                         tile_size, tile_size]
            pygame.draw.rect(screen, curr_sudoku.grid[i][k].color, tile_rect)
            # Blit text
            if curr_sudoku.grid[i][k].num != 0:
                text_render = font.render(str(curr_sudoku.grid[i][k].num), True, text_color)
                text_rect = text_render.get_rect(center=(tile_rect[0] + tile_size / 2, tile_rect[1] + tile_size / 2))  # put text on rectangle
                screen.blit(text_render, text_rect)


""" main() """
def main():
    """ Sudoku Setup """
    sudoku = Sudoku()
    sudoku.grid[3][3].num = 5
    sudoku.grid[3][8].num = 5
    sudoku.grid[3][3].color = "#cccccc"
    sudoku.grid[5][3].color = "#ffcccb"
    # sudoku.__print__()

    """ Function Loop"""
    end = False

    while not end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw(sudoku)

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
