''' ADVENT OF CODE day 1'''

import numpy as np


def find_two_sum(sorted_list, target):
    ''' find two elements that sum up to target in a sorted list and return their product'''
    start_index = 0
    end_index = len(sorted_list)-1

    while start_index < end_index:
        sum_values = sorted_list[start_index] + sorted_list[end_index]
        if sum_values == target:
            return sorted_list[start_index] * sorted_list[end_index]
        elif sum_values > target:
            end_index -= 1
        else:
            start_index += 1
    return 0

def find_three_sum(sorted_list, target):
    ''' find three elements that sum up to target in a sorted list and return their product '''
    for i in range(len(sorted_list)-2):
        rest_target = target - sorted_list[i]
        found = find_two_sum(sorted_list[i+1:], rest_target)
        if found:
            return found * sorted_list[i]

if __name__ == '__main__':

    array = np.loadtxt('input/day1.txt', dtype=int)
    array.sort()

    part1 = find_two_sum(array, 2020)
    print(f'Part1: {part1}')

    part2 = find_three_sum(array, 2020)
    print(f'Part2: {part2}')
