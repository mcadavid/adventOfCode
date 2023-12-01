import numpy as np
f = open("input.txt")

def print_crt(crt):
    print(np.array(crt))
    #print(crt[0])

cycle = 0
register = 1

LOG = False

crt = [''] * 6
print_crt(crt)

def draw(cycle, sprite_pos):
    pos = ((cycle - 1) // 40, (cycle - 1) % 40)
    if pos[1] % 5 == 0:
        crt[pos[0]] += '   '
    if LOG: print(cycle, pos, sprite_pos)
    if  sprite_pos - 1 <= pos[1] <= sprite_pos + 1:
        crt[pos[0]] += '#'
    else:
        crt[pos[0]] += '.'


for line in f:
    if cycle == 40: break
    line = line[:-1]
    #print(line)
    if line == 'noop':
        if LOG: print("start", cycle + 1)
        cycle += 1
        draw(cycle, register)
        if LOG: print("end", cycle)
    if line != 'noop':
        addx, value = line.split()
        value = int(value)
        if LOG: print("start", cycle + 1)
        cycle += 1
        draw(cycle, register)
        if LOG: print("end", cycle)
        if LOG: print("start", cycle + 1)
        cycle += 1
        draw(cycle, register)
        if LOG: print("end", cycle)
        register += value
        if LOG: print(register)

print_crt(crt)
