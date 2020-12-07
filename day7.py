''' ADVENT OF CODE day 7'''

class Bag():
    def __init__(self, color):
        self.color = color
        self.contains = []
        self.contains_gold = False
        self.inside_of = []
        self.contains_bags = None
        self.number_of_bags_inside = None

    def __repr__(self):
        return f'<Bag {self.color}: {len(self.contains)}, {self.contains_gold} {self.number_of_bags_inside}>'

    def add_content(self, count, next_bag):
        self.contains.append([count, next_bag])



bags = {}
golden = []
end_bags = []
with open("input/day7.txt", "r") as f:
    for line in f:
        parent, children = line.strip().split('contain')

        parent = parent[:-6]
        children = children.split(',')
        if parent in bags:
            outer_bag = bags[parent]
        else:
            outer_bag = Bag(parent)
            bags[parent] = outer_bag
        for child in children:
            child = child.strip()
            if child[0] == 'n':
                outer_bag.number_of_bags_inside = 0
                if outer_bag not in end_bags:
                    end_bags.append(outer_bag)
                continue
            count = int(child[0])
            child = ' '.join(child.split(' ')[1:3])

            if child in bags:
                inner_bag = bags[child]
            else:
                inner_bag = Bag(child)
                bags[child] = inner_bag
            if child == 'shiny gold':
                outer_bag.contains_gold = True
                inner_bag.contains_gold = True
                golden_start = inner_bag
            outer_bag.add_content(count, inner_bag)
            inner_bag.inside_of.append(outer_bag)


count_outer_bags = 0
seen = {}

q = [golden_start]
while len(q) > 0:
    current_bag = q.pop()
    if current_bag not in seen:
        count_outer_bags += 1
    seen[current_bag] = True

    q.extend(current_bag.inside_of)

print(f'Part 1: {count_outer_bags -1}')



q = end_bags
seen = {}

while len(q) > 0:
    current_bag = q.pop()
    seen[current_bag] = True

    for outer_bag in current_bag.inside_of:
        
        outer_bag.contains_bags = []
        q.append(outer_bag)
        for count, inner_bag in outer_bag.contains:
            if inner_bag.number_of_bags_inside is not None:
                outer_bag.contains_bags.append(count * (1 + inner_bag.number_of_bags_inside))
            else:
                outer_bag.contains_bags.append(None)
        if None not in outer_bag.contains_bags:
            outer_bag.number_of_bags_inside = sum(outer_bag.contains_bags)

print(f'Part 2: {golden_start.number_of_bags_inside}')