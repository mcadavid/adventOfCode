import sys, math


def check_one_ray(p1, p2):
    found = False
    ray_already_visited = False
    if p1 == p2:
        return False
    x_dist = p2[0] - p1[0]
    y_dist = p2[1] - p1[1]
    x_step = 0
    y_step = 0
    ggT = 0
    if x_dist != 0 and y_dist != 0:
        # asteroids can be found in gitter
        # with the ggT you can find the points on the line
        # between p1 and p2 which are integer
        ggT = math.gcd(abs(x_dist), abs(y_dist))
        x_step = x_dist // ggT
        y_step = y_dist // ggT
    elif x_dist == 0:
        ggT = abs(y_dist)
        if y_dist > 0:
            y_step = 1
        else:
            y_step = -1
    elif y_dist == 0:
        ggT = abs(x_dist)
        if x_dist > 0:
            x_step = 1
        else:
            x_step = -1

    for i in range(1, ggT + 1):
        gitter_point = (p1[0] + i * x_step, p1[1] + i * y_step)
        if gitter_point in visited.keys():
            ray_already_visited = True
        elif gitter_point in karte:
            visited[gitter_point] = True
            found = True

    return found and not ray_already_visited


map_input = ['.#..#', '.....', '#####', '....#', '...##']
map_input = ['......#.#.', '#..#.#....', '..#######.', '.#.#.###..', '.#..#.....', '..#....#.#', '#..#....#.',
             '.##.#..###', '##...#..#.', '.#....####']
map_input = ['#.#...#.#.', '.###....#.', '.#....#...', '##.#.#.#.#', '....#.#.#.', '.##..###.#', '..#...##..',
             '..##....##', '......#...', '.####.###.']
map_input = ['.#..##.###...#######', '##.############..##.', '.#.######.########.#', '.###.#######.####.#.',
             '#####.##.#.##.###.##', '..#####..#.#########', '####################', '#.####....###.#.#.##',
             '##.#################', '#####.##.###..####..', '..######..##.#######', '####.##.####...##..#',
             '.#####..#.######.###', '##...#.##########...', '#.##########.#######', '.####.#.###.###.#.##',
             '....##.##.###..#####', '.#.#.###########.###', '#.#.#.#####.####.###', '###.##.####.##.#..##']




sys.stdin = open("input.txt")
karte = set()
visited = dict()
# m = len(map_input)
i = 0
while True:
    try:
        line = input()
        n = len(line)
        for j in range(n):
            if line[j] == '#':
                karte.add((j, i))
        i += 1
    except EOFError:
        break

m = i
max_asteroids = 0
base_asteroid = (0, 0)
for point1 in karte:
    visible_asteroids = 0
    visited = dict()
    for point2 in karte:
        if point2 != point1 and point2 not in visited.keys() and check_one_ray(point1, point2):
            visible_asteroids += 1

    if max_asteroids < visible_asteroids:
        max_asteroids = visible_asteroids
        base_asteroid = point1
        print(point1)

print(max_asteroids)
print(base_asteroid)
