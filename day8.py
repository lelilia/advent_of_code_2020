''' ADVENT OF CODE day 8'''

def run_code(code, index_to_change=None):
    ''' runs the code based on the code '''
    index = 0
    acc = 0
    seen = {}

    while index < len(code):
        if index in seen:
            if index_to_change is None:
                return acc
            return
        seen[index] = True
        instruction, argument = code[index].split()
        argument = int(argument)
        if instruction == 'acc':
            acc += argument
            index += 1
        elif instruction == 'jmp':
            if index == index_to_change:
                index += 1
            else:
                index += argument
        elif instruction == 'nop':
            if index == index_to_change:
                index += argument
            else:
                index += 1
            continue
    return acc


def change_index(code):
    ''' for each index it changes the instruction until the code terminates '''
    c_index = 0
    while c_index < len(code):
        res = run_code(code, c_index)
        if res is not None:
            return res
        c_index += 1


if __name__ == '__main__':

    with open('input/day8.txt', 'r') as f:
        puzzle_input = f.read().split('\n')

    # Part 1
    print(f'Part 1: {run_code(puzzle_input)}')

    # Part 2
    print(f'Part 2: {change_index(puzzle_input)}')


    # Tests
    with open('input/day8_test.txt', 'r') as f:
        test_input = f.read().split('\n')

    assert run_code(test_input) == 5
    assert change_index(test_input) == 8
