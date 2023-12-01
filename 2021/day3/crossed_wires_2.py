import sys, itertools

sys.stdin = open("input.txt")

path1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
path2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

path1 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
path2 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']


path1 = list(input().split(','))
path2 = list(input().split(','))

def fill_collections(ver, hor, path):
    start = (0, 0)
    d = 0
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
            ver.append((start, end, d, dir))
        elif type == 'H':
            hor.append((start, end, d, dir))
        d += steps
        start = end


def calculate_min_distance(hor, ver, i):
    min_distance = sys.maxsize
    min_steps = sys.maxsize
    for h, v in itertools.product(hor, ver):
        h_start_x = h[0][0]
        h_end_x = h[1][0]
        h_y = h[0][1]
        d1 = h[2]
        dir1 = h[3]

        v_x = v[0][0]
        v_start_y = v[0][1]
        v_end_y = v[1][1]
        d2 = v[2]
        dir2 = v[3]

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
            print("intersection point", v_x, h_y)
            print(d1, dir1, d2, dir2)
            min_distance = min(min_distance, abs(h_y) + abs(v_x))
            steps1 = d1
            if dir1 == 'R':
                steps1 += v_x - h_start_x
            elif dir1 == 'L':
                steps1 += h_end_x - v_x

            print(steps1)

            steps2 = d2
            if dir2 == 'U':
                steps2 += h_y - v_start_y
            elif dir2 == 'D':
                steps2 += v_end_y - h_y

            print(steps2)

            min_steps = min(min_steps, steps1 + steps2)
            print(d1, d2, steps1 + steps2, min_steps)

    return min_distance, min_steps


v1 = []
h1 = []

v2 = []
h2 = []

fill_collections(v1, h1, path1)
fill_collections(v2, h2, path2)

result, steps_result = calculate_min_distance(h1, v2, 1)
result2, steps_result2 = calculate_min_distance(h2, v1, 2)

print("Min-Distance", min(result, result2))
print("Steps", min(steps_result, steps_result2))
