import sys, math

pts = [[5, 2], [4, 1], [3.5, 1], [1, 2], [2, 1], [3, 1], [3, 3], [4, 3]]
origin = [2, 3]
refvec = [0, 1]


def clockwiseangle_and_distance(point):
    y = -1 * point[1]
    y_origin = -1 * origin[-1]
    # Vector between point and the origin: v = p - o
    vector = [point[0] - origin[0], y - y_origin]
    # Length of vector: ||v||
    lenvector = math.hypot(vector[0], vector[1])
    # If length is zero there is no angle
    if lenvector == 0:
        return -math.pi, 0
    # Normalize vector: v/||v||
    normalized = [vector[0] / lenvector, vector[1] / lenvector]
    dotprod = normalized[0] * refvec[0] + normalized[1] * refvec[1]  # x1*x2 + y1*y2
    diffprod = refvec[1] * normalized[0] - refvec[0] * normalized[1]  # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    # Negative angles represent counter-clockwise angles so we need to subtract them
    # from 2*pi (360 degrees)
    if angle < 0:
        return 2 * math.pi + angle, lenvector
    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    return angle, lenvector


def are_collinear(p1, p2, p3):
    a = p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])
    if a == 0:
        return True

    return False


# map_input = ['.#..#', '.....', '#####', '....#', '...##']
# map_input = ['......#.#.', '#..#.#....', '..#######.', '.#.#.###..', '.#..#.....', '..#....#.#', '#..#....#.',
#              '.##.#..###', '##...#..#.', '.#....####']
# map_input = ['#.#...#.#.', '.###....#.', '.#....#...', '##.#.#.#.#', '....#.#.#.', '.##..###.#', '..#...##..',
#              '..##....##', '......#...', '.####.###.']
map_input = ['.#..##.###...#######', '##.############..##.', '.#.######.########.#', '.###.#######.####.#.',
             '#####.##.#.##.###.##', '..#####..#.#########', '####################', '#.####....###.#.#.##',
             '##.#################', '#####.##.###..####..', '..######..##.#######', '####.##.####...##..#',
             '.#####..#.######.###', '##...#.##########...', '#.##########.#######', '.####.#.###.###.#.##',
             '....##.##.###..#####', '.#.#.###########.###', '#.#.#.#####.####.###', '###.##.####.##.#..##']

#map_input = ['.#....#####...#..','##...##.#####..##', '##...#...#.#####.', '..#.....#...###..', '..#.#.....#....##']
sys.stdin = open("input.txt")
karte = []
visited = dict()
m = len(map_input)
i = 0
while True:
    try:
        line = input()
        n = len(line)
        for j in range(n):
            if line[j] == '#':
                karte.append((j, i))
        i += 1
    except EOFError:
        break

# for i in range(len(map_input)):
#     line = map_input[i]
#     n = len(line)
#     print(line)
#     for j in range(n):
#         if line[j] == '#':
#             karte.append((j, i))
#
#
# m = len(map_input)
# print(karte)
m = i
# origin = [11, 13]
# origin = (11, 13)
origin = [28, 29]
refvec = [0, 1]
col = sorted(karte, key=clockwiseangle_and_distance)
print(col)

counter = 1
bombed = 0
while len(col) > 1 and counter - 1 < len(col):
    p = col[counter]
    bombed += 1
    print(counter, bombed, p)
    if bombed == 201:
        break
    col.remove(p)
    while counter < len(col) and are_collinear(origin, p, col[counter]):
        counter += 1

    if counter >= len(col):
        counter = 1

print(p, p[0] * 100 + p[1])
