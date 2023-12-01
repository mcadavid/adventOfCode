import sys

f = open("input.txt")
LINE = 10
LINE = 2000000


def read(string):
    sl = string.split()
    return int(sl[-2].strip(',').split('=')[1]), int(sl[-1].strip(',').split('=')[1])

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = []
x_min = sys.maxsize
x_max = -sys.maxsize
inLine = set()
for line in f:
    print(line.strip())
    s, b = line.strip().split(':')
    sx, sy = read(s)
    bx, by = read(b)
    if sy == LINE:
        inLine.add(s)
    elif by == LINE:
        inLine.add(b)
    x_min = min(x_min, sx, bx)
    x_max = max(x_max, sx, bx)
    sensors.append(((sx,sy), distance((sx,sy), (bx,by))))

result = set()
reduced = len(inLine)
for s, r in sensors:
    d = abs(LINE - s[1])
    print(s, "r", r, "d", d)
    if d > r:
        print(s, "does not reach line")
        continue
    diff = r - d
    for i in range(s[0] - diff, s[0] + diff + 1):
        result.add(i)
    #print(result)
print(sensors)
print(len(result),reduced, len(result)-reduced)

