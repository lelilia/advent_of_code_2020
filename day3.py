''' ADVENT OF CODE day 3'''

def get_tree_for_slope(grid, row_dir, col_dir):
    row_pos = 0
    col_pos = 0

    max_row = len(grid)
    max_col = len(grid[0])

    tree_count = 0

    while row_pos < max_row:
        if grid[row_pos][col_pos] == '#':
            tree_count += 1
        row_pos += row_dir
        col_pos = (col_pos + col_dir) % max_col

    return tree_count



if __name__ == '__main__':
    with open('input/day3_test.txt') as f:
        test_grid = []
        for line in f:
            test_grid.append(list(line.strip()))

    assert get_tree_for_slope(test_grid, 1,3) == 7
    prod = 1
    for x, y in [[1,1], [3,1], [5,1], [7,1], [1,2]]:

        prod *= get_tree_for_slope(test_grid, y, x)

    assert prod == 336


    with open('input/day3.txt') as f:
        grid = []
        for line in f:
            grid.append(list(line.strip()))

    # Part 1

    solution1 = get_tree_for_slope(grid, 1,3)
    print(f'Part 1: {solution1}')


    # Part 2

    solution2 = 1
    for x, y in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
        solution2 *= get_tree_for_slope(grid, y, x)

    print(f'Part 2: {solution2}')