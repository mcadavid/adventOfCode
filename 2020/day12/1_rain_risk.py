def change_facing_180(current):
    return [-1 * current[0], -1 * current[1]]


def change_facing_90_r(current):
    return [current[1], -1 * current[0]]


def change_facing_90_l(current):
    return [-1 * current[1], current[0]]


facing = [1, 0]
pos = [0, 0]
print("start: ", pos, facing)
f = open("input", 'r')
for line in f:
    print(line[0:-1], end=': ')
    dir = line[0]
    units = int(line[1:-1])
    if dir == 'F':
        # pos += units * facing
        pos[0] += units * facing[0]
        pos[1] += units * facing[1]
    elif dir == 'N':
        pos[1] += units
    elif dir == 'S':
        pos[1] -= units
    elif dir == 'E':
        pos[0] += units
    elif dir == 'W':
        pos[0] -= units
    elif units == 180:
        facing = change_facing_180(facing)
    elif units == 270 and dir == 'R':
        facing = change_facing_90_l(facing)
    elif units == 270 and dir == 'L':
        facing = change_facing_90_r(facing)
    elif units == 90 and dir == 'L':
        facing = change_facing_90_l(facing)
    elif units == 90 and dir == 'R':
        facing = change_facing_90_r(facing)
    print(pos, facing)

print(abs(pos[0]) + abs(pos[1]))
