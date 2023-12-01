from copy import deepcopy

OCCUPIED = '#'
FREE = 'L'
FLOOR = '.'
PRINT = False


def check(i, j):
    return previous[i][j] == OCCUPIED


def print_seats():
    if not PRINT:
        return
    for i in range(n):
        for j in range(m):
            print(seats[i][j], end='')
        print()
    print()


def count_neighbours():
    count = 0
    if i > 0 and j > 0 and previous[i - 1][j - 1] == OCCUPIED:
        count += 1
    if i > 0 and previous[i - 1][j] == OCCUPIED:
        count += 1
    if i > 0 and j < m - 1 and previous[i - 1][j + 1] == OCCUPIED:
        count += 1
    if j > 0 and previous[i][j - 1] == OCCUPIED:
        count += 1
    if j < m - 1 and previous[i][j + 1] == OCCUPIED:
        count += 1
    if i < n - 1 and j > 0 and previous[i + 1][j - 1] == OCCUPIED:
        count += 1
    if i < n - 1 and previous[i + 1][j] == OCCUPIED:
        count += 1
    if i < n - 1 and j < m - 1 and previous[i + 1][j + 1] == OCCUPIED:
        count += 1
    return count


def occupied_neighbors(grid, r, c):
    deltas = (
        (-1, 0), (1, 0), (0, 1), (0, -1),
        (-1, 1), (-1, -1), (1, 1), (1, -1)
    )

    total = 0
    for dr, dc in deltas:
        rr, cc = r + dr, c + dc
        if 0 <= rr < n and 0 <= cc < m:
            total += grid[rr][cc] == OCCUPIED

    return total


f = open("input", 'r')
seats = []
status = []

for line in f:
    seats.append(list(line[0:-1]))

n = len(seats)
m = len(seats[0])
print_seats()
step = 0
previous = deepcopy(seats)
break1 = False
total = 0
while True:  # new_no_occupied != no_occupied:
    previous = deepcopy(seats)
    step += 1
    for i in range(n):
        for j in range(m):
            if seats[i][j] == FLOOR:
                continue
            count = count_neighbours()
            if seats[i][j] == FREE and count == 0:
                seats[i][j] = OCCUPIED
                total += 1
            elif seats[i][j] == OCCUPIED and count >= 4:
                seats[i][j] = FREE
                total -= 1

    if break1:
        break
    print_seats()
    if previous == seats:
        break
print()
print(total)
# 2503
