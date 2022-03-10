problem = []


# Try and continue approach
"""
search black -> row, col
for i:
    if recursion() -> return true
delete()
return false
"""

def solve_4():
    global problem

    # check next block
    pos = None
    for i in range(16):
        if problem[i // 4][i % 4] == 0:
            pos = (i // 4, i % 4)
            break
    if pos is None:
        return True

    # check possible output
    possible = [i for i in range(1, 5)]
    for i in range(4):
        # same row
        if (pos[1] != i) and problem[pos[0]][i] in possible:
            possible.remove(problem[pos[0]][i])
        # same col
        if (pos[0] != i) and problem[i][pos[1]] in possible:
            possible.remove(problem[i][pos[1]])
    # check 2 * 2 grid
    for row_del in range(pos[0] // 2 * 2, pos[0] // 2 * 2 + 2):
        for col_del in range((pos[1] % 4) // 2 * 2, (pos[1] % 4) // 2 * 2 + 2):
            if (row_del != pos[0]) and (col_del != pos[1]) and (problem[row_del][col_del] in possible):
                possible.remove(problem[row_del][col_del])

    # recursion
    for num in possible:
        problem[pos[0]][pos[1]] = num
        if solve_4():
            return True
    problem[pos[0]][pos[1]] = 0
    return False


def main():
    global problem

    # Test
    # problem_text = "4..331..2..1..2."
    problem_text = "." * 16
    problem = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(16):
        problem[i // 4][i % 4] = 0 if problem_text[i] == "." else int(problem_text[i])

    print(solve_4())
    print(problem)


if __name__ == '__main__':
    main()
