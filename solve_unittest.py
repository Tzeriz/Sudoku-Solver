import unittest
import solve

def valid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            num = grid[row][col]
            if num == 0:
                return False
            # same row or col
            for i in range(9):
                if (i != row and grid[i][col] == num) or (i != col and grid[row][i] == num):
                    return False
            # check 3 * 3 grid
            for row_block in range(row // 3 * 3, row // 3 * 3 + 3):
                for col_block in range((col % 9) // 3 * 3, (col % 9) // 3 * 3 + 3):
                    if row_block != row and col_block != col and grid[row_block][col_block] == num:
                        return False
    return True

class Sudoku_Test(unittest.TestCase):
    def setUp(self) -> None:
        solve.problem = [[0 for _ in range(9)] for _ in range(9)]
        self.solution_str = ""
        self.answer_str = None

    def tearDown(self) -> None:
        # Problem List Setup
        for i in range(81):
            solve.problem[i // 9][i % 9] = 0 if self.problem_str[i] == "0" else int(self.problem_str[i])
        # solution_str set up
        # Check if problem can be and is being solved
        self.assertTrue(solve.solve())
        # Check if solution is valid
        if self.answer_str is None:
            self.assertTrue(valid(solve.problem))
        else:
            for row in range(9):
                for col in range(9):
                    self.solution_str += str(solve.problem[row][col])
            self.assertEquals(self.solution_str, self.answer_str)

    # Test case naming format: test_solve_[difficulty level]_[case number]
    # Test case are found on: http://lipas.uwasa.fi/~timan/sudoku/

    # Solve empty grid
    def test_solve_0(self):
        self.problem_str = "0" * 81

    def test_solve_1_1(self):
        self.problem_str = "040000179002008054006005008080070910050090030019060040300400700570100200928000060"
        self.answer_str = "845632179732918654196745328683574912457291836219863547361429785574186293928357461"

    def test_solve_1_2(self):
        self.problem_str = "802050701007082460010900000600001832500000009184300006000004020095610300308090607"
        self.answer_str = "832456791957182463416973258679541832523768149184329576761834925295617384348295617"

    def test_solve_1_3(self):
        self.problem_str = "000000007720309001008705060502890000040501090000063705030906100200107053900000000"
        self.answer_str = "495618237726349581318725469572894316643571892189263745837956124264187953951432678"

    def test_solve_2_1(self):
        self.problem_str = "206000049037009000100700006000580900705000804009062000900004001000300490410000208"
        self.answer_str = "256831749837649512194725386641587923725193864389462175978254631562318497413976258"

    def test_solve_3_1(self):
        self.problem_str = "050200000300005080960078200000030020708000103040080000001640032070500001000009050"
        self.answer_str = "857261394312495786964378215195734628728956143643182579581647932479523861236819457"


if __name__ == '__main__':
    unittest.main()
