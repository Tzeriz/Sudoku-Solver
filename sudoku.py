# import pygame

tile_color_list = ["#ffffff", "#cccccc", "#ffcccb"]  # white, light-gray, light-red
text_color_list = ["#000000", "#ff0000", "#0000ff"]  # black, red, blue

class Sudoku:

    def __init__(self):
        self.num = [[None for _ in range(9)] for _ in range(9)]
        self.curr_focus = (-1, -1)
        self.valid = [[[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9] * 9  # valid input list for 9 * 9 grid
        # graphic
        self.tile_color = [[tile_color_list[0] for _ in range(9)] for _ in range(9)]
        self.text_color = [[text_color_list[0] for _ in range(9)] for _ in range(9)]

    def reset(self):
        self.num = [[None for _ in range(9)] for _ in range(9)]
        self.curr_focus = (-1, -1)
        self.valid = [[[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9] * 9
        self.tile_color = [[tile_color_list[0] for _ in range(9)] for _ in range(9)]
        self.text_color = [[text_color_list[0] for _ in range(9)] for _ in range(9)]

    def enter(self, num_input):
        if self.curr_focus != (-1, -1):
            self.num[self.curr_focus[0]][self.curr_focus[1]] = num_input

    def check(self):
        # return True
        pass

    def __print__(self):
        for i in range(9):
            print("[", end="")
            for k in range(8):
                print(self.num[i][k], end=", ")
            print(self.num[i][8], "]", sep="")

    def solve(self):
        pass


def solve(grid):
    pass
