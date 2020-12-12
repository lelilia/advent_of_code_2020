
def count_neighbours(board, i, j):
    row_len = len(board)
    col_len = len(board[0])
    count = 0
    # -1 -1
    if i > 0 and j > 0 and board[i-1][j-1] == '#':
        count += 1
    # -1  0
    if i > 0 and board[i-1][j] == '#':
        count += 1
    # -1 +1
    if i > 0 and j < col_len - 1 and board[i-1][j + 1] == '#':
        count += 1
    #  0 -1
    if j > 0 and board[i][j - 1] == '#':
        count += 1
    #  0 +1
    if j < col_len - 1 and board[i][j + 1] == '#':
        count += 1
    # +1 -1
    if i < row_len - 1 and j > 0 and board[i+1][j-1] == '#':
        count += 1
    # +1  0
    if i < row_len - 1 and board[i+1][j] == '#':
        count += 1
    # +1 +1
    if i < row_len - 1 and j < col_len - 1 and board[i+1][j+1] == '#':
        count += 1

    return count

def print_board(board):
    for row in board:
        print(''.join(row))

def count_visible(board, i, j):
    col_len = len(board[0])
    row_len = len(board)
    count = 0
    # -1 -1
    c_i = i -1
    c_j = j -1
    while c_i >= 0 and c_j >= 0:
        if board[c_i][c_j] == '#':
            count += 1
            #print("-1 -1")
            break
        if board[c_i][c_j] == 'L':
            break
        c_i -= 1
        c_j -= 1
    # -1  0
    c_i = i -1
    c_j = j
    while c_i >= 0:
        if board[c_i][c_j] == '#':
            count += 1
            #print("-1  0")
            break
        if board[c_i][c_j] == 'L':
            break
        c_i -= 1
    # -1 +1
    c_i = i -1
    c_j = j + 1
    while c_i >= 0 and c_j < col_len:
        if board[c_i][c_j] == '#':
            count += 1
            #print("-1 +1")
            break
        if board[c_i][c_j] == 'L':
            break
        c_i -= 1
        c_j += 1
    #  0 -1
    c_i = i
    c_j = j -1
    while  c_j >= 0:
        if board[c_i][c_j] == '#':
            count += 1
            #print(" 0 -1")
            break
        if board[c_i][c_j] == 'L':
            break
        c_j -= 1
    #  0 +1
    c_i = i
    c_j = j + 1
    while  c_j < col_len:
        if board[c_i][c_j] == '#':
            count += 1
            #print(" 0 +1", c_i, c_j)
            break
        if board[c_i][c_j] == 'L':
            break
        c_j += 1
    # +1 -1
    c_i = i + 1
    c_j = j - 1
    while c_i < row_len  and c_j >= 0:
        if board[c_i][c_j] == '#':
            count += 1
            #print("+1 -1")
            break
        if board[c_i][c_j] == 'L':
            break
        c_i += 1
        c_j -= 1
    # +1  0
    c_i = i +1
    c_j = j
    while c_i < row_len:
        if board[c_i][c_j] == '#':
            count += 1
            #print("+1  0")
            break
        if board[c_i][c_j] == 'L':
            break
        c_i += 1
    # +1 +1
    c_i = i + 1
    c_j = j + 1
    while c_i < row_len and c_j < col_len:
        if board[c_i][c_j] == '#':
            count += 1
            #print("+1 +1")
            break
        if board[c_i][c_j] == 'L':
            break
        c_i += 1
        c_j += 1
    return count

if __name__ == '__main__':

    seats = []
    seats2 = []
    row_len = 0
    with open('input/day11.txt', 'r') as f:
        for r in f.read().split('\n'):
            row_len += 1
            seats.append(list(r))
            seats2.append(list(r))


    # print_board(seats)
    # print(count_visible(seats, 1,1))
    # exit()

    did_something_change = True
    while did_something_change:
        new_seats = []
        did_something_change = False
        for x in range(len(seats)):
            new_row = []
            for y in range(len(seats[0])):

                if seats[x][y] == '.':
                    new_row.append('.')
                elif seats[x][y] == '#':
                    if count_neighbours(seats, x, y) >= 4:
                        new_row.append('L')
                        did_something_change = True
                    else:
                        new_row.append('#')
                else:
                    if count_neighbours(seats, x, y) == 0:
                        new_row.append('#')
                        did_something_change = True
                    else:
                        new_row.append('L')
            new_seats.append(new_row)
        seats = []
        for col in new_seats:
            seats.append(col.copy())

    count = 0
    for row in seats:
        for cell in row:
            if cell == '#':
                count += 1
    print(f'Part 1: {count}')

    # Part 2
    counter = 0
    did_something_change = True
    while did_something_change:
        counter += 1
        new_seats2 = []
        did_something_change = False
        for x in range(len(seats2)):
            new_row = []
            for y in range(len(seats2[0])):

                if seats2[x][y] == '.':
                    new_row.append('.')
                elif seats2[x][y] == '#':
                    if count_visible(seats2, x, y) >= 5:
                        new_row.append('L')
                        did_something_change = True
                    else:
                        new_row.append('#')
                else:
                    if count_visible(seats2, x, y) == 0:
                        new_row.append('#')
                        did_something_change = True
                    else:
                        new_row.append('L')
            new_seats2.append(new_row)
        seats2 = []
        for col in new_seats2:
            seats2.append(col.copy())
        # print_board(seats2)



    print(count_visible(seats2, 0, 3))


    count = 0
    for row in seats2:
        for cell in row:
            if cell == '#':
                count += 1
    print(f'Part 1: {count}')


