f = open("input.txt")

cycle = 0
register = 1
total = 0

LOG = False


def signal_strength(c, r):
    if cycle in (20, 60, 100, 140, 180, 220):
        print('****************', c, r)
        return c * r
    return 0

for line in f:
    line = line[:-1]
    #print(line)
    if line == 'noop':
        if LOG: print("start", cycle + 1)
        cycle += 1
        total += signal_strength(cycle, register)
        if LOG: print("end", cycle)
    if line != 'noop':
        addx, value = line.split()
        value = int(value)
        if LOG: print("start", cycle + 1)
        cycle += 1
        total += signal_strength(cycle, register)
        if LOG: print("end", cycle)
        if LOG: print("start", cycle + 1)
        cycle += 1
        total += signal_strength(cycle, register)
        if LOG: print("end", cycle)
        register += value
        if LOG: print(register)

print(total)
