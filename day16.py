


def check_value(rules, value):
    for r1_min, r1_max, r2_min, r2_max in rules:
        value = int(value)
        if r1_min <= value <= r1_max or r2_min <= value <= r2_max:
            return True
    return False

if __name__ == '__main__':
    rules_input, your_ticket, nearby_tickets  = open('input/day16.txt').read().strip().split('\n\n')

    rules_input = rules_input.split('\n')

    rules = []
    in_rules = True
    in_tickets = False

    for line in rules_input:
        line = line.split(': ')[1]
        r1_min, r1_max, _, r2_min, r2_max = line.replace('-', ' ').split()
        r1_min, r1_max, r2_min, r2_max = int(r1_min), int(r1_max), int(r2_min), int(r2_max)

        rules.append([r1_min, r1_max, r2_min, r2_max])

    valid_tickets = []

    errors = 0
    for ticket in nearby_tickets.split('\n')[1:]:
        for value in ticket.split(','):
            if not check_value(rules, value):
                errors += int(value)

    print(f'Part 1: {errors}')

    # Part 2

    could_be_rules = {}
    for i in range(len(rules)):
        could_be_rules[i] = list(range(len(rules)))

    for ticket in nearby_tickets.split('\n')[1:]:
        for i, value in enumerate(ticket.split(',')):

            value = int(value)
            for j, [r1_min, r1_max, r2_min, r2_max] in enumerate(rules):
                if i not in could_be_rules[j]:
                    continue
                if not check_value(rules, value):
                    continue
                if not (r1_min <= value <= r1_max or r2_min <= value <= r2_max):
                    could_be_rules[j].remove(i)




    found = [False for i in range(len(rules))]
    while False in found:
        for value in could_be_rules.values():
            if len(value) == 1:
                found[value[0]] = True
            else:
                for i,f in enumerate(found):
                    if i in value and f:
                        value.remove(i)

    departure = 1

    your_ticket = your_ticket.split('\n')[1].split(',')

    for depart in range(6):
        index = could_be_rules[depart][0]
        departure *= int(your_ticket[index])

    print(f'Part 2: {departure}')