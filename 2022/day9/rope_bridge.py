f = open("input")

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

visited = dict()

for line in f:
    dir, steps = line.split()
    steps = int(steps)

    if dir == 'R':
        for i in range(steps):
            if tail_x == head_x - 1:
                tail_x += 1
                tail_y = head_y
                visited[(tail_x, tail_y)] = 1
            head_x += 1

    if dir == 'L':
        for i in range(steps):
            if tail_x == head_x + 1:
                tail_x -= 1
                tail_y = head_y
                visited[(tail_x, tail_y)] = 1
            head_x -= 1

    if dir == 'U':
        for i in range(steps):
            if tail_y == head_y - 1:
                tail_x = head_x
                tail_y += 1
                visited[(tail_x, tail_y)] = 1
            head_y += 1

    if  dir == 'D':
        for i in range(steps):
            if tail_y == head_y + 1:
                tail_x = head_x
                tail_y -= 1
                visited[(tail_x, tail_y)] = 1
            head_y -= 1






print(visited.keys())
print(len(visited.keys()))
if not (0,0) in visited.keys():
    print("(0,0) was not visited")
    print("result: ",    len(visited.keys()) + 1)
else:
    print("result: ", len(visited.keys()))

