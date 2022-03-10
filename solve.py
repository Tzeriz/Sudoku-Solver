problem = []

"""
search black -> row, col
for i:
    if recursion() -> return true
delete()
return false
"""

def solve():
    global problem

    # check next block
    pos = None
    for i in range(81):
        if problem[i // 9][i % 9] == 0:
            pos = (i // 9, i % 9)
            break
    if pos is None:
        return True

    # check possible output
    possible = [i for i in range(1, 10)]
    for i in range(9):
        # same row
        if (pos[1] != i) and problem[pos[0]][i] in possible:
            possible.remove(problem[pos[0]][i])
        # same col
        if (pos[0] != i) and problem[i][pos[1]] in possible:
            possible.remove(problem[i][pos[1]])
    # check 3 * 3 grid
    for row_del in range(pos[0] // 3 * 3, pos[0] // 3 * 3 + 3):
        for col_del in range((pos[1] % 9) // 3 * 3, (pos[1] % 9) // 3 * 3 + 3):
            if (row_del != pos[0]) and (col_del != pos[1]) and (problem[row_del][col_del] in possible):
                possible.remove(problem[row_del][col_del])

    # recursion
    for num in possible:
        problem[pos[0]][pos[1]] = num
        if solve():
            return True
    problem[pos[0]][pos[1]] = 0
    return False
