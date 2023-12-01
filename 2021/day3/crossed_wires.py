import sys, itertools

sys.stdin = open("input.txt")

path1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
path2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

path1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
path2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

path1 = list(input().split(','))
path2 = list(input().split(','))


def fill_collections(ver, hor, path):
    start = (0, 0)
    for i in range(len(path)):
        dir = path[i][0]
        steps = int(path[i][1:])
        if dir == 'R':
            end = (start[0] + steps, start[1])
            type = 'H'
        elif dir == 'L':
            end = (start[0] - steps, start[1])
            type = 'H'
        elif dir == 'U':
            end = (start[0], start[1] + steps)
            type = 'V'
        elif dir == 'D':
            end = (start[0], start[1] - steps)
            type = 'V'

        if type == 'V':
            ver.append((start, end))
        elif type == 'H':
            hor.append((start, end))

        start = end


def calculate_min_distance(hor, ver):
    min_distance = sys.maxsize
    for h, v in itertools.product(hor, ver):
        h_start_x = h[0][0]
        h_end_x = h[1][0]
        h_y = h[0][1]

        v_x = v[0][0]
        v_start_y = v[0][1]
        v_end_y = v[1][1]

        # make start smaller for x
        if h_start_x > h_end_x:
            temp = h_start_x
            h_start_x = h_end_x
            h_end_x = temp

        # make start smaller for x
        if v_start_y > v_end_y:
            temp = v_start_y
            v_start_y = v_end_y
            v_end_y = temp

        # if the segments meet
        if h_start_x < v_x < h_end_x and v_start_y < h_y < v_end_y:
            min_distance = min(min_distance, abs(h_y) + abs(v_x))

    return min_distance

v1 = []
h1 = []

v2 = []
h2 = []

fill_collections(v1, h1, path1)
fill_collections(v2, h2, path2)

result = min(calculate_min_distance(h1, v2), calculate_min_distance(h2, v1))

print(result)
