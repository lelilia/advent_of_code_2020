''' ADVENT OF CODE day 9'''

import numpy as np


def check_if_valid(array, preamble_length, index):
    '''
    check if there are two values in the subarray of length
    preamble_length before the index that sum up to the value
    of the array at index
    '''

    for i in range(index-preamble_length, index-1):
        for j in range(i+1, index):
            if array[i] + array[j] == array[index]:
                return True
    return False

def find_sequence(array, target):
    '''
    find a sequence in the array that sums up to target
    '''
    i = j = 0
    current_sum = array[0]
    while j < len(array):
        if current_sum > target:
            current_sum -= array[i]
            i += 1
        elif current_sum < target:
            j += 1
            current_sum += array[j]
        elif current_sum == target:
            min_val = min(array[i:j])
            max_val = max(array[i:j])
            return min_val + max_val


def find_first_invalid(array, preamble_length):
    '''
    find the first number in an array after the preamble
    where the value is not a sum of two values in the part of the
    array before the value of preable length
    '''
    for i in range(preamble_length, len(array)):
        if not check_if_valid(array, preamble_length, i):
            return array[i]

if __name__ == '__main__':
    code = np.loadtxt('input/day9.txt', dtype=int)
    PREAMBLE = 25
    first_invalid_number = find_first_invalid(code, PREAMBLE)

    # Part 1
    print(f'Part 1: {first_invalid_number}')

    # Part 2
    res_part2 = find_sequence(code, first_invalid_number)
    print(f'Part 2: {res_part2}')

    # Tests
    test_code = np.loadtxt('input/day9_test.txt', dtype=int)
    TEST_PREABLE = 5
    test_first_invalid_number = find_first_invalid(test_code, TEST_PREABLE)
    assert test_first_invalid_number == 127
    assert find_sequence(test_code, test_first_invalid_number) == 62
