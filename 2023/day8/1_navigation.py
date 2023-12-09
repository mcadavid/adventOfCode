instructions, *navigation = open('input.txt').read().split('\n')


def getDirection(value):
    if direction == 'R':
        return 1
    return 0

def getMapPair(line):
    if len(line.strip()) == 0:
        return ("0", "0")
    from_pos, to_pos = line.split("=")
    to_pos = to_pos.strip()
    return (from_pos.strip(), (to_pos[1:4], to_pos[6:9]))



navigation_instructions = dict(map(getMapPair, navigation))
print(instructions)
#print(navigation_instructions)

count = 0
result = 'AAA'
while result != 'ZZZ':
    direction = instructions[count % len(instructions)]
    result = navigation_instructions[result][getDirection(direction)]
    count += 1



print(count)

