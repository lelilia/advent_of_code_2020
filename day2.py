''' ADVENT OF CODE day 2'''

def extract_information(line):
    '''splits the line into 2 numbers, a letter and a password'''
    number1, number2, letter, password = line.replace('-', ' ').strip().split(' ')
    letter = letter[0]
    number1, number2 = int(number1), int(number2)

    return number1, number2, letter, password


def is_password_valid_part1(line):
    '''checks if the password is valid under the restrictions of part 1'''
    min_scope, max_scope, letter, password = extract_information(line)

    if min_scope <= password.count(letter) <= max_scope:
        return True
    return False


def is_password_valid_part2(line):
    '''checks if the password is valid under the restrictions of part 2'''
    pos1, pos2, letter, password = extract_information(line)

    if len(password) < pos2 :
        return False
    if (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter):
        return True
    return False

if __name__ == '__main__':
    with open('input/day2.txt') as f:
        count_1 = count_2 = 0

        for line in f:
            if is_password_valid_part1(line):
                count_1 += 1
            if is_password_valid_part2(line):
                count_2 += 1

    print(f'Part 1: {count_1}')
    print(f'Part 2: {count_2}')


