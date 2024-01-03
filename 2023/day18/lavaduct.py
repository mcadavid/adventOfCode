from itertools import pairwise

def get_values(line):
    direction, distance, color = line.split()
    d = int(distance)
    yield  ((d, 0), (0, d), (-d, 0), (0, -d))['RDLU'.index(direction)]
    d = int(color[2:7], 16)
    # 0 means R, 1 means D, 2 means L, and 3 means U.
    yield  ((d, 0), (0, d), (-d, 0), (0, -d))[int(color[7])]

def digging(steps):
    polygon = []
    acc = (0,0)
    #calculate all the points of the polygon
    for s1, s2 in steps:
        acc = (s1 + acc[0], s2 + acc[1])
        polygon.append(acc)

    result = 0
    # close the path
    path = polygon + [polygon[0]]

    # shoelace formula for the area of a polygon https://en.wikipedia.org/wiki/Shoelace_formula
    for (p1x, p1y), (p2x, p2y) in pairwise(path):
        result += p1x * p2y - p1y * p2x

    result = result // 2

    # Pick's formula for the number of interior points Area=border/2+interior−1. That is interior = Area + 1 - border/2
    # We need all the points, therefore: result = interior + border = Area + 1 + border/2
    # https://mathigon.org/task/picks-theorem
    border = 0
    for (p1x, p1y), (p2x, p2y) in pairwise(path):
        border += abs(p1x - p2x + p1y - p2y) 

    print(result, border // 2, result + border // 2 + 1)

    return result + border // 2 + 1

directions, color_directions = zip(*map(get_values,  open('input.txt', 'r')))
print(digging(directions))
print(digging(color_directions))
