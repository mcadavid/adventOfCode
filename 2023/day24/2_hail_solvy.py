from sympy.solvers import solve
from sympy import Symbol

# Solvy is too slow to check all solutions, but for three lines it is enough
# The data was chosen, that the first three lines would already intersect in one point
# Of course because if you have more points you would have a plane and none of the lines were coplanar!!!!!
f = open('input.txt')

lines = []

for line in f:
    line = line.strip()
    pos, velocity = line.split('@')
    lines.append((list(map(int, pos.split(','))),
                 list(map(int, velocity.split(',')))))

x, y, z, vx, vy, vz = Symbol('x'), Symbol('y'), Symbol(
    'z'), Symbol('vx'), Symbol('vy'), Symbol('vz')
t = [Symbol('t' + str(i)) for i in range(len(lines))]
equations = []
count = 0
break_val = 5
for [x1, y1, z1], [vx1, vy1, vz1] in lines:
    equations.append(x - x1 + t[count]*vx - t[count]*vx1)
    equations.append(y - y1 + t[count]*vy - t[count]*vy1)
    equations.append(z - z1 + t[count]*vz - t[count]*vz1)
    count += 1
    if count == break_val:
        break
print(equations)
solutions = solve(equations, *([x, y, z, vx, vy, vz] + t[0:break_val]))

print(solutions[0][0] + solutions[0][1] + solutions[0][2])

print(solutions)


# Hailstone: 19, 13, 30 @ -2, 1, -2
# Collision time: 5
# Collision position: 9, 18, 20

# Hailstone: 18, 19, 22 @ -1, -1, -2
# Collision time: 3
# Collision position: 15, 16, 16

# Hailstone: 20, 25, 34 @ -2, -2, -4
# Collision time: 4
# Collision position: 12, 17, 18

# Hailstone: 12, 31, 28 @ -1, -2, -1
# Collision time: 6
# Collision position: 6, 19, 22

# Hailstone: 20, 19, 15 @ 1, -5, -3
# Collision time: 1
# Collision position: 21, 14, 12
