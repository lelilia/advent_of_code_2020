'''solving Advent of Code day 13'''

if __name__ == '__main__':
    time, departures = open('input/day13.txt').read().strip().split('\n')
    departures = departures.split(',')
    time = int(time)


    next_bus = 2 * time
    res = 0

    for depart in departures:
        if depart == 'x':
            continue
        depart = int(depart)
        this_next_bus = depart - (time % depart)
        if this_next_bus < next_bus:
            next_bus = this_next_bus
            res = this_next_bus * depart
        # print(depart, this_next_bus)


    print(f'Part 1: {res}')

    # Part 2
    start = 0
    stepsize = 1
    for dt, depart in enumerate(departures):

        if depart == 'x':
            continue
        depart = int(depart)
        while start % depart != (depart - dt) % depart:
            start += stepsize
        stepsize *= depart
    print(f'Part 2: {start}')
