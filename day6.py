''' ADVENT OF CODE day 6'''

def number_anyone(block):
    ...

def number_everyone(block):
    block = block.split('\n')
    set_of_answers = set(block.pop())
    while len(block) > 0:
        this_answer = set(block.pop())
        set_of_answers = set_of_answers.intersection(this_answer)
    return len(set_of_answers)


if __name__=='__main__':

    with open('input/day6.txt') as f:
        answers = f.read().split('\n\n')

    sum_questions_anyone = 0
    sum_questions_everyone = 0

    for block in answers:
        sum_questions_anyone += len(set(block.replace('\n','')))
        sum_questions_everyone += number_everyone(block)

    print(f'Part 1: {sum_questions_anyone}')

    print(f'Part 2: {sum_questions_everyone}')