def change_facing_180(current):
    return [-1 * current[0], -1 * current[1]]


def change_facing_90_cw(wp):
    return [wp[1], -1 * wp[0]] # multipty by -i


def change_facing_90_acw(wp):
    return [-1 * wp[1], wp[0]] # multiply by i


pos = [0, 0]
waypoint = [10, 1]

print("start: ", pos, waypoint)
f = open("input", 'r')
for line in f:
    print(line[0:-1], end=': ')
    dir = line[0]
    units = int(line[1:-1])
    if dir == 'F':
        # pos += units * facing
        pos[0] += units * waypoint[0]
        pos[1] += units * waypoint[1]
    elif dir == 'N':
        waypoint[1] += units
    elif dir == 'S':
        waypoint[1] -= units
    elif dir == 'E':
        waypoint[0] += units
    elif dir == 'W':
        waypoint[0] -= units
    elif units == 180:
        waypoint = change_facing_180(waypoint)
    elif units == 270 and dir == 'R':
        waypoint = change_facing_90_acw(waypoint)
    elif units == 270 and dir == 'L':
        waypoint = change_facing_90_cw(waypoint)
    elif units == 90 and dir == 'L':
        waypoint = change_facing_90_acw(waypoint)
    elif units == 90 and dir == 'R':
        waypoint = change_facing_90_cw(waypoint)
    print(pos, waypoint)

print(abs(pos[0]) + abs(pos[1]))
