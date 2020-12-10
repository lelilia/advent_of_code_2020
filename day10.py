''' ADVENT OF CODE day 10'''

import numpy as np

if __name__ == '__main__':
    adapters = np.loadtxt('input/day10.txt', dtype=int)
    adapters.sort()


    last_jolt = 0
    stepsize = {}
    sequence_list = []
    current_sequence = 0
    solution_space = {
        2: 1,
        3: 2,
        4: 4,
        5: 7
    }

    for adapter in adapters:
        diff = adapter - last_jolt
        last_jolt = adapter
        current_sequence += 1
        if diff == 3:
            if current_sequence > 1:
                sequence_list.append(current_sequence)
            current_sequence = 0

        if diff in stepsize:
            stepsize[diff] += 1
        else:
            stepsize[diff] = 1

    if stepsize[3]:
        stepsize[3] += 1
    else:
        stepsize[3] = 1

    if current_sequence > 1:
        sequence_list.append(current_sequence + 1)


    res1 = stepsize[1] * stepsize[3]
    print(f'Part 1: {res1} ')


    #count sequences

    prod = 1
    for sequence in sequence_list:
        prod *= solution_space[sequence]

    print(f'Part 2: {prod}')
