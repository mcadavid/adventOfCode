from collections import defaultdict

f = open("input.txt")

offsets = [(.5, 0, 0), (-.5, 0, 0), (0, .5, 0), (0, -.5, 0), (0, 0, .5), (0, 0, -.5)]
faces_count = defaultdict(int)
cubes = []
for line in f:
    x, y, z = map(int, line.strip().split(','))
    cubes.append((x, y, z))

for x, y, z in cubes:
    for dx, dy, dz in offsets:
        face = (x + dx, y + dy, z + dz)
        faces_count[face] += 1

print(list(faces_count.values()).count(1))
print(faces_count.keys())
