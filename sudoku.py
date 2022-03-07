# import pygame

tile_color_list = ["#ffffff", "#cccccc", "#ffcccb"]

class Sudoku:

    def __init__(self):
        self.grid = [[Tile() for _ in range(9)] for _ in range(9)]

    def check(self):
        pass

    def __print__(self):
        for i in range(9):
            print("[", end="")
            for k in range(8):
                print(self.grid[i][k], end=", ")
            print(self.grid[i][8], "]", sep="")


class Tile:

    def __init__(self):
        self.num = 0
        self.color = tile_color_list[0]
