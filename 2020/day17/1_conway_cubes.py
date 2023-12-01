from itertools import product
from copy import deepcopy

MAX_SPACE = 25
ZERO = 9
INACTIVE = '.'
ACTIVE = '#'


def print_level(level):
    for i in range(MAX_SPACE):
        for j in range(MAX_SPACE):
            print(space[i][j][level], end='')
        print()


def count_neighbous(grid2, x, y, z):
    deltas = (
        (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, 1, 1), (0, 1, -1), (0, -1, 0), (0, -1, 1), (0, -1, -1),
        (-1, 0, 0), (-1, 0, 1), (-1, 0, -1), (-1, 1, 0), (-1, 1, 1), (-1, 1, -1), (-1, -1, 0), (-1, -1, 1),
        (-1, -1, -1),
        (1, 0, 0), (1, 0, 1), (1, 0, -1), (1, 1, 0), (1, 1, 1), (1, 1, -1), (1, -1, 0), (1, -1, 1), (1, -1, -1),
    )

    total = 0
    for dx, dy, dz in deltas:
        xx, yy, zz = x + dx, y + dy, z + dz
        total += grid2[xx][yy][zz] == ACTIVE

    return total


n = MAX_SPACE
space = [[['.' for k in range(n)] for j in range(n)] for i in range(n)]
f = open('input1', 'r')

counter = ZERO
for line in f:
    line = line[0:-1]
    for i in range(len(line)):
        space[counter][i + ZERO - 3][ZERO] = line[i]
    counter += 1

print_level(ZERO)

grid = deepcopy(space)
for _ in range(6):
    for i, j, k in product(range(MAX_SPACE - 2), range(MAX_SPACE - 2), range(MAX_SPACE - 2)):
        n = count_neighbous(space, i, j, k)
        if grid[i][j][k] == ACTIVE:
            if 2 <= n <= 3:
                grid[i][j][k] = ACTIVE
            else:
                grid[i][j][k] = INACTIVE
        elif n == 3:
            grid[i][j][k] = ACTIVE
    space = deepcopy(grid)

total_occupied = 0
for i, j, k in product(range(MAX_SPACE), range(MAX_SPACE), range(MAX_SPACE)):
    if grid[i][j][k] == ACTIVE:
        total_occupied += 1
print(total_occupied)
print_level(ZERO)
