import solve

tile_color_list = ["#ffffff", "#cccccc", "#ffcccb"]  # white, light-gray, light-red
text_color_list = ["#000000", "#ff0000", "#0000ff"]  # black, red, blue

class Sudoku:

    def __init__(self):
        self.num = [[0 for _ in range(9)] for _ in range(9)]  # 0 represent a empty tile
        self.curr_focus = (-1, -1)
        # graphic
        self.tile_color = [[tile_color_list[0] for _ in range(9)] for _ in range(9)]
        self.text_color = [[text_color_list[0] for _ in range(9)] for _ in range(9)]

    def reset(self):
        self.num = [[0 for _ in range(9)] for _ in range(9)]
        self.curr_focus = (-1, -1)
        self.tile_color = [[tile_color_list[0] for _ in range(9)] for _ in range(9)]
        self.text_color = [[text_color_list[0] for _ in range(9)] for _ in range(9)]

    def enter(self, num_input):
        if self.curr_focus != (-1, -1):
            self.num[self.curr_focus[0]][self.curr_focus[1]] = num_input

    def check(self):
        for row in range(9):
            for col in range(9):
                num = self.num[row][col]
                if num == 0:
                    continue
                # same row or col
                for i in range(9):
                    if (i != row and self.num[i][col] == num) or (i != col and self.num[row][i] == num):
                        return False
                # check 3 * 3 grid
                for row_block in range(row // 3 * 3, row // 3 * 3 + 3):
                    for col_block in range((col % 9) // 3 * 3, (col % 9) // 3 * 3 + 3):
                        if row_block != row and col_block != col and self.num[row_block][col_block] == num:
                            return False
        return True

    def solve(self):
        solve.problem = self.num
        for row in range(9):
            for col in range(9):
                if self.num[row][col] == 0:
                    self.text_color[row][col] = text_color_list[1]
        if not solve.solve():
            self.text_color = [[text_color_list[0] for _ in range(9)] for _ in range(9)]
            return False
        return True
