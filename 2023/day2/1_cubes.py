f = open("input.txt", 'r')
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

sum = 0
for line in f:
    line = line.strip()
    parts = line.split()
    gameId = int(parts[1][0:-1])
    value = 0
    valid = True
    # print(line)
    for i in range(2, len(parts)):
        part = parts[i]
        if part.startswith('blue'):
            if value > MAX_BLUE:
                valid = False
                break
        elif part.startswith('red'):
            if value > MAX_RED:
                valid = False
                break
        elif part.startswith('green'):
            if value > MAX_GREEN:
                valid = False
                break
        else:
            value = int(part)

    if valid:
        sum += gameId

print(sum)
