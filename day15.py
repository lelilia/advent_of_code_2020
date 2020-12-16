''' Advent of Code day 15 '''

def find_last_number(start_numbers, index):
    seen = {}
    for i, start_number in enumerate(start_numbers):
        seen[start_number] = i
    this_number = 0

    for i in range (len(start_numbers), index - 1):
        if this_number in seen:
            next_number = i - seen[this_number]
        else:
            next_number = 0
        seen[this_number] = i
        this_number = next_number
    return this_number

if __name__ == '__main__':

    seen = {}

    input_array = [0,12,6,13,20,1,17]

    res1 = find_last_number(input_array, 2020)
    print(f'Part 1: {res1}')

    res2 = find_last_number(input_array, 30000000)
    print(f'Part 2: {res2}')
