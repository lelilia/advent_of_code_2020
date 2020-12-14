''' advend of code day 14'''

def get_memory_addresses(mask, val):

    x_positions = []
    mask_or = ['0' if m == '0' else '1' for m in mask]
    mask_or  = int(''.join(mask_or), 2)
    length = len(mask)
    for i in range(length):
        if mask[i] == 'X':
            x_positions.append(length-1 -i)
    val = val | mask_or
    q = [val]
    for pos in x_positions:
        new_q = []
        while len(q) > 0:
            curr = q.pop()
            new_q.append(curr - 2**pos)
            new_q.append(curr)
        q = new_q
    return q

def get_mask(mask):
    mask = mask.split()[-1]
    mask_and = ['1' if m == '0' else '0' for m in mask]
    mask_or  = ['1' if m == '1' else '0' for m in mask]
    mask_and = int(''.join(mask_and),2)
    mask_or  = int(''.join(mask_or), 2)
    return mask_and, mask_or


if __name__ == '__main__':
    puzzle_input = open('input/day14.txt').read().strip().split('\n')
    memory = {}
    for command in puzzle_input:
        if command.startswith('mask'):
           mask_and, mask_or = get_mask(command)
        else:
            memory_pos = command.split('[')[1].split(']')[0]
            val = int(command.split()[-1])

            val = (mask_or | val) - (mask_and & val)

            memory[memory_pos] = val
    res1 = sum([v for v in memory.values()])

    print(f'Part 1: {res1}')

    assert res1 == 14722016054794

    # Part 2
    memory = {}
    for command in puzzle_input:
        if command.startswith('mask'):
            mask = command.split()[-1]
        else:
            memory_pos = int(command.split('[')[1].split(']')[0])
            val = int(command.split()[-1])

            memory_pos_list = get_memory_addresses(mask, memory_pos)

            for pos in memory_pos_list:
                memory[pos] = val
    res2 = sum([v for v in memory.values()])

    print(f'Part 2: {res2}')
