import numpy as np

gas = []
for line in open('input'):
    gas = list(line)

gas = [1 if g == '>' else -1 for g in gas]
# width, height
rocks = [[]] * 5
tower_height = 0
current_height = 0

rocks[0] = np.array([[1, 1, 1, 1]])
rocks[1] = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
rocks[2] = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
rocks[3] = np.array([[1], [1], [1], [1]])
rocks[4] = np.array([[1, 1], [1, 1]])


def blown(sr, sc, r, g):
    rows, columns = len(r), len(r[0])
    dot_prod = 0
    if g == 1:
        if sc + columns + 1 >= 7:
            return False
        dot_prod = sum(sum(np.multiply(cave[sr:sr + rows, sc + 1:sc + columns + 1], r)))
    elif g == -1:
        if sc - 1 < 0:
            return False
        dot_prod = sum(sum(np.multiply(cave[sr:sr + rows, sc - 1:sc + columns - 1], r)))
    return dot_prod == 0


def down(sr, sc, r):
    rows, columns = len(r), len(r[0])
    if sr + rows == END:
        return False
    dot_prod = sum(sum(np.multiply(cave[sr + 1:sr + 1 + rows, sc:sc + columns], r)))
    return dot_prod == 0


def settle(sr, sc, r):
    rows, columns = len(r), len(r[0])
    # print(sr, sc, r, rows, columns)
    for i in range(rows):
        for j in range(columns):
            # print(sr + i, sc + j)
            if r[i, j] != 0:
                cave[sr + i, sc + j] = 1


def get_start(sc, r, g):
    rows, columns = len(r), len(r[0])
    if g == 1 and sc + columns < 7:
        return sc + 1
    if g == -1 and sc - 1 >= 0:
        return sc - 1
    return sc


END = 3500
ROCKS = 2022
g_i = 0
print("len of gas", len(gas))
count = 1
cave = np.array([[0 for _ in range(7)] for _ in range(END)])

for r_nr in range(ROCKS):
    rock = r_nr % 5
    start = 1

    done = False
    current_height = 0
    g = gas[0]
    while True:
        g = gas[g_i % len(gas)]
        blown_allowed = blown(current_height, start, rocks[rock], g)
        if blown_allowed:
            start = get_start(start, rocks[rock], g)
        down_allowed = down(current_height, start, rocks[rock])
        if down_allowed:
            current_height += 1
            g_i += 1
        else:
            break
    else:
        break

    # print("rock ", rock, "::: current_height", current_height)
    settle(current_height, start, rocks[rock])
    tower_height = max(tower_height, (END - current_height))
    count += 1

    # print(cave)
    # elif rock == 4:
    #     for h in range(2):
    #         cave[current_height - h, start] = 1
    #         cave[current_height, start + h] = 1
    #     tower_height = max(tower_height, (END - current_height) + 2)
    # print("Finishing: current height:", current_height, "tower_height:", tower_height)

# print(cave)
for i in range(END):
    if sum(cave[i]) > 0:
        print(cave[i], sum(cave[i]))
        print(i, END - i)
        break
print("tower_height:", tower_height)
