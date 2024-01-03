from z3 import *

f = open('input_init.txt')

lines = []

for line in f:
    line = line.strip()
    pos, velocity = line.split('@')
    lines.append((list(map(int, pos.split(','))), list(map(int, velocity.split(',')))))

x, y, z, vx, vy, vz = Int('x'), Int('y'), Int('z'), Int('vx'), Int('vy'), Int('vz')
t = [Int('t'+ str(i)) for i in range(len(lines)) ]
solver = Solver()
count = 0
for [x1, y1, z1], [vx1, vy1, vz1] in lines:
    solver.add(x - x1 + t[count]*vx - t[count]*vx1 == 0)
    solver.add(y - y1 + t[count]*vy - t[count]*vy1 == 0)
    solver.add(z - z1 + t[count]*vz - t[count]*vz1 == 0)
    count += 1

solver.check()
M = solver.model()
print(M[x], M[y], M[z], M[vx], M[vy], M[vz])
print(M[x].as_long() + M[y].as_long() + M[z].as_long())




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
