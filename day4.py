''' ADVENT OF CODE day 4'''

import re


def check_passport(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if len(passport) < 7:
        return False
    fields = set()
    for field in passport:
        field = field.split(':')[0]
        fields.add(field)
    if required_fields - fields == set():
        return True
    return False

def check_passport_strict(passport):
    for field in passport:
        field, value = field.split(':')
        if field == 'byr':
            if not (1920 <= int(value) <= 2002):
                return False
        elif field == 'iyr':
            if not (2010 <= int(value) <= 2020):
                return False
        elif field == 'eyr':
            if not (2020 <= int(value) <= 2030):
                return False
        elif field == 'hgt':
            if value[-2:] == 'cm':
                if not(150 <= int(value[:-2]) <= 193):
                    return False
            elif value[-2:] == 'in':
                if not(59 <= int(value[:-2]) <= 76):
                    return False
            else:
                return False
        elif field == 'hcl':
            if not bool(re.match("^#([a-f0-9]{6})$", value)):
                return False
        elif field == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif field == 'pid':
            if not bool(re.match("^[0-9]{9}$", value)):
                return False
    return True

if __name__ == '__main__':


    number_of_valid_passports = 0
    number_of_valid_passports_strict = 0
    with open('input/day4.txt') as f:
        single_passport = []
        for line in f:

            if line == '\n':
                if check_passport(single_passport):
                    number_of_valid_passports += 1
                    if check_passport_strict(single_passport):
                        number_of_valid_passports_strict += 1
                single_passport = []
                continue
            single_passport.extend(line.strip().split(' '))
        if check_passport(single_passport):
            number_of_valid_passports += 1
            if check_passport_strict(single_passport):
                number_of_valid_passports_strict += 1
    print (f'Part 1: {number_of_valid_passports}')
    print(f'Part 2: {number_of_valid_passports_strict}')