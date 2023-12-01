import numpy as np

f = open("input")

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

visited = dict()


class Knot:
    def __init__(self, name, x=0, y=0):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f'knot {self.name}: ({self.x}, {self.y})'

    def move(self, dir):
        if dir == 'R':
            self.x += 1
        if dir == 'L':
            self.x -= 1
        if dir == 'U':
            self.y += 1
        if dir == 'D':
            self.y -= 1

def print_scenery(knot_list, size = 10):
    scenery = np.array([['.'] * size] * size)
    scenery[size - 1][0] = 's'
    for i in range(size-1, -1, -1):
        k = knot_list[i]
        scenery[size -1 - k.y, k.x] = k.name
    print("##################################")
    print(scenery)

def move_next(head, tail, dir, count):
    if dir == 'R':
        if tail.x == head.x - 2:
            tail.x += 1
            tail.y = head.y
            if count:
                visited[(tail.x, tail.y)] = 1

    if dir == 'L':
        if tail.x == head.x + 2:
            tail.x -= 1
            tail.y = head.y
            if count:
                visited[(tail.x, tail.y)] = 1

    if dir == 'U':
        if tail.y == head.y - 2:
            tail.x = head.x
            tail.y += 1
            if count:
                visited[(tail.x, tail.y)] = 1
        elif tail.x == head.x - 2:
            tail.x += 1
            tail.y += head.y

    if  dir == 'D':
        if tail.y == head.y + 2:
            tail.x = head.x
            tail.y -= 1
            if count:
                visited[(tail.x, tail.y)] = 1




knots = [Knot(i) for i in range(10)]
knots[0].name = 'H'
count = 0
for line in f:
    count += 1
    dir, steps = line.split()
    steps = int(steps)
    print(dir, steps)
    head_moves = True
    for i in range(steps):
        knots[0].move(dir)
        for j in range(1, 10):
            move_next(knots[j-1], knots[j], dir, j == 9)
            print(knots[j])
        print_scenery(knots)
    if count == 2:
        break
    print('\n')


print(visited.keys())
print(len(visited.keys()))
if not (0,0) in visited.keys():
    print("(0,0) was not visited")
    print("result: ",    len(visited.keys()) + 1)
else:
    print("result: ", len(visited.keys()))
for k in knots:
    print(k)

