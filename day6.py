''' ADVENT OF CODE day 6'''

from functools import reduce

def get_count_any(block):
    '''count the number of unique answers in a block'''
    return len(set(block.replace('\n', '')))

def get_count_all(block):
    '''count the number of answers that everyone gave in a block'''
    return len(reduce(lambda x,y: set(x).intersection(set(y)), block.split("\n")))


if __name__=='__main__':

    with open('input/day6.txt') as f:
        blocks = f.read().split('\n\n')

    sum_any = sum(map(get_count_any, blocks))
    sum_all = sum(map(get_count_all, blocks))

    print(f'Part 1: {sum_any}')
    print(f'Part 2: {sum_all}')
