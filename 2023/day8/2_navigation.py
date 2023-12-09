import math
instructions, *navigation = open('input.txt').read().split('\n')

START_NODE = 0
END_NODE = 1
NONE_NODE = -1

SIZE = 6


def getDirection(direction):
    if direction == 'R':
        return 1
    return 0

def getMapPair(line):
    if len(line.strip()) == 0:
        return ("0", "0")
    from_pos, to_pos = line.split("=")
    from_pos = from_pos.strip()
    to_pos = to_pos.strip()
    if from_pos.endswith("A"):
        startNodes.append(from_pos)
    elif from_pos.endswith("Z"):
        endNodes.append(from_pos)

    return (from_pos.strip(), (to_pos[1:4], to_pos[6:9]))


startNodes = []
endNodes = []

navigation_instructions = dict(map(getMapPair, navigation))

# print(instructions)
# print(navigation_instructions)


count = 0
result = startNodes
print(result, endNodes)
already_visited = [[] for i in range(SIZE)]
count_full = 0
cycle_sizes = [0] * SIZE
start_cycles = [0] * SIZE
while True:
    direction = instructions[count % len(instructions)]
    result = [navigation_instructions[res][getDirection(direction)] for res in result]
    print(result)

    for i in range(SIZE):
        visited = already_visited[i]
        if len(visited) >= 2:
            continue
        if len(visited) < 2 and result[i].endswith("Z"):
            visited.append((result[i], count))
        if len(visited) == 2:
            cycle_sizes[i] = abs(visited[0][1] - visited[1][1])
            count_full += 1
    if count_full == SIZE:
        break

    count += 1

print(already_visited)
print(cycle_sizes)
# this works because the first time a Z is hit, is twice the length of the cycle
# so no need to use the chinese reminder theorem
print(math.lcm(*cycle_sizes))

