''' ADVENT OF CODE day 6'''

def get_count_any(block):
    '''count the number of unique answers in a block'''
    return len(set(block.replace('\n', '')))

def get_count_all(block):
    '''count the number of answers that everyone gave in a block'''
    block = block.split('\n')
    set_everyone =  set(block.pop())
    while len(block) > 0:
        this_answer = set(block.pop())
        set_everyone = set_everyone.intersection(this_answer)
    return len(set_everyone)


if __name__=='__main__':

    with open('input/day6.txt') as f:
        answers = f.read().split('\n\n')

    sum_any = sum(map(get_count_any, answers))
    sum_all = sum(map(get_count_all, answers))

    print(f'Part 1: {sum_any}')
    print(f'Part 2: {sum_all}')
