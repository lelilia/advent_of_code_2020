''' ADVENT OF CODE day 5'''
import numpy as np

def get_part1(boardingpass):
    ''''''
    return int(boardingpass.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"),2)


if __name__ == '__main__':

    boardingpasses = np.loadtxt('input/day5.txt', dtype=str)
    boardingpasses = [get_part1(boardingpass) for boardingpass in boardingpasses]
    max_seat = max(boardingpasses)
    min_seat = min(boardingpasses)

    # Part 1
    print(f'Part 1: {max_seat}')

    # Part 2
    my_seat = list(set(range(min_seat, max_seat +1)) - set(boardingpasses))[0]
    print(f'Part 2: {my_seat}')

    # Tests
    assert get_part1("FBFBBFFRLR") == 357
    assert get_part1("BFFFBBFRRR") == 567
    assert get_part1("FFFBBBFRRR") == 119
    assert get_part1("BBFFBBFRLL") == 820
