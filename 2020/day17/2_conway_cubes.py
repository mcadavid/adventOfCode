from itertools import product
from copy import deepcopy

MAX_SPACE = 25
ZERO = 9
INACTIVE = '.'
ACTIVE = '#'


def print_level(level1, level2):
    for i in range(MAX_SPACE):
        for j in range(MAX_SPACE):
            print(space[i][j][level1][level2], end='')
        print()


def count_neighbours(grid2, x, y, z, w):
    deltas = []
    for i, j, k, l in product([0, 1, -1], [0, 1, -1], [0, 1, -1], [0, 1, -1]):
        deltas.append((i, j, k, l))
    deltas.remove((0, 0, 0, 0))

    total = 0
    for dx, dy, dz, dw in deltas:
        xx, yy, zz, ww = x + dx, y + dy, z + dz, w + dw
        total += grid2[xx][yy][zz][ww] == ACTIVE

    return total


n = MAX_SPACE
space = [[[['.' for k in range(n)] for j in range(n)] for i in range(n)] for l in range(n)]
f = open('input1', 'r')

counter = ZERO
for line in f:
    line = line[0:-1]
    for i in range(len(line)):
        space[counter][i + ZERO][ZERO][ZERO] = line[i]
    counter += 1

print_level(ZERO, ZERO)

grid = deepcopy(space)
for _ in range(6):
    for i, j, k, l in product(range(MAX_SPACE - 2), range(MAX_SPACE - 2), range(MAX_SPACE - 2), range(MAX_SPACE - 2)):
        n = count_neighbours(space, i, j, k, l)
        if grid[i][j][k][l] == ACTIVE:
            if 2 <= n <= 3:
                grid[i][j][k][l] = ACTIVE
            else:
                grid[i][j][k][l] = INACTIVE
        elif n == 3:
            grid[i][j][k][l] = ACTIVE
    space = deepcopy(grid)

total_occupied = 0
for i, j, k, l in product(range(MAX_SPACE), range(MAX_SPACE), range(MAX_SPACE), range(MAX_SPACE)):
    if grid[i][j][k][l] == ACTIVE:
        total_occupied += 1
print(total_occupied)

