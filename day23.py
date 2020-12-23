
def print_list(head):
    for _ in range(length):
        if not head:
            break
        print(head.value)
        head = head.next

def print_result(head):
    while head.value != 1:
        head = head.next
    res = ""
    head = head.next
    while head.value != 1:
        res += str(head.value)
        head = head.next
    return res

cups = list("219347865")
length = len(cups)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = LinkedList(None)
current = head
while cups:
    next_cup = LinkedList(int(cups.pop(0)))
    current.next = next_cup
    current = current.next
current.next = head.next


# pick current
current = head.next
for _ in range(100):
    cutout1 = current.next
    cutout2 = cutout1.next
    cutout3 = cutout2.next

    current.next = cutout3.next

    next_value = current.value - 1

    while next_value in [cutout1.value, cutout2.value, cutout3.value]:
        next_value -= 1
    if next_value < 1:
        next_value = length

    searching = current.next
    while searching.value != next_value:
        if searching == current:
            next_value -= 1
            if next_value == 0:
                next_value = length
        searching = searching.next

    temp = searching.next
    searching.next = cutout1
    cutout3.next = temp
    current = current.next


print(f'Part 1: {print_result(current)}')

# Part 2
cups = list("219347865")
cup_hash = {}
head = LinkedList(None)
current = head
while cups:
    value = int(cups.pop(0))
    next_cup = LinkedList(value)
    cup_hash[value] = next_cup
    current.next = next_cup
    current = current.next

for value in range(10, 1_000_001):
    next_cup = LinkedList(value)
    cup_hash[value] = next_cup
    current.next = next_cup
    current = current.next

current.next = head.next


current = head.next
for _ in range(10_000_000):
    cutout1 = current.next
    cutout2 = cutout1.next
    cutout3 = cutout2.next

    current.next = cutout3.next

    next_value = current.value - 1

    while next_value in [cutout1.value, cutout2.value, cutout3.value]:
        next_value -= 1
    if next_value < 1:
        next_value = 1_000_000

    searching = cup_hash[next_value]

    temp = searching.next
    searching.next = cutout1
    cutout3.next = temp
    current = current.next

res2 = cup_hash[1].next.value * cup_hash[1].next.next.value
print(f'Part 2: {res2}')
