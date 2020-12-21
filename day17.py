import numpy as np

def get_neighbors():
    neighbours_3d = []
    neighbours_4d = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if not(i == 0 and j == 0 and k == 0):
                    neighbours_3d.append((i, j, k))
                for l in range(-1,2):
                    if not (i == 0 and j == 0 and k == 0 and l == 0):
                        neighbours_4d.append((i, j, k, l))

    return neighbours_3d, neighbours_4d

def check_neighbours(box, i, j, k, neighbours):
    count_neighbours = 0
    for a, b, c in neighbours:

        if 0 <= i + a < box.shape[0] and 0 <= j + b < box.shape[1] and 0 <= k + c < box.shape[2]:
            if box[i+a,j+b,k+c] == 1:
                count_neighbours += 1
    return count_neighbours

def check_neighbours_4d(box, i, j, k, l, neighbours_4d):
    count_neighbours = 0
    max_index = len(box) - 1
    for a, b, c, d in neighbours_4d:
        if 0 <= i + a < box.shape[0] and 0 <= j + b < box.shape[1] and 0 <= k + c < box.shape[2] and 0 <= l + d < box.shape[3]:
            if box[i+a, j+b, k+c, l+d] == 1:
                count_neighbours += 1
    return count_neighbours

if __name__ == '__main__':
    input_box = open('input/day17.txt').read().split('\n')

    SIZE = len(input_box) + 12

    initial_box = np.zeros((SIZE, SIZE, SIZE), dtype=np.uint8)

    for i in range(6, SIZE - 6):
        for j in range(6, SIZE - 6):
            if input_box[i - 6][j - 6] == '#':
                initial_box[i,j,7] = 1

    #box[6,7,7] = box[7,8,7] = box[8,6:9,7] = 1


    neighbours_3d, neighbours_4d = get_neighbors()
    boxes = [initial_box]
    for cycle in range(6):
        box = boxes.pop()
        new_box = np.zeros((SIZE, SIZE, SIZE), dtype=np.uint8)
        for i in range(5 - cycle, (SIZE - 5) + cycle):
            for j in range(5 - cycle, (SIZE - 5) + cycle):
                for k in range(5 - cycle, (SIZE - 5) + cycle):
                    neighbour_count = check_neighbours(box, i, j, k, neighbours_3d)
                    if neighbour_count == 3 or box[i,j,k] == 1 and neighbour_count == 2:
                        new_box[i,j,k] = 1
        boxes.append(new_box)

    print(np.count_nonzero(new_box))

    res1 = np.count_nonzero(new_box)
    print(f'Part 1: {res1}')

    # Part 2

    initial_box = np.zeros((SIZE, SIZE, SIZE, SIZE), dtype=np.uint8)

    for i in range(6, SIZE - 6):
        for j in range(6, SIZE - 6):
            if input_box[i - 6][j - 6] == '#':
                initial_box[i,j,7,7] = 1

    boxes = [initial_box]
    for cycle in range(6):
        box = boxes.pop()
        new_box = np.zeros((SIZE, SIZE, SIZE,SIZE), dtype=np.uint8)
        for i in range(5 - cycle, (SIZE - 5) + cycle):
            for j in range(5 - cycle, (SIZE - 5) + cycle):
                for k in range(5 - cycle, (SIZE - 5) + cycle):
                    for l in range(5 - cycle, (SIZE - 5) + cycle):
                        neighbour_count = check_neighbours_4d(box, i, j, k,l, neighbours_4d)
                        if neighbour_count == 3 or box[i,j,k,l] == 1 and neighbour_count == 2:
                            new_box[i,j,k,l] = 1
        boxes.append(new_box)

    print(np.count_nonzero(new_box))
