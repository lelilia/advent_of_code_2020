''' advent of code day 18 '''

class Tree:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

def append_number(child, root):
    q = [root]
    while q:
        current = q.pop(0)
        if isinstance(current.value, str) or current.value is None:
            if current.left is None:
                current.left = child
                return
            elif current.right is None:
                current.right = child
                return
        if current.left:
            q.append(current.left)
            q.append(current.right)


def append_child(child, root):
    if root.left is None:
        root.left = child
    else:
        root.right = child
    return root

def build_tree(line):
    line = list(line.replace(' ', ''))
    root = Tree()
    current = root
    q = [current]
    for char in line:
        if char.isnumeric():
            child = Tree(int(char))
            append_number(child, current)
        elif char in '*+':
            if current.value is not None:
                #build node on top
                parent = Tree(char)
                parent.left = current
                current = parent
            else:
                current.value = char
        elif char == '(':
            q.append(current)
            current = Tree()
        elif char == ')':
            parent = q.pop()
            parent = append_child(current, parent)
            current = parent
    return current

def build_tree_precedence(line):
    line = list(line.replace(' ', ''))
    current = Tree()
    q = [current]
    for char in line:
        # print_tree(current)
        if char.isnumeric():
            child = Tree(int(char))
            append_number(child, current)
        elif char == '*':
            if current.value is None:
                current.value = char
            else:
                parent = Tree(char)
                parent.left = current
                current = parent
        elif char == '+':
            if current.value is None:
                current.value = char
            else:
                temp = current.right
                current.right = Tree(char)
                current.right.left = temp
        elif char == '(':
            q.append(current)
            current = Tree()
        elif char == ')':
            parent = q.pop()
            if parent.right is not None and parent.right.value == '+':
                append_number(current, parent.right)
            else:
                append_child(current, parent)
            current = parent

    return current

def print_tree(root):
    q = [root]
    this_level = 1
    next_level = 0

    while q:
        current = q.pop(0)
        print(current.value, end=' ')
        this_level -= 1
        if current.left:
            q.append(current.left)
            next_level += 1
        if current.right:
            q.append(current.right)
            next_level += 1
        if this_level == 0:
            this_level, next_level = next_level, 0
            print()
    print('----')



def solve(root):
    if root is None:
        return
    if isinstance(root.value, int):
        return root.value
    if root.value == '+':
        return solve(root.left) + solve(root.right)
    elif root.value == '*':
        return solve(root.left) * solve(root.right)



if __name__ == '__main__':
    # test = '2 * 3 + (4 * 5)'
    # s = build_tree_precedence(test)
    # q = [s]

    # print_tree(s)
    # print(solve(s))

    # exit()
    code = open('input/day18.txt').read().strip().split('\n')
    result = 0
    res2 = 0
    for line in code:
        s = build_tree(line.replace(' ',''))

        this_result = solve(s)
        result += this_result

        s2 = build_tree_precedence(line)
        this_res2 = solve(s2)
        res2 += this_res2

    print(f'Part 1: {result}')
    print(f'Part 2: {res2}')