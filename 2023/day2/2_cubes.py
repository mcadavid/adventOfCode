f = open("input.txt", 'r')

sum = 0
for line in f:
    line = line.strip()
    parts = line.split()
    max_blue = 0
    max_red = 0
    max_green = 0
    gameId = int(parts[1][0:-1])
    value = 0
    # print(line)
    for i in range(2, len(parts)):
        part = parts[i]
        if part.startswith('red'):
            max_red = max(max_red, value)
        elif part.startswith('green'):
            max_green = max(max_green, value)
        elif part.startswith('blue'):
            max_blue = max(max_blue, value)
        else:
            value = int(part)

    sum += max_red * max_green * max_blue

print(sum)
