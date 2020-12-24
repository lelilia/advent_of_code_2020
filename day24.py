''' advent of code day 24 '''

import numpy as np

def walk_path_and_flip(path, tiles):
    x = 0
    y = 0
    index = 0
    while index < len(path):
        step = path[index]
        if step in 'sn':
            step = path[index : index + 2]
            index += 1
        index += 1

        if step == 'e':
            y += 2
        elif step == 'se':
            x += 1
            y += 1
        elif step == 'sw':
            x += 1
            y -= 1
        elif step == 'w':
            y -= 2
        elif step == 'nw':
            x -= 1
            y -= 1
        elif step == 'ne':
            x -= 1
            y += 1

    if (x,y) in tiles:
        tiles[(x,y)] = not tiles[(x,y)]
    else:
        tiles[(x,y)] = True

def count_black(tiles):
    count = 0
    for value in tiles.values():
        if value:
            count += 1
    return count

def walk_path_and_build_grid(path, grid, start_x, start_y):
    x = 0
    y = 0
    index = 0
    while index < len(path):

        step = path[index]

        if step in 'sn':
            step = path[index : index + 2]
            index += 1
        index += 1
        if step == 'e':
            y += 2
        elif step == 'se':
            x += 1
            y += 1
        elif step == 'sw':
            x += 1
            y -= 1
        elif step == 'w':
            y -= 2
        elif step == 'nw':
            x -= 1
            y -= 1
        elif step == 'ne':
            x -= 1
            y += 1


    grid[start_x + x, start_y + y] = (grid[start_x + x, start_y + y] + 1) % 2

    return grid, start_x, start_y

if __name__ == '__main__':

    with open('input/day24.txt', 'r') as f:
        paths = f.read().split('\n')

    tiles = {}

    for path in paths:
        walk_path_and_flip(path, tiles)


    print(count_black(tiles))

    print(min([x for x,y in tiles.keys()]))
    print(max([x for x,y in tiles.keys()]))
    print(min([y for x,y in tiles.keys()]))
    print(max([y for x,y in tiles.keys()]))

    grid = np.zeros((300, 300))
    start_x = 120
    start_y = 135

    for path in paths:
        grid, start_x, start_y = walk_path_and_build_grid(path, grid, start_x, start_y)


    print(np.count_nonzero(grid))



    def get_neighbours(grid, x, y):
        steps = [(0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        count = 0
        for dx, dy in steps:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                if grid[x + dx, y + dy] == 1:
                    count += 1
        return count

    grids = [grid]
    for round in range(100):
        print(round)
        grid = grids.pop()
        new_grid = np.zeros((300, 300))
        for x, col in enumerate(grid):
            for y, cell in enumerate(col):
                count = get_neighbours(grid, x, y)
                if count == 2 or cell == 1 and count == 1:
                    new_grid[x,y] = 1
        grids.append(new_grid)


    print(np.count_nonzero(grids.pop()))