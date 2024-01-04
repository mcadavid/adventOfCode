from itertools import combinations
import sys

f = open('input.txt')
range_l = 200000000000000
range_r = 400000000000000
# range_l = 7
# range_r = 27

lines = []

for line in f:
    line = line.strip()
    pos, velocity = line.split('@')
    lines.append((list(map(int, pos.split(',')))[0:2], list(
        map(int, velocity.split(',')))[0:2]))


# print(lines)
result = 0
min_coor = sys.maxsize
min_d = sys.maxsize
max_coor = 0
max_d = -sys.maxsize
for ([x1, y1], [vx1, vy1]), ([x2, y2], [vx2, vy2]) in combinations(lines, 2):
    # print([x1,y1], [vx1, vy1])
    # print([x2,y2], [vx2, vy2])
    min_coor = min(min_coor, x1, y1)
    min_d = min(min_d, vx1, vy1)
    max_coor = max(max_coor, x1, y1)
    max_d = max(max_d, vx1, vy1)
    m1 = vy1 / vx1
    m2 = vy2 / vx2
    b1 = y1 - m1 * x1
    b2 = y2 - m2 * x2
    if m1 == m2:  # lines are parallel
        if b1 == b2:
            result += 1  # the lines will only intersect if they are equal
        print("parallel lines: m, b", m1, b1)
    else:
        # m1 != m2
        x = (b2 - b1) / (m1 - m2)
        if range_l <= x <= range_r:
            y = m1 * x + b1
            if range_l <= y <= range_r:
                # print("Meet point:", (x,y))
                t1 = (x - x1) / vx1
                t2 = (x - x2) / vx2
                if t1 > 0 and t2 > 0:
                    result += 1
                elif t1 == 0 or t2 == 0:
                    print("t1 or t2 are 0")


print(result)
print(min_coor, min_d)
print(max_coor, max_d)


# Hailstone A: 19, 13, 30 @ -2, 1, -2
# Hailstone B: 18, 19, 22 @ -1, -1, -2
# Hailstones' paths will cross inside the test area (at x=14.333, y=15.333).

# Hailstone A: 19, 13, 30 @ -2, 1, -2
# Hailstone B: 20, 25, 34 @ -2, -2, -4
# Hailstones' paths will cross inside the test area (at x=11.667, y=16.667).

# Hailstone A: 19, 13, 30 @ -2, 1, -2
# Hailstone B: 12, 31, 28 @ -1, -2, -1
# Hailstones' paths will cross outside the test area (at x=6.2, y=19.4).

# Hailstone A: 19, 13, 30 @ -2, 1, -2
# Hailstone B: 20, 19, 15 @ 1, -5, -3
# Hailstones' paths crossed in the past for hailstone A.

# Hailstone A: 18, 19, 22 @ -1, -1, -2
# Hailstone B: 20, 25, 34 @ -2, -2, -4
# Hailstones' paths are parallel; they never intersect.

# Hailstone A: 18, 19, 22 @ -1, -1, -2
# Hailstone B: 12, 31, 28 @ -1, -2, -1
# Hailstones' paths will cross outside the test area (at x=-6, y=-5).

# Hailstone A: 18, 19, 22 @ -1, -1, -2
# Hailstone B: 20, 19, 15 @ 1, -5, -3
# Hailstones' paths crossed in the past for both hailstones.

# Hailstone A: 20, 25, 34 @ -2, -2, -4
# Hailstone B: 12, 31, 28 @ -1, -2, -1
# Hailstones' paths will cross outside the test area (at x=-2, y=3).

# Hailstone A: 20, 25, 34 @ -2, -2, -4
# Hailstone B: 20, 19, 15 @ 1, -5, -3
# Hailstones' paths crossed in the past for hailstone B.

# Hailstone A: 12, 31, 28 @ -1, -2, -1
# Hailstone B: 20, 19, 15 @ 1, -5, -3
# Hailstones' paths crossed in the past for both hailstones.
