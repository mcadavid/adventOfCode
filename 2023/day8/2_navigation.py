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
count_full = 0
cycle_sizes = [0] * SIZE
while True:
    direction = instructions[count % len(instructions)]
    result = [navigation_instructions[res][getDirection(direction)] for res in result]
    # print(result)

    for i in range(SIZE):
        if cycle_sizes[i] == 0 and result[i].endswith("Z"):
            cycle_sizes[i] = count + 1
            count_full += 1
    
    if count_full == SIZE:
        break

    count += 1

print(cycle_sizes)
# this works because the first time a Z is hit, is twice the length of the cycle
# so no need to use the chinese reminder theorem
# and what is called cycle sizes would be the as of CRT in x = a_i mod n_i
# and n_i are the really cycle sizes
print(math.lcm(*cycle_sizes))

