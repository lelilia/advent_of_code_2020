''' Advent of Code day 12 '''

class Ship():
    def __init__(self):
        self.facing = 0
        self.n = 0
        self.e = 0

    def __repr__(self):
        return f'Part 1: {abs(self.n) + abs(self.e)}'

    def move(self, command):
        direction, value = command[0], int(command[1:])
        if direction == 'N':
            self.n += value
        elif direction == 'S':
            self.n -= value
        elif direction == 'E':
            self.e += value
        elif direction == 'W':
            self.e -= value

        elif direction == 'F':
            if self.facing == 0:
                self.e += value
            elif self.facing == 90:
                self.n -= value
            elif self.facing == 180:
                self.e -= value
            elif self.facing == 270:
                self.n += value

        elif direction == 'R':
            self.facing = (self.facing + value) % 360

        elif direction == 'L':
            self.facing = (self.facing - value) % 360


class Ship_with_waypoint():
    def __init__(self):
        self.wp = Waypoint()
        self.e = 0
        self.n = 0

    def __repr__(self):
        return f'Part 2: {(abs(self.e) + abs(self.n))}'

    def move(self, command):
        command, value = command[0], int(command[1:])

        if command in "RL":
            self.wp.rotate(command, value)
        elif command in "NESW":
            self.wp.translate(command, value)
        else:
            self.move_forward(value)

    def move_forward(self, value):
        self.e += self.wp.e * value
        self.n += self.wp.n * value

class Waypoint():
    def __init__(self):
        self.e = 10
        self.n = 1
        self.w = -10
        self.s = -1

    def __repr__(self):
        return f' <w {self.e} {self.n}>'

    def rotate(self, direction, degree):
        if degree == 90 and direction == 'R' or degree == 270 and direction == 'L':
            self.e, self.n, self.w, self.s = self.n, self.w, self.s, self.e
        if degree == 180:
            self.e, self.n, self.w, self.s = self.w, self.s, self.e, self.n
        if degree == 270 and direction == 'R' or degree == 90 and direction == 'L':
            self.e, self.n, self.w, self.s = self.s, self.e, self.n, self.w

    def translate(self, direction, length):
        if direction == 'E':
            self.e += length
            self.w -= length
        elif direction == 'N':
            self.n += length
            self.s -= length
        elif direction == 'S':
            self.s += length
            self.n -= length
        elif direction == 'W':
            self.w += length
            self.e -= length



if __name__ == '__main__':
    ship = Ship()
    ship2 = Ship_with_waypoint()


    with open('input/day12.txt', 'r') as f:
        for line in f:
            ship.move(line)
            ship2.move(line)

    print(ship)


    # Part 2

    print(ship2)