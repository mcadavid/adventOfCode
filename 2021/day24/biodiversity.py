import copy

GRID_SIZE = 5
TOTAL_GRID_SIZE = GRID_SIZE * GRID_SIZE


def count_bugs(i, current):
    bugs = 0
    if i + GRID_SIZE < TOTAL_GRID_SIZE and current[i + GRID_SIZE] == '1':
        bugs += 1
    if i - GRID_SIZE >= 0 and current[i - GRID_SIZE] == '1':
        bugs += 1
    if i % GRID_SIZE > 0 and current[i - 1] == '1':
        bugs += 1
    if i % GRID_SIZE != 4 and current[i + 1] == '1':
        bugs += 1
    return bugs


def next_generation(current):
    new_gen = ''
    for i in range(TOTAL_GRID_SIZE):
        bugs = count_bugs(i, current)
        if current[i] == '1':
            if bugs == 1:
                new_gen += '1'
            else:
                new_gen += '0'
        else:
            if bugs == 1 or bugs == 2:
                new_gen += '1'
            else:
                new_gen += '0'
    return new_gen


with open("input.txt") as infile:
    lines = infile.read().split('\n')

eris = ''
for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        if lines[y][x] == '.':
            eris += '0'
        else:
            eris += '1'

print("eris =", eris)
print(int(eris, 2))

repeating = set()
next_value = eris
while True:
    next_value = next_generation(next_value)
    print(next_value)
    if next_value in repeating:
        print(next_value)
        print(int(next_value[TOTAL_GRID_SIZE :: -1], 2))
        break
    repeating.add(next_value)


